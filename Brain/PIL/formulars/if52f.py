from Vu.Memory.data_factory import DataFactory

class F52F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        result = {}
        eg34 = "EG34"
        names = set()
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [],"Industry/Domain": [], "Company name": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Client name": [], "Interim Position": []})

        fl_job_ID = fl_job[fl_job["Industry/Domain"] == "Consultancy"]
        fl_job_ID_jid = fl_job_ID["JID"].values
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_ID_jid)]
        fl_assignment_jid_clients = fl_assignment_jid["Client name"].values
        names.update(fl_assignment_jid_clients)

        fl_job_not_consultancy = fl_job[fl_job["Industry/Domain"] != "Consultancy"]
        fl_job_not_consultancy_cn = fl_job_not_consultancy["Company name"].values
        names.update(fl_job_not_consultancy_cn)

        result[eg34] = len(names)
        return result

iff = F52F()
print(iff.getScore("FL-00001"))
