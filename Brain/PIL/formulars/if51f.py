from Vu.Memory.data_factory import DataFactory
import math
class F51F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg33 = "EG33"
        result = {}
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [], "Industry/Domain": [], "Company Size": [], "Duration JOB": [], "Self Employed": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Interim Position": [], "Client Size": [], "Duration": []})

        fl_job_se = fl_job[fl_job["Self Employed"] == "yes"]
        fl_job_se_jid = fl_job_se["JID"].values
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_se_jid)]
        fl_assignment_jid_ip = fl_assignment_jid[fl_assignment_jid["Interim Position"] == "yes"]
        fl_assignment_grouped = fl_assignment_jid_ip.groupby("Client Size")["Duration"]
        assignment_out = {k: math.fsum(list(v)) for k, v in fl_assignment_grouped}

        fl_job_nse = fl_job[(fl_job["Self Employed"] == "no") & (fl_job["Industry/Domain"] != "Consultancy")]
        fl_job_grouped = fl_job_nse.groupby("Company Size")["Duration JOB"]
        job_out = {k: math.fsum(list(v)) for k, v in fl_job_grouped}

        result[eg33] = { k: assignment_out.get(k, 0) + job_out.get(k, 0) for k in set(assignment_out) | set(job_out) }
        return result

iff = F51F()
print(iff.getScore("FL-00001"))
