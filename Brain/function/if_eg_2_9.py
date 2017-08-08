from PyCal.Memory.data_factory import DataFactory
from PyCal.Brain.industry.merge import merge, count_lower_level, get_lower_industry_level
class IF_EG_2_9:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()
    def __cal_relative(self, sub_function, sub_function_value, number_lower_level):
        total = count_lower_level(sub_function, sub_function_value)
        if total == 0: return 1
        return number_lower_level/total
    def getScore(self, fid, sub_function):
        eg18 = "EG_2_9"
        result = {}
        #Find the lower level of the sub_function
        sub_industry_type = sub_function[len("Function/"):]
        sub_function_lower_level = get_lower_industry_level(sub_industry_type)
        sub_function_lower_level_name = "Function/"+sub_function_lower_level
        #get data
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], sub_function: [], "JID": [], sub_function_lower_level_name: []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid],"JID":[], sub_function: [], sub_function_lower_level_name: []})

        """
        1. For each JOB ID check the FUNCTION (Domain) column in the Job tab
        A) If there is no input (it means it is "Consultancy") then
        """
        fl_job_consultancy = fl_job[fl_job[sub_function] == "Consultancy"]

        """
        2. Go to the Assignment tab and check the FUNCTION (Domain) column
        """
        fl_job_consultancy_jid = fl_job_consultancy["JID"].values
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_consultancy_jid)]
        """
        3. Check and also take the input of FUNCTION (Sub-Domain) column (Assignment tab)
        """
        fl_assignment_jid_grouped = fl_assignment_jid.groupby(sub_function)[sub_function_lower_level_name]
        a_out = {k: set(v) for k,v in fl_assignment_jid_grouped}

        """
        B) If there is an input (it means it is not "Consultancy") then
        """
        fl_job_not_consultancy = fl_job[fl_job[sub_function] != "Consultancy"]

        """
        2. Check the input of the FUNCTION (Domain) column (Job tab)
        3. Check and also take the input of Function (Sub-domain) column (Job tab)
        """
        fl_job_not_consultancy_grouped = fl_job_not_consultancy.groupby(sub_function)[sub_function_lower_level_name]
        b_out = {k: set(v) for k,v in fl_job_not_consultancy_grouped}
        """
        - For each Freelancer ID count how many different FUNCTION (Sub-Domain) inputs there are for each FUNCTION (Domain)
        """
        merged = merge(a_out, b_out)
        """
        Compare the obtained number with the total FUNCTION (Sub-Domain) data:
        """
        result[eg18] = {k: self.__cal_relative(sub_industry_type, k, v) for k, v in merged.items()}
        return result
