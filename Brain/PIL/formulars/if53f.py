from Vu.Memory.data_factory import DataFactory

class F53F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        result = {}
        eg35 = "EG35"
        domains = set()
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [],"Industry/Domain": [], "Function/Domain": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Function/Domain":[], "Interim Position":[]})
        fl_job_consultancy = fl_job[fl_job["Industry/Domain"] == "Consultancy"]
        fl_job_consultancy_jid = fl_job_consultancy["JID"].values
        fl_assignment_ip = fl_assignment[fl_assignment["Interim Position"] == "yes"]

        domains.update(fl_assignment_ip["Function/Domain"].values)

        fl_job_not_consultancy = fl_job[fl_job["Industry/Domain"] != "Consultancy"]
        fl_job_not_consultancy_fd = fl_job_not_consultancy["Function/Domain"].values
        domains.update(fl_job_not_consultancy_fd)

        result[eg35] = len(domains)
        return result

iff = F53F()
print(iff.getScore("FL-00001"))
