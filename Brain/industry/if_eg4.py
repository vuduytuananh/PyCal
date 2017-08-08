from PyCal.Memory.data_factory import DataFactory
from PyCal.Brain.industry.merge import merge
class IF_EG_1_4:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid, sub_industry):
        eg_1_4 = "EG_1_4"
        result = {}

        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [], sub_industry: [], "Function/Domain": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], sub_industry: [], "Function/Domain": []})
        """
        1. Check INDUSTRY (Domain) column in the job tab
        A) If the Input is Consultancy then:
        """
        fl_job_consultancy = fl_job[fl_job[sub_industry] == "Consultancy"]

        """
        2.go to assignment tab and work only with Assignments related to that specific Consultancy Jobs ID
        """
        fl_job_consultancy_jid = fl_job_consultancy["JID"].values
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_consultancy_jid)]
        """
        3. then count the number of different FUNCTIONS (Domain) of each particular INDUSTRY (Domain) (Assignment tab)
        """
        fl_assignment_jid_grouped = fl_assignment_jid.groupby(sub_industry)["Function/Domain"]
        a_out = {k: set(v) for k,v in fl_assignment_jid_grouped}

        """
        B) If the input is not a Consultancy then:
        2. count the number of different FUNCTIONS (Domain) (column in job tab) of each particular INDUSTRY (Domain)
        """
        fl_job_not_consultancy = fl_job[fl_job[sub_industry] != "Consultancy"]
        fl_job_not_consultancy_grouped = fl_job_not_consultancy.groupby(sub_industry)["Function/Domain"]
        b_out = {k: set(v) for k,v in fl_job_not_consultancy_grouped}

        merged = merge(a_out, b_out)
        result[eg_1_4] = {k: len(v) for k,v in merged.items()}
        return result
