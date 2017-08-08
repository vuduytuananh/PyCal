import math
from PyCal.Memory.data_factory import DataFactory
class IF92:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        result = {}
        eg69 = "EG69"

        fl_method_assigment = self.__data_factory.getTab(self.__data_type, "Method Assignment", {"FID": [fid], "Assignment ID": [], "Method ID": []})
        """
        1. Check the METHOD ASSIGNMENT tab
        A) If there is an input in the METHOD ID column then:
        """
        fl_method_assigment_mid = fl_method_assigment[fl_method_assigment["Method ID"].notnull()]
        """
        2. count the number of ASSIGNMENT IDs related to each particular METHOD ID(Methods Assignment tab)
        """
        result[eg69] = len(fl_method_assigment_mid["Assignment ID"].values)
        """
        B) If there is no input then:
        2. count the number of ASSIGNMENT IDs as "0" or don't count them.
        At the end take the results and use the EG to obtain a score for each Method ID (related to a particular Freelancer ID)
        """
        return result
# class IF93:
#     def __init__(self):
#         self.__data_type = "DataTab"
#         self.__data_factory = DataFactory()
#
#     def getScore(self, fid):
#         result = {}
#         eg70 = "EG70"
#         fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "Industry/Sub-Domain":[]})
#         fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "Industry/Sub-Domain": []})
#         fl_job_method = self.__data_factory.getTab(self.__data_type, "Method Job", {"FID": [fid], "JID": [], "Method": []})
#         """
#         1. Check METHOD ID column in the METHOD JOB tab
#         A) If there is an input then
#         2. Check INDUSTRY (Sub-Domain) column in the JOB tab
#         AA) If there is no Input (its because its a consultancy) then:
#         """
#         fl_job_method_wm = fl_job_method[fl_job_method["Method ID"].notnull()]
#         fl_job_method_wm_grouped = fl_job_method_wm.groupby("JID")["Method"]
#         jid_method = {k:v for k,v in fl_job_method_wm_grouped}
#         """
#         3. go to assignment tab and work only with Assignments related to that specific Consultancy Jobs ID
#         """
#         fl_job_method_wm_jid = fl_job_method_wm["JID"].values
#         """
#         4. then take the INDUSTRY (Sub-Domain) related to that particular JOB ID (Assignment tab)
#         """
#         fl_job_jid = fl_job[fl_job["JID"].isin(fl_job_method_wm_jid)]
#         fl_job_jid_nosd = fl_job_jid[fl_job_jid["Sub-Domain"].isnull()]
#         fl_job_jid_nosd_jid = fl_job_jid_nosd["JID"].values
#         fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_jid_nosd_jid)]
#         """
#         5. then for each Method ID column(Method Job tab) take the associated JOB ID (Method Job tab) and therefore the associated ASSIGNMENT ID(Assignment tab) and therefore the associated INDUSTRY (Sub-Domain) (Assignment tab)
#         """
#         fl_assignment_jid["JID"] = fl_assignment_jid["JID"].map(i => jid_method[i])
#         fl_assignemnt_jid_grouped = fl_assignment_jid.groupby("JID")["Industry/Sub-Domain"]
#         aa_out = {k: set(v) for k,v in fl_assignment_jid_grouped}
#         """
#         AB) If there is input (its because its not a consultancy) then:
#         """
#         fl_job_jid_wsd = fl_job_jid[fl_job_jid["Sub-Domain"].notnull()]
#         """
#         3. take the INDUSTRY (Sub-Domain) (Job tab) related to that particular JOB ID (Job tab)
#         """
#         fl_job_jid_wsd["JID"] = fl_job_jid_wsd["JID"].map(i => jid_method[i])
#         """
#         4. then for each Method ID column(Method Job tab) take the associated JOB ID (Method Job tab) and therefore the associated INDUSTRY (Sub-Domain) (Job tab)
#         """
#         fl_job_jid_wsd_grouped = fl_job_jid_wsd.groupby("JID")["Industry/Sub-Domain"]
#         ab_out = {k: set(v) for k,v in fl_job_jid_wsd_grouped}
#
#         result[eg70] = {k: len(aa_out.get(k, set()) | ab_out.get(k, set())) for k in set(aa_out) | set(ab_out)}
#         """
#         B) If there is not input the
#         Count the number of different INDUSTRIES as "0" or don't count them.
#         ----
#         -At the end for each FREELANCER ID take all the INDUSTRY (Sub-Domain) obtained for each METHOD ID
#         -Count the number of different INDUSTRY (Sub-Domain) per METHOD ID
#         """
#         return result
#
# class IF94:
#     def __init__(self):
#         self.__data_type = "DataTab"
#         self.__data_factory = DataFactory()
#
#     def getScore(self, fid):
#         result = {}
#         eg71 = "EG71"
#         """
#         1. Check the METHODS column in the Trainings & Certificates tab
#         """
#         fl_tnc = self.__data_factory.getTab(self.__data_type, "Trainings & Certificates", {"FID": [fid], "TNCID": [], "Method": []})
#         """
#         2. then in the Trainings & Certificates ID column, count the number of Training & Certificates related to the specific METHOD
#         """
#         fl_tnc_grouped = fl_tnc.groupby("Method")["TNCID"]
#         result[eg71] = {k: len(list(v)) for k,v in fl_tnc_grouped}
#         return result
