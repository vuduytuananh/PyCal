from PyCal.Memory.data_factory import DataFactory

class IF_EG_1_2_EG_1_3:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid, sub_industry):
        eg_1_2 = "EG_1_2"
        eg_1_3 = "EG_1_3"
        result = {}
        """
        NOTE: use formula of IF2 to represent the document for all the influencers that use EG2 + EG3
        """
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], sub_industry: [], "JID": [], "Company Name": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], sub_industry: [], "Client name": []})
        """
        1. Check INDUSTRY (Domain) column in the job tab
        A) If the Input is Consultancy then:
        2. then go to assignment tab and work only with Assignments related to that specific Consultancy Jobs ID
        """
        fl_job_consultancy = fl_job[fl_job[sub_industry] == "Consultancy"]
        fl_job_consultancy_jid = fl_job_consultancy["JID"].values
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_consultancy_jid)]
        """
        3. then count the number of different CLIENT NAMES related to each particular INDUSTRY (Domain) (Assignment tab)
        """
        fl_assignment_jid_grouped = fl_assignment_jid.groupby(sub_industry)["Client name"]
        """
        4. then sum up all the obtained results (from the different consultancy jobs) related to each INDUSTRY (Domain)
        """
        a_out = {k: len(set(v)) for k,v in fl_assignment_jid_grouped}
        """
        5. then the obtained result will be used for a LOOK UP using the EG2 (for consultancy)
        """
        result[eg_1_2] = a_out
        """
        B) If the input is not a Consultancy then:
        """
        fl_job_not_consultancy = fl_job[fl_job[sub_industry] != "Consultancy"]
        """
        2. count the number of different COMPANY NAMES (column in job tab) of each particular INDUSTRY (Domain)
        """
        fl_job_not_consultancy_grouped = fl_job_not_consultancy.groupby(sub_industry)["Company Name"]
        """
        3. then sum up all the obtained results (from the different jobs (non-consultancy jobs)) related to each INDUSTRY (Domain)
        """
        b_out = {k: len(set(v)) for k,v in fl_job_not_consultancy_grouped}
        result[eg_1_3] = b_out

        return result
