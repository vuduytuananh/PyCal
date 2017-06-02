from Vu.Memory.data_factory import DataFactory

class F54F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        result = {}
        eg36 = "EG36"
        domains = set()
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [],"Industry/Domain": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Industry/Domain":[], "Interim Position":[]})
        fl_job_consultancy = fl_job[fl_job["Industry/Domain"] == "Consultancy"]
        fl_job_consultancy_jid = fl_job_consultancy["JID"].values
        fl_assignment_ip = fl_assignment[fl_assignment["Interim Position"] == "yes"]

        idomains = fl_assignment_ip["Industry/Domain"].values
        domains.update(idomains)

        fl_job_not_consultancy = fl_job[fl_job["Industry/Domain"] != "Consultancy"]
        fl_job_not_consultancy_id = fl_job_not_consultancy["Industry/Domain"].values
        domains.update(fl_job_not_consultancy_id)

        result[eg36] = len(domains)
        return result
