import math
from PyCal.Brain.PFS.MonthsCountAbstract import MonthsCountAbstract
from PyCal.Brain.PFS.NumberAbstract import NumberAbstract
from PyCal.Brain.PFS.VarietyAbstract import VarietyAbstract
from PyCal.Brain.PFS.DurationAbstract import DurationAbstract
from PyCal.Memory.data_factory import DataFactory
class IF_5_1:
    def getScore(self, fid):
        eg_5_1 = "EG_5_1"
        duration = DurationAbstract()
        #Duration of assignments and jobs with E-activity
        result = duration.getScore(fid, "E-Activity", eg_5_1)
        return result
class IF_5_2:
    def getScore(self, fid):
        eg_5_2 = "EG_5_2"
        number = NumberAbstract()
        #N° of assignments and jobs with E-activity
        result = number.getScore(fid, "E-Activity", eg_5_2)
        return result
class IF_5_3:
    def getScore(self, fid):
        eg_5_3 = "EG_5_3"
        variety = VarietyAbstract()
        #Variety of companies from assignments and jobs with E-activity
        result = variety.getScore(fid, "E-Activity", "Company Name", "Client name", eg_5_3)
        return result
# NEW after 60
class IF_5_4:
    def getScore(self, fid):
        eg_5_4 = "EG_5_4"
        variety = VarietyAbstract()
        #Variety of industries with E-activity
        result = variety.getScore(fid, "E-Activity", "Industry/Domain", "Industry/Domain", eg_5_4)
        return result
class IF_5_5:
    def getScore(self, fid):
        eg_5_5 = "EG_5_5"
        variety = VarietyAbstract()
        #"Variety of functions from assignments and jobs with E-activity
        result = variety.getScore(fid, "E-Activity", "Function/Domain", "Function/Domain", eg_5_5)
        return result
class IF_5_6:
    def getScore(self, fid):
        eg_5_6 = "EG_5_6"
        duration = DurationAbstract()
        #Duration (time units) of assignments with M-Activities
        result = duration.getAssignmentDuration(fid, "M-Activity", eg_5_6)
        return result
class IF_5_7:
    def getScore(self, fid):
        eg_5_7 = "EG_5_7"
        number = NumberAbstract()
        #N° of Assignment with M-Activities
        result = number.getAssignmentNumber(fid, "M-Activity", eg_5_7)
        return result
class IF_5_8:
    def getScore(self, fid):
        eg_5_8 = "EG_5_8"
        variety = VarietyAbstract()
        #Variety of companies with M-Activities"
        result = variety.getAssignmentVariety(fid, "M-Activity", "Client name", eg_5_8)
        return result
class IF_5_9:
    def getScore(self, fid):
        eg_5_9 = "EG_5_9"
        variety = VarietyAbstract()
        #Variety of industries
        result = variety.getAssignmentVariety(fid, "M-Activity", "Industry/Domain", eg_5_9)
        return result
class IF_5_10:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg_5_10 = "EG_5_10"
        result = {}
        fl_tnc = self.__data_factory.getTab(self.__data_type, "Trainings & Certificates", {"FID":[fid], "Leadership Certificate":[], "Information": []})
        """
        1. Check the LEADERSHIP CERTIFICATE column in the Trainings & Certificates tab
        A) if the input is "YES"  then check the INFORMATION column
        AA) if the input is "CERTIFICATE" then
        2. take the TRAINING & CERTIFICATES ID
        """
        fl_tnc_query = fl_tnc[fl_tnc["Leadership Certificate"] == "YES"][fl_tnc["Information"] == "CERTIFICATE"]
        result[eg_5_10] = len(fl_tnc_query["Leadership Certificate"].values)
        """
        AB) if the input is not "CERTIFICATE" (Its a training) then don't take the TRAINING & CERTIFICATES ID or take it as "0"
        B) if the input is "NO" then don't take the TRAINING & CERTIFICATES ID or take it as "0"
        3. Count the number of TRAINING & CERTIFICATE IDs related to each FREELANCER ID
        """
        return result
class IF_5_11:
    def getScore(self, fid):
        eg_5_11 = "EG_5_11"
        # Duration (time units) with a specific project team size managed (Assignment)
        month_count = MonthsCountAbstract()
        result = month_count.getAssignmentScore(fid, "Team size", eg_5_11)
        return result
class IF_5_12:
    def getScore(self, fid):
        eg_5_12 = "EG_5_12"
        # Duration (time units) of M-Activities in Jobs
        duration = DurationAbstract()
        return duration.getJobDuration(fid, "M-Activity", eg_5_12)
class IF_5_13:
    def getScore(self, fid):
        eg_5_13 = "EG_5_13"
        number = NumberAbstract()
        # N° of Jobs with M-Activities
        return number.getJobNumber(fid, "M-Activity", eg_5_13)
class IF_5_14:
    def getScore(self, fid):
        eg_5_14 = "EG_5_14"
        variety = VarietyAbstract()
        # Variety of companies with M-Activities"
        return variety.getJobVariety(fid, "M-Activity", "Company Name", eg_5_14)
class IF_5_15:
    def getScore(self, fid):
        eg_5_15 = "EG_5_15"
        variety = VarietyAbstract()
        #Variety of industries
        result = variety.getJobVariety(fid, "M-Activity", "Industry/Domain", eg_5_15)
        return result
class IF_5_16:
    def getScore(self, fid):
        eg_5_16 = "EG_5_16"
        month_count = MonthsCountAbstract()
        # Duration (time units) of assignments with M-Activities
        result = month_count.getJobScore(fid, "Direct report", eg_5_16)
        return result
class IF_5_17:
    def getScore(self, fid):
        eg_5_17 = "EG_5_17"
        # Duration of jobs and assignments with A-activity
        duration = DurationAbstract()
        result = duration.getScore(fid, "A-Activity", eg_5_17)
        return result
class IF_5_18:
    def getScore(self, fid):
        eg_5_18 = "EG_5_18"
        # N° of jobs and assignments with A-activity
        number = NumberAbstract()
        result = number.getScore(fid, "A-Activity", eg_5_18)
        return result
class IF_5_19:
    def getScore(self, fid):
        eg_5_19 = "EG_5_19"
        # "Variety of functions with A-Activities
        variety = VarietyAbstract()
        result = variety.getScore(fid, "A-Activity", "Function/Domain", "Function/Domain", eg_5_19)
        return result
class IF_5_20:
    def getScore(self, fid):
        eg_5_20 = "EG_5_20"
        # Variety of industries with A-activity
        variety = VarietyAbstract()
        result = variety.getScore(fid, "A-Activity", "Industry/Domain", "Industry/Domain", eg_5_20)
        return result
class IF_5_21:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def __getTabScore(self, df):
        df = df[df["A-Activity Method"] == "yes"]
        return len(df["A-Activity Method"].values)
    # "N° of different methods tagged (combination of both: assignment and jobs)"
    def getScore(self, fid):
        eg_5_21 = "EG_5_21"
        result = {}
        fl_assignment_method = self.__data_factory.getTab(self.__data_type, "Method Job", {"FID": [fid], "A-Activity Method" : []})
        fl_job_method = self.__data_factory.getTab(self.__data_type, "Method Assignment", {"FID": [fid], "A-Activity Method" : []})
        """
        1. Check the A-ACTIVITY METHODS Column in the Method Assignment tab
        A) if the input is "yes" then take the METHOD ID
        B) if the input is "no" then don’t take the Method IDs or take it as "0"
        """
        assignment_method_out = self.__getTabScore(fl_assignment_method)
        """
        2. Check the A-ACTIVITY METHODS Column in the Method Job tab
        A) if the input is "yes" then take the METHOD ID
        B) if the input is "no" then don’t take the Method IDs or take it as "0"
        """
        job_method_out = self.__getTabScore(fl_job_method)
        result[eg_5_21] = assignment_method_out + job_method_out
        return result
#
# print(IF_5_1().getScore("FL-00001"))
# print(IF_5_2().getScore("FL-00001"))
# print(IF_5_3().getScore("FL-00001"))
# print(IF_5_4().getScore("FL-00001"))
# print(IF_5_5().getScore("FL-00001"))
# print(IF_5_6().getScore("FL-00001"))
# print(IF_5_7().getScore("FL-00001"))
# print(IF_5_8().getScore("FL-00001"))
# print(IF_5_9().getScore("FL-00001"))
# print(IF_5_10().getScore("FL-00001"))
# print(IF_5_11().getScore("FL-00001"))
# print(IF_5_12().getScore("FL-00001"))
# print(IF_5_13().getScore("FL-00001"))
# print(IF_5_14().getScore("FL-00001"))
# print(IF_5_15().getScore("FL-00001"))
# print(IF_5_16().getScore("FL-00001"))
# print(IF_5_17().getScore("FL-00001"))
# print(IF_5_18().getScore("FL-00001"))
# print(IF_5_19().getScore("FL-00001"))
# print(IF_5_20().getScore("FL-00001"))
# print(IF_5_21().getScore("FL-00001"))
