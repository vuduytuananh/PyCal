from PyCal.Memory.data_factory import DataFactory
from PyCal.Brain.industry.merge import merge, count_lower_level, get_lower_industry_level
class IF_EG_1_7:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()
    def __cal_relative(self, sub_industry, sub_industry_value, number_lower_level):
        total = count_lower_level(sub_industry, sub_industry_value)
        if total == 0: return 1
        return number_lower_level/total
    def getScore(self, fid, sub_industry):
        TOTAL_Industry_SUB_DOMAIN = 20
        eg_1_7 = "EG_1_7"
        result = {}
        #Find the lower level of the sub_industry
        sub_industry_type = sub_industry[len("Industry/"):]
        sub_industry_lower_level = get_lower_industry_level(sub_industry[len("Industry/"):])
        sub_industry_lower_level_name = "Industry/" + sub_industry_lower_level
        #get data
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], sub_industry: [], "JID": [], sub_industry_lower_level_name: []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid],"JID":[], sub_industry: [], sub_industry_lower_level_name: []})

        """
        1. For each JOB ID check the INDUSTRY (Domain) column in the Job tab
        A) If the input is "Consultancy" then
        """
        fl_job_consultancy = fl_job[fl_job[sub_industry] == "Consultancy"]

        """
        2. Go to the Assignment tab and check the INDUSTRY (Domain) column
        """
        fl_job_consultancy_jid = fl_job_consultancy["JID"].values
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_consultancy_jid)]
        """
        3. Check and also take the input of Industry (Sub-Domain) column (Assignment tab)
        """
        fl_assignment_jid_grouped = fl_assignment_jid.groupby(sub_industry)[sub_industry_lower_level_name]
        a_out = {k: set(v) for k,v in fl_assignment_jid_grouped}

        """
        B) If the input is not "Consultancy" then
        """
        fl_job_not_consultancy = fl_job[fl_job[sub_industry] != "Consultancy"]

        """
        2. Check the input of the INDUSTRY (Domain) column (Job tab)
        3. Check and also take the input of Industry (Sub-domain) column (Job tab)
        """
        fl_job_not_consultancy_grouped = fl_job_not_consultancy.groupby(sub_industry)[sub_industry_lower_level_name]
        b_out = {k: set(v) for k,v in fl_job_not_consultancy_grouped}

        merged = merge(a_out, b_out)
        result[eg_1_7] = {k: self.__cal_relative(sub_industry_type, k, v) for k, v in merged.items()}
        return result
