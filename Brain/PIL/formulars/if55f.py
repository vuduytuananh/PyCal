from Vu.Memory.data_factory import DataFactory

class F55F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        result = {}
        eg37 = "EG37"
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [],"Industry/Domain": [], "Management Position": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Assignment ID":[], "Industry/Domain":[], "Interim Position":[]})

        fl_job_not_consultancy_mp = fl_job[(fl_job["Industry/Domain"] != "Consultancy") & (fl_job["Management Position"] == "yes")]
        jids = fl_job_not_consultancy_mp["JID"].values
        result[eg37] = len(jids)

        fl_job_consultancy = fl_job[fl_job["Industry/Domain"] == "Consultancy"]
        fl_job_consultancy_jid = fl_job_consultancy["JID"].values

        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_consultancy_jid)]
        fl_assignment_ip = fl_assignment_jid[fl_assignment_jid["Interim Position"] == "yes"]
        fl_assignment_ip_aid = fl_assignment_ip["Assignment ID"].values
        result[eg37] += len(fl_assignment_ip_aid)

        return result

iff = F55F()
print(iff.getScore("FL-00001"))
