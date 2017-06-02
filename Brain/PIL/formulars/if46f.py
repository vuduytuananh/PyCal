from Vu.Memory.data_factory import DataFactory
import math
class IF46F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__reference = "ReferenceTab"
        self.__data_factory = DataFactory()
    def __lookupCompany(self, dictionary):
        ref_consultancy_list = self.__data_factory.getTab(self.__reference, "Consultancy List", {"Consultancy List": [], "Tier Level": []})
        temp = {}
        for c in dictionary:
            lookupVal = ref_consultancy_list[ref_consultancy_list["Consultancy List"] == c].values
            if len(lookupVal == 1):
                key = str(lookupVal[0])
            else:
                key = "0"
            temp[key] = dictionary[c]
        return temp
    def __lookupSize(self, dictionary):
        ref_company_size = self.__data_factory.getTab(self.__reference, "Company Size", {"Company Size": [], "Tier Level": []})
        temp = {}
        for c in dictionary:
            lookupVal = ref_company_size[ref_company_size["Company Size"] == c].values
            if len(lookupVal == 1):
                key = str(lookupVal[0])
            else:
                key = "0"
            temp[key] = dictionary[c]
        return temp
    def getScore(self, fid):
        result = {}
        eg26 = "EG26"

        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "Self Employed": [], "JID": [], "Company Name": [], "Duration JOB": [], "Industry/Domain": [], "Company Size": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "Intermediate Company": [], "JID": [], "Duration": [], "Client name": [], "Internal": []})


        #A
        fl_job_self_employed = fl_job[fl_job["Self Employed"] == "yes"]
        fl_job_self_employed_jid = fl_job_self_employed["JID"].values

        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_self_employed_jid)]
        #AA
        fl_assignment_company_name = fl_assignment_jid[fl_assignment_jid["Intermediate Company"].notnull()]
        fl_assignment_company_name_grouped = fl_assignment_company_name.groupby("Intermediate Company")["Duration"]
        company_for_duration = {k: math.fsum(list(v)) for k,v in fl_assignment_company_name_grouped}
        temp_one = self.__lookupCompany(company_for_duration)

        #AB
        fl_assignment_NOT_company_name = fl_assignment_jid[fl_assignment_jid["Intermediate Company"].isnull()]
        fl_assignment_NOT_company_name_group = fl_assignment_NOT_company_name.groupby("Client name")["Duration"]
        client_for_duration = {k: math.fsum(list(v)) for k, v in fl_assignment_NOT_company_name_group}
        temp_two = self.__lookupCompany(client_for_duration)

        #B
        fl_job_nse = fl_job[fl_job["Self Employed"] == "no"]
        fl_job_nse_not_consultancy = fl_job_nse[fl_job_nse["Industry/Domain"] != "Consultancy"]
        fl_job_nse_not_consultancy_jid = fl_job_nse_not_consultancy["JID"].values
        fl_assignment_not_consultancy_jid = fl_assignment[(fl_assignment["JID"].isin(fl_job_nse_not_consultancy_jid)) & ((fl_assignment["Internal"] == "yes") | (fl_assignment["Internal"].isnull()))]
        fl_assignment_jid_tb = fl_assignment_not_consultancy_jid["JID"].values
        fl_job_cs_duration = fl_job[fl_job["JID"].isin(fl_assignment_jid_tb)]
        fl_job_cs_duration_grouped = fl_job_cs_duration.groupby("Company Size")["Duration JOB"]
        cs_for_duration = {k : math.fsum(list(v)) for k,v in fl_job_cs_duration_grouped}
        temp_three = self.__lookupSize(cs_for_duration)

        fl_assignment_no_internal = fl_assignment[(fl_assignment["JID"].isin(fl_job_nse_not_consultancy_jid)) & (fl_assignment["Internal"] == "no")]
        temp_four = {"3": math.fsum(fl_assignment_no_internal["Duration"].values)}


        fl_job_nse_consultancy = fl_job_nse[fl_job_nse["Industry/Domain"] == "Consultancy"]
        fl_job_nse_consultancy_group = fl_job_nse_consultancy.groupby("Company Name")["Duration JOB"]
        cn_for_duration = {k: math.fsum(list(v)) for k,v in fl_job_nse_consultancy_group}
        temp_five = self.__lookupSize(cn_for_duration)

        result[eg26] = {k: temp_one.get(k,0) + temp_two.get(k,0) + temp_three.get(k,0) + temp_four.get(k,0) + temp_five.get(k,0) for k in set(temp_one) | set(temp_two) | set(temp_three) | set(temp_four) | set(temp_five)}

        return result

fff = IF46F()
print(fff.getScore("FL-00001"))
