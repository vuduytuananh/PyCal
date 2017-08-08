from PyCal.Brain.industry.if_eg1 import IF_EG_1_1
from PyCal.Brain.industry.if_eg4 import IF_EG_1_4
from PyCal.Brain.industry.if_eg5 import IF_EG_1_5
from PyCal.Brain.industry.if_eg6 import IF_EG_1_6
from PyCal.Brain.industry.if_eg7 import IF_EG_1_7
from PyCal.Brain.industry.if_eg2_eg3 import IF_EG_1_2_EG_1_3
class IF_1_1:
    def __init__(self):
        self.__if = IF_EG_1_1()
    #Time period (time units) spent studying/working in an industry
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Domain")
class IF_1_2:
    def __init__(self):
        self.__if = IF_EG_1_2_EG_1_3()
    #Variety of companies regarding an industry in which the freelancer worked
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Domain")
class IF_1_3:
    def __init__(self):
        self.__if = IF_EG_1_4()
    #Variety of functions regarding an industry
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Domain")
class IF_1_4:
    def __init__(self):
        self.__if = IF_EG_1_5()
    #Number of memberships related to an industry
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Domain")
class IF_1_5:
    def __init__(self):
        self.__if = IF_EG_1_6()
    #Number of trainings & certificates regarding a specific industry
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Domain")
class IF_1_6:
    def __init__(self):
        self.__if = IF_EG_1_7()
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Domain")
class IF_1_7:
    def __init__(self):
        self.__if = IF_EG_1_1()
    #Sum of months related to each INDUSTRY (Sub-Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Sub-Domain")
class IF_1_8:
    def __init__(self):
        self.__if = IF_EG_1_2_EG_1_3()
    #Number of different Companies related to each INDUSTRY (Sub-Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Sub-Domain")
class IF_1_9:
    def __init__(self):
        self.__if = IF_EG_1_4()
    #Number of different Functions (Domain) related to each INDUSTRY (Sub-Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Sub-Domain")
class IF_1_10:
    def __init__(self):
        self.__if = IF_EG_1_5()
    #Number of memberships related to each INDUSTRY (Sub-Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Sub-Domain")
class IF_1_11:
    def __init__(self):
        self.__if = IF_EG_1_6()
    #Number of Trainings & Certificates related to each INDUSTRY (Sub-Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Sub-Domain")
class IF_1_12:
    def __init__(self):
        self.__if = IF_EG_1_7()
    #Number of INDUSTRY (Category) compared to the number of total INDUSTRY (Sub-Domains) regarding each INDUSTRY (Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Sub-Domain")
class IF_1_13:
    def __init__(self):
        self.__if = IF_EG_1_1()
    #Sum of months related to each INDUSTRY (Category)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Category")
class IF_1_14:
    def __init__(self):
        self.__if = IF_EG_1_2_EG_1_3()
    #Number of different Companies related to each INDUSTRY (Category)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Category")
class IF_1_15:
    def __init__(self):
        self.__if = IF_EG_1_4()
    #Number of different Functions (D) related to each INDUSTRY (Category)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Category")
class IF_1_16:
    def __init__(self):
        self.__if = IF_EG_1_5()
    #Number of memberships related to each INDUSTRY (Category)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Category")
class IF_1_17:
    def __init__(self):
        self.__if = IF_EG_1_6()
    #Number of Trainings & Certificates related to each INDUSTRY (Category)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Category")
class IF_1_18:
    def __init__(self):
        self.__if = IF_EG_1_7()
    #Number of INDUSTRY (Sub-Category) compared to the number of total INDUSTRY (Sub-Domains) regarding each INDUSTRY (Category)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Category")
class IF_1_19:
    def __init__(self):
        self.__if = IF_EG_1_1()
    #Sum of months related to each INDUSTRY (Sub-Category)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Category")
class IF_1_20:
    def __init__(self):
        self.__if = IF_EG_1_2_EG_1_3()
    #Number of different Companies related to each INDUSTRY (Sub-Category)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Category")
class IF_1_21:
    def __init__(self):
        self.__if = IF_EG_1_4()
    #Number of different Functions (D) related to each INDUSTRY (Sub-Category)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Category")
class IF_1_22:
    def __init__(self):
        self.__if = IF_EG_1_5()
    #Number of memberships related to each INDUSTRY (Sub-Category)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Category")
class IF_1_23:
    def __init__(self):
        self.__if = IF_EG_1_6()
    #Number of Trainings & Certificates related to each INDUSTRY (Sub-Category)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Industry/Category")

# if1 = IF_1_1()
# print(if1.getScore("FL-00001"))
# if2 = IF_1_2()
# print(if2.getScore("FL-00001"))
# if3 = IF_1_3()
# print(if3.getScore("FL-00001"))
# if4 = IF_1_4()
# print(if4.getScore("FL-00001"))
# if5 = IF_1_5()
# print(if5.getScore("FL-00001"))
# if6 = IF_1_6()
# print(if6.getScore("FL-00001"))
# if7 = IF_1_7()
# print(if7.getScore("FL-00001"))
# if8 = IF_1_8()
# print(if8.getScore("FL-00001"))
# if9 = IF_1_9()
# print(if9.getScore("FL-00001"))
# if21 = IF_1_21()
# print(if21.getScore("FL-00001"))
# if10 = IF_1_10()
# print(if10.getScore("FL-00001"))
# if11 = IF_1_11()
# print(if11.getScore("FL-00001"))
# if12 = IF_1_12()
# print(if12.getScore("FL-00001"))
# if13 = IF_1_13()
# print(if13.getScore("FL-00001"))
# if14 = IF_1_14()
# print(if14.getScore("FL-00001"))
# if15 = IF_1_15()
# print(if15.getScore("FL-00001"))
# if16 = IF_1_16()
# print(if16.getScore("FL-00001"))
# if17 = IF_1_17()
# print(if17.getScore("FL-00001"))
# if18 = IF_1_18()
# print(if18.getScore("FL-00001"))
# if17 = IF_1_17()
# print(if17.getScore("FL-00001"))
# if18 = IF_1_18()
# print(if18.getScore("FL-00001"))
# if19 = IF_1_19()
# print(if19.getScore("FL-00001"))
# if20 = IF_1_20()
# print(if20.getScore("FL-00001"))
# if22 = IF_1_22()
# print(if22.getScore("FL-00001"))
# if23 = IF_1_23()
# print(if23.getScore("FL-00001"))
