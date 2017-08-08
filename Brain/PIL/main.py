from PyCal.Memory.data_factory import DataFactory
import math
class IF_4_1:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()
    """
    STEP 2 (EXTERNAL PROJECT ASSIGNMENTS)
    For each ASSIGNMENT ID (Assignment tab) related to that specific FREELANCER ID:
    """
    def __step2(self, fid):
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "Assignment ID": [], "Internal": [], "Management position":[]})
        """
        1. Check the INTERNAL PROJECTS column (Assignment tab)
        A) if the input is "NO"
        2. then check the MANAGEMENT POSITION column (Assignment tab)
        AA) If the input is "yes" then count the number of ASSIGNMENT IDs
        AB) If the input is "no" then don't count the Assignment IDs or count them as "0"
        B) if the input is "YES" then don't count the Assignment IDs or count them as "0"
        """
        fl_assignment_query = fl_assignment[(fl_assignment["Internal"] == "no") & (fl_assignment["Management position"] == "yes")]
        """
        -Take the number of Assignments and multiply it by the factor  x1 (one)
        """
        count = len(fl_assignment_query["Assignment ID"].values) * 1
        return count

    """
    STEP 1 (INTERNAL PROJECT ASSIGNMENTS)
    For each ASSIGNMENT ID (Assignment tab) related to that specific FREELANCER ID:
    """
    def __step1(self, fid):
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "Assignment ID": [], "Internal": [], "Management position":[]})
        """
        1. Check the INTERNAL PROJECTS column (Assignment tab)
        A) if the input is "YES"
        2. then check the MANAGEMENT POSITION column (Assignment tab)
        AA) If the input is "yes" then count the number of ASSIGNMENT IDs
        AB) If the input is "no" then don't count the Assignment IDs or count them as "0"
        B) if the input is "NO" then don't count the Assignment IDs or count them as "0"
        """
        fl_assignment_query = fl_assignment[(fl_assignment["Internal"] == "yes") & (fl_assignment["Management position"] == "yes")]
        """
        -Take the number of Assignments and multiply it by the factor  x0.5 (cero point five)
        """
        count = len(fl_assignment_query["Assignment ID"].values) * 0.5
        return count

    """
    STEP 3 (TOTAL PROJECT ASSIGNMENTS)
    1. Sum up the obtained final results from step 1 and 2
    """
    def getScore(self, fid):
        eg_4_1 = "EG_4_1"
        step1 = self.__step1(fid)
        step2 = self.__step2(fid)
        return {eg_4_1: step1 + step2}

class IF_4_2:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()
    """
    STEP 2 (EXTERNAL PROJECT ASSIGNMENTS)
    For each ASSIGNMENT ID (Assignment tab) related to that specific FREELANCER ID:
    """
    def __step2(self, fid):
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "Assignment ID": [], "Internal": [], "Management position":[]})
        """
        1. Check the INTERNAL PROJECTS column (Assignment tab)
        A) if the input is "NO"
        2. then check the MANAGEMENT POSITION column (Assignment tab)
        AA) If the input is "no" then count the number of ASSIGNMENT IDs
        AB) If the input is "yes" then don't count the Assignment IDs or count them as "0"
        B) if the input is "NO" then don't count the Assignment IDs or count them as "0"
        """
        fl_assignment_query = fl_assignment[(fl_assignment["Internal"] == "no") & (fl_assignment["Management position"] == "no")]
        """
        -Take the number of Assignments and multiply it by the factor  x1 (one)
        """
        count = len(fl_assignment_query["Assignment ID"].values) * 1
        return count
    """
    STEP 1 (INTERNAL PROJECT ASSIGNMENTS)
    For each ASSIGNMENT ID (Assignment tab) related to that specific FREELANCER ID:
    """
    def __step1(self, fid):
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "Assignment ID": [], "Internal": [], "Management position":[]})
        """
        1. Check the INTERNAL PROJECTS column (Assignment tab)
        A) if the input is "YES"
        2. then check the MANAGEMENT POSITION column (Assignment tab)
        AA) If the input is "no" then count the number of ASSIGNMENT IDs
        AB) If the input is "yes" then don't count the Assignment IDs or count them as "0"
        B) if the input is "NO" then don't count the Assignment IDs or count them as "0"
        """
        fl_assignment_query = fl_assignment[(fl_assignment["Internal"] == "yes") & (fl_assignment["Management position"] == "no")]
        """
        -Take the number of Assignments and multiply it by the factor  x0.5 (cero point five)
        """
        count = len(fl_assignment_query["Assignment ID"].values) * 0.5
        return count

    """
    STEP 3 (TOTAL PROJECT ASSIGNMENTS)
    1. Sum up the obtained final results from step 1 and 2
    """
    def getScore(self, fid):
        eg_4_2 = "EG_4_2"
        step1 = self.__step1(fid)
        step2 = self.__step2(fid)
        return {eg_4_2: step1 + step2}

class IF_4_3:
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
        eg_4_3 = "EG_4_3"

        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "Self Employed": [], "JID": [], "Company Name": [], "Duration": [], "Full time project": [], "Industry/Domain": [], "Company Size": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "Intermediate Company": [], "JID": [], "Duration": [], "Full time project": [], "Client name": [], "Internal": []})


        """
        1. Check the Self-Employed column (Job tab)
        A) If the input is ""Yes"" then
        """
        fl_job_self_employed = fl_job[fl_job["Self Employed"] == "yes"]
        """
        2. Check the Intermediate Column (Assignment tab) for that same JOB ID
        AA) If there is an input (Company name) then
        """
        fl_job_self_employed_jid = fl_job_self_employed["JID"].values

        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_self_employed_jid)]
        """
        AA) If there is an input (Company name) then
        """
        fl_assignment_company_name = fl_assignment_jid[fl_assignment_jid["Intermediate Company"].notnull()]
        """
        3. Take the input and do a Look up with the CONSULTANCY LIST (Consultancy list_Company size FILE)  and obtain a value
        4. Take the DURATION (months) (Assignment tab) related to that specific JOB ID
        """
        fl_assignment_company_name_grouped = fl_assignment_company_name.groupby("Intermediate Company")["Duration"]
        company_for_duration = {k: math.fsum(list(v)) for k,v in fl_assignment_company_name_grouped}
        temp_one = self.__lookupCompany(company_for_duration)

        """
        AB) if there is no input in the Intermediate Company column then
        3. Go to the CLIENT NAME column (Assignment tab)
        """
        fl_assignment_NOT_company_name = fl_assignment_jid[fl_assignment_jid["Intermediate Company"].isnull()]
        """
        4. Take the input and do a Look up with the CONSULTANCY LIST (Consultancy list_Company size FILE) and obtain a value
        5. Take the DURATION (months) (Assignment tab) related to that specific JOB ID
        """
        fl_assignment_NOT_company_name_group = fl_assignment_NOT_company_name.groupby("Client name")["Duration"]
        client_for_duration = {k: math.fsum(list(v)) for k, v in fl_assignment_NOT_company_name_group}
        temp_two = self.__lookupCompany(client_for_duration)

        """
        B) If the input is ""No"" then
        2. Go to the INDUSTRY (Sub-Domain) column (Job tab)
        """
        fl_job_nse = fl_job[fl_job["Self Employed"] == "no"]
        """
        2. Go to the INDUSTRY (Sub-Domain) column (Job tab)
        AA) If the input is not a ""Consultancy"" then
        """
        fl_job_nse_not_consultancy = fl_job_nse[fl_job_nse["Industry/Domain"] != "Consultancy"]
        """
        Check the column "WAS THAT A FULL TIME PROJECT?" (Job tab)
        AAA) If the input is "No" then
        """
        fl_job_nse_not_consultancy_nftp = fl_job_nse_not_consultancy[fl_job_nse_not_consultancy["Full time project"] == "No"]
        fl_job_nse_not_consultancy_jid = fl_job_nse_not_consultancy_nftp["JID"].values
        """
        3. Check the INTERNAL PROJECTS column (Assignment tab) of the same JOB ID
        AAAA) If the input is ""Yes"" or there is no input then
        """
        fl_assignment_not_consultancy_jid = fl_assignment[(fl_assignment["JID"].isin(fl_job_nse_not_consultancy_jid)) & (fl_assignment["Internal"] == "yes")]
        fl_assignment_jid_tb = fl_assignment_not_consultancy_jid["JID"].values
        """
        4. Check the COMPANY SIZE column (Job tab)
        """
        fl_job_cs_duration = fl_job[fl_job["JID"].isin(fl_assignment_jid_tb)]
        """
        5. Take the input and do a Look up with the COMPANY SIZE (Consultancy list_Company size FILE)  and obtain a value
        6. Take DURATION (months) (Job tab) related to that specific JOB ID
        """
        fl_job_cs_duration_grouped = fl_job_cs_duration.groupby("Company Size")["Duration"]
        cs_for_duration = {k : math.fsum(list(v)) for k,v in fl_job_cs_duration_grouped}
        temp_three = self.__lookupSize(cs_for_duration)

        """
        AAAB) If the input is ""No"" (it means it's an external project) then
        4. Take as a value the lowest consultancy score (value 3)
        5. Take the DURATION (months) (Assignment tab) related to that specific JOB ID
        """
        fl_assignment_no_internal = fl_assignment[(fl_assignment["JID"].isin(fl_job_nse_not_consultancy_jid)) & (fl_assignment["Internal"] == "no")]
        temp_four = {"3": math.fsum(fl_assignment_no_internal["Duration"].values)}

        """
        AAB) If the input is "Yes" then:
        3. Take as a value the lowest consultancy score (value 3)
        4. Take the DURATION (months) (Assignment tab) related to that specific JOB ID
        """
        fl_job_nse_not_consultancy_ftp = fl_job_nse_not_consultancy[fl_job_nse_not_consultancy["Full time project"] == "Yes"]
        fl_job_nse_not_consultancy_ftp_jid = fl_job_nse_not_consultancy_ftp["JID"].values
        fl_assignment_ftp = fl_assignment[fl_assignment["JID"].isin(fl_job_nse_not_consultancy_ftp_jid)]
        temp_five = {"3": math.fsum(fl_assignment_ftp["Duration"].values)}
        """
        AB) If the input is a ""Consultancy""
        """
        fl_job_nse_consultancy = fl_job_nse[fl_job_nse["Industry/Domain"] == "Consultancy"]
        """
        3. Check the COMPANY NAME (Job tab)
        4. Take the input and do a Look up with the CONSULTANCY LIST (Consultancy list_Company size FILE) and obtain a value
        5. Take the DURATION (months) (Job tab) related to that specific JOB ID
        """
        fl_job_nse_consultancy_group = fl_job_nse_consultancy.groupby("Company Name")["Duration"]
        cn_for_duration = {k: math.fsum(list(v)) for k,v in fl_job_nse_consultancy_group}
        temp_six = self.__lookupSize(cn_for_duration)

        result[eg_4_3] = {k: temp_one.get(k,0) + temp_two.get(k,0) + temp_three.get(k,0) + temp_four.get(k,0) + temp_five.get(k,0) + temp_six.get(k,0) for k in set(temp_one) | set(temp_two) | set(temp_three) | set(temp_four) | set(temp_five) | set(temp_six)}

        return result


class IF_4_4:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg_4_4 = "EG_4_4"
        result = {}
        """
        1. Check the PROJECT MANAGEMENT column in the TRAINING & CERTIFICATES tab
        A) if the input is "YES " then count the TRAINING & CERTIFICATES ID
        B) if the input is "NO" then count the TRAINING & CERTIFICATES ID as "0"
        """
        fl_training = self.__data_factory.getTab(self.__data_type, "Trainings & Certificates", {"FID": [fid], "TNCID": [], "Project Management": []})
        fl_training_query = fl_training[fl_training["Project Management"] == "yes"]
        result[eg_4_4] = len(fl_training_query["TNCID"].values)
        return result

class IF_4_5:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg_4_5 = "EG_4_5"
        result = {}
        """
        1. Check the PROJECT MANAGEMENT column in the Trainings & Certificates tab
        A) if the input is "YES"  then check the INFORMATION column
        AA) if the input is "CERTIFICATE" than count the TRAINING & CERTIFICATES ID
        AB) if the input is "TRAINING" then count the TRAINING & CERTIFICATES ID as "0"
        B) if the input is "NO" then count the TRAINING & CERTIFICATES ID as "0"
        """
        fl_training = self.__data_factory.getTab(self.__data_type, "Trainings & Certificates", {"FID": [fid], "TNCID": [], "Project Management": [], "Information": []})
        fl_training_query = fl_training[(fl_training["Project Management"] == "yes") & (fl_training["Information"] == "certificate")]
        result[eg_4_5] = len(fl_training_query["TNCID"].values)
        return result

class IF_4_6:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg_4_6 = "EG_4_6"
        result = {}
        """
        For each FREELANCER ID:
        1. Check the PROJECT MANAGEMENT Methods column in the Method Assignment tab
        A) if the input is "yes"
        then count the METHOD ID
        B) if the input is "no" then don’t count the Method IDs or count them as "0"
        """
        fl_method = self.__data_factory.getTab(self.__data_type, "Method Assignment", {"FID": [fid], "Project Management Method": []})
        fl_method_pm = fl_method[fl_method["Project Management Method"] == "yes"]
        count = len(fl_method_pm["Project Management Method"].values)
        result[eg_4_6] = count
        return result

# class IF_4_50:
#     def __init__(self):
#         self.__data_type = "DataTab"
#         self.__data_factory = DataFactory()
#
#     def getScore(self, fid):
#         eg26 = "EG26"
#         result = {}
#         """
#         1. Check the PROJECT MANAGEMENT SOFTWARE column in the IT APPLICATIONS tab
#         A) if the input is "YES " then count the IT APPLICATION ID
#         B) if the input is "NO" then count the IT APPLICATION ID as "0"
#         """
#         fl_it = self.__data_factory.getTab(self.__data_type, "IT Application", {"FID": [fid], "Project Management Software": []})
#         fl_it_pm = fl_it[fl_it["Project Management Software"] == "yes"]
#         count = len(fl_it["Project Management Software"].values)
#         result[eg26] = count
#         return result

class IF_4_7:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg_4_7 = "EG_4_7"
        result = {}
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [], "Industry/Sub-Domain": [], "Company Size": [], "Duration": [], "Self Employed": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Interim Position": [], "Client Size": [], "Duration": []})
        """
        1. Check the Self-Employed column (Job tab)
        A) If the input is ""Yes"" then
        """
        fl_job_se = fl_job[fl_job["Self Employed"] == "yes"]
        fl_job_se_jid = fl_job_se["JID"].values
        """
        2. Check the INTERIM Column (Assignment tab) for that same JOB ID
        AA) If the input is "Yes" then
        """
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_se_jid)]
        fl_assignment_jid_ip = fl_assignment_jid[fl_assignment_jid["Interim Position"] == "yes"]
        """
        3. Check the CLIENT SIZE (Assignment tab) for that JOB ID
        4. Take the DURATION (months) (Assignment tab) related to that specific CLIENT SIZE  for that specific JOB ID
        """
        fl_assignment_grouped = fl_assignment_jid_ip.groupby("Client Size")["Duration"]
        assignment_out = {k: math.fsum(list(v)) for k, v in fl_assignment_grouped}
        """
        B) If the input is ""No"" then
        2. Go to the INDUSTRY (Sub-Domain) column (Job tab)
        """
        fl_job_nse = fl_job[(fl_job["Self Employed"] == "no") & (fl_job["Industry/Sub-Domain"] != "Consultancy")]
        """
        AA) If the input is not a ""Consultancy"" then
        3. Check the COMPANY SIZE column (Job tab)
        4. Take DURATION (months) (Job tab) related to that specific COMPANY SIZE for that specific JOB ID
        AB) If the input is a ""Consultancy"" then
        3.  Count the DURATION as 0 or don't count it
        """
        fl_job_grouped = fl_job_nse.groupby("Company Size")["Duration"]
        job_out = {k: math.fsum(list(v)) for k, v in fl_job_grouped}

        result[eg_4_7] = { k: assignment_out.get(k, 0) + job_out.get(k, 0) for k in set(assignment_out) | set(job_out) }
        return result

class IF_4_8:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        result = {}
        eg_4_8 = "EG_4_8"
        names = set()
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [],"Industry/Sub-Domain": [], "Company Name": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Client name": [], "Interim Position": []})
        """
        1. Check INDUSTRY (Sub-Domain) column in the job tab
        A) If the Input is Consultancy then:
        2. then go to assignment tab and work only with Assignments related to that specific Consultancy Jobs ID
        """
        fl_job_ID = fl_job[fl_job["Industry/Sub-Domain"] == "Consultancy"]
        fl_job_ID_jid = fl_job_ID["JID"].values
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_ID_jid)]
        """
        3. then go to the INTERIM column
        AA) If the input is "yes" then take the CLIENT NAME
        AB) If the input is "no" then don't take the CLIENT NAMEs
        """
        fl_assignment_jid_clients = fl_assignment_jid["Client name"].values
        names.update(fl_assignment_jid_clients)

        """
        B) If the input is not a "Consultancy" then take the COMPANY NAMES ( job tab)
        ----
        4. Count the number of different CLIENTS NAMES
        BE CAREFUL AND DON'T COUNT THE SAME CLIENT TWICE
        """
        fl_job_not_consultancy = fl_job[fl_job["Industry/Sub-Domain"] != "Consultancy"]
        fl_job_not_consultancy_cn = fl_job_not_consultancy["Company Name"].values
        names.update(fl_job_not_consultancy_cn)

        result[eg_4_8] = len(names)
        return result

class IF_4_9:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        result = {}
        eg_4_9 = "EG_4_9"
        domains = set()
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [],"Industry/Sub-Domain": [], "Function/Domain": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Function/Domain":[], "Interim Position":[]})
        """
        1. Check INDUSTRY (Sub-Domain) column in the job tab
        A) If the Input is "Consultancy" then:
        """
        fl_job_consultancy = fl_job[fl_job["Industry/Sub-Domain"] == "Consultancy"]
        fl_job_consultancy_jid = fl_job_consultancy["JID"].values
        """
        2. then go to assignment tab and work only with Assignments related to that specific Consultancy Jobs ID
        """
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_consultancy_jid)]
        """
        3. then go to the INTERIM column
        AA) If the input is "yes" then take the FUNCTIONS (Domain) relater to the specific Consultancy JOB ID (Assignment tab)
        AB) if the input is "no" then don't take the FUNCTIONS or count them as "0"
        """
        fl_assignment_ip = fl_assignment_jid[fl_assignment_jid["Interim Position"] == "yes"]
        domains.update(fl_assignment_ip["Function/Domain"].values)
        """
        B) If the Input is not "Consultancy"
        3. then take the FUNCTION (Domain) (job tab) relater to the specific Non- Consultancy JOB ID (Job tab)
        """
        fl_job_not_consultancy = fl_job[fl_job["Industry/Sub-Domain"] != "Consultancy"]
        fl_job_not_consultancy_fd = fl_job_not_consultancy["Function/Domain"].values
        """
        4. Count the number of different FUNCTIONs (Domain) related to each FREELANCER ID
        BE CAREFUL AND DON'T COUNT THE SAME FUNCTION TWICE (IF APPEAR THE SAME FUNCTION in non-Consultancy Job and Consultancy Job, count them only ONCE)
        """
        domains.update(fl_job_not_consultancy_fd)

        result[eg_4_9] = len(domains)
        return result

class IF_4_10:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        result = {}
        eg_4_10 = "EG_4_10"
        domains = set()
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [],"Industry/Sub-Domain": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Industry/Sub-Domain":[], "Interim Position":[]})
        """
        1. Check INDUSTRY (Sub-Domain) column in the job tab
        A) If the Input is "Consultancy" then:
        """
        fl_job_consultancy = fl_job[fl_job["Industry/Sub-Domain"] == "Consultancy"]
        fl_job_consultancy_jid = fl_job_consultancy["JID"].values
        """
        2. then go to assignment tab and work only with Assignments related to that specific Consultancy Jobs ID
        """
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_consultancy_jid)]
        """
        3. then go to the INTERIM column
        AA) If the input is "yes" then take the INDUSTRY (Sub-Domain) relater to the specific Consultancy JOB ID (Assignment tab)
        AB) if the input is "no" then don't take the INDUSTRY (Sub-Domain) or take it as "0"
        """
        fl_assignment_ip = fl_assignment_jid[fl_assignment_jid["Interim Position"] == "yes"]
        idomains = fl_assignment_ip["Industry/Sub-Domain"].values
        domains.update(idomains)

        """
        B) If the Input is not "Consultancy"
        3. Take the INDUSTRY (Sub-Domain) (Job tab) regarding the specific Non-Consultancy Job ID
        4. Count the number of different INDUSTRY (Sub-Domain) related to each FREELANCER ID
        BE CAREFUL AND DON'T COUNT THE SAME INDUSTRY TWICE (IF APPEAR THE SAME INDUSTRY in non-Consultancy Job and Consultancy Job, count them only ONCE)
        """
        fl_job_not_consultancy = fl_job[fl_job["Industry/Sub-Domain"] != "Consultancy"]
        fl_job_not_consultancy_id = fl_job_not_consultancy["Industry/Sub-Domain"].values
        domains.update(fl_job_not_consultancy_id)

        result[eg_4_10] = len(domains)
        return result

class IF_4_11:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        result = {}
        eg_4_11 = "EG_4_11"
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [],"Industry/Sub-Domain": [], "Management Position": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Assignment ID":[], "Industry/Sub-Domain":[], "Interim Position":[]})
        """
        1. Check the INDUSTRY (Sub-Domain) column (Job tab)
        A) If the input is not a "Consultancy" then
        2. Check the MANAGEMENT POSITION column (Job tab)
        AA) If the Input is "yes" then take the JOB ID
        AB) If the input is "no" then don't take the Job ID or take it as "0"
        """
        fl_job_not_consultancy_mp = fl_job[(fl_job["Industry/Sub-Domain"] != "Consultancy") & (fl_job["Management Position"] == "yes")]
        jids = fl_job_not_consultancy_mp["JID"].values
        result[eg_4_11] = len(jids)

        """
        B) if the input is "Consultancy" then go to the Assignment tab and work with that specific consultancy JOB ID
        """
        fl_job_consultancy = fl_job[fl_job["Industry/Sub-Domain"] == "Consultancy"]
        fl_job_consultancy_jid = fl_job_consultancy["JID"].values
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_consultancy_jid)]
        """
        2. Check the INTERIM column (Assignment tab)
        AA) If the Input is "Yes" then take the Assignment ID
        AB) If the input is "No" then don't take the Assignment ID or take it as "0"
        """
        fl_assignment_ip = fl_assignment_jid[fl_assignment_jid["Interim Position"] == "yes"]
        fl_assignment_ip_aid = fl_assignment_ip["Assignment ID"].values
        """
        3.Count the number of JOB IDs + ASSIGNMENT IDs related to each FREELANCER ID
        """
        result[eg_4_11] += len(fl_assignment_ip_aid)

        return result

# print(IF_4_1().getScore("FL-00001"))
# print(IF_4_2().getScore("FL-00001"))
# print(IF_4_3().getScore("FL-00001"))
# print(IF_4_4().getScore("FL-00001"))
# print(IF_4_5().getScore("FL-00001"))
# print(IF_4_6().getScore("FL-00001"))
# print(IF_4_7().getScore("FL-00001"))
# print(IF_4_8().getScore("FL-00001"))
# print(IF_4_9().getScore("FL-00001"))
# print(IF_4_10().getScore("FL-00001"))
# print(IF_4_11().getScore("FL-00001"))
