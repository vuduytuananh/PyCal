from PyCal.Brain.function.if_eg_2_1 import IF_EG_2_1
from PyCal.Brain.function.if_eg_2_2_eg_2_3 import IF_EG_2_2_EG_2_3
from PyCal.Brain.function.if_eg_2_4 import IF_EG_2_4
from PyCal.Brain.function.if_eg_2_5 import IF_EG_2_5
from PyCal.Brain.function.if_eg_2_6 import IF_EG_2_6
from PyCal.Brain.function.if_eg_2_7 import IF_EG_2_7
from PyCal.Brain.function.if_eg_2_8 import IF_EG_2_8
from PyCal.Brain.function.if_eg_2_9 import IF_EG_2_9
class IF_2_1:
    def __init__(self):
        self.__if = IF_EG_2_1("Domain")
    #Sum of months related to each FUNCTION (Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_2:
    def __init__(self):
        self.__if = IF_EG_2_2_EG_2_3("Domain")
    #Number of different Companies related to each  FUNCTION (Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_3:
    def __init__(self):
        self.__if = IF_EG_2_4("Domain")
    #Number of different INDUSTRIES (Domain) related to each FUNCTION (Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_4:
    def __init__(self):
        self.__if = IF_EG_2_5("Domain")
    #Number of different publications related to each FUNCTION (Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_5:
    def __init__(self):
        self.__if = IF_EG_2_6("Domain")
    #Number of different conferences related to each FUNCTION (Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_6:
    def __init__(self):
        self.__if = IF_EG_2_7("Domain")
    #Number of different memberships related to each FUNCTION (Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_7:
    def __init__(self):
        self.__if = IF_EG_2_8("Domain")
    #Number of Trainings & Certificates related to each FUNCTION (Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_8:
    def __init__(self):
        self.__if = IF_EG_2_9()
    #Number of FUNCTION (Sub-Domains) compared to the number of total FUNCTION (Domains)
    def getScore(self, fid):
        return self.__if.getScore(fid, "Function/Domain")

class IF_2_9:
    def __init__(self):
        self.__if = IF_EG_2_1("Sub-Domain")
    #Sum of months related to each FUNCTION (Sub-Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_10:
    def __init__(self):
        self.__if = IF_EG_2_2_EG_2_3("Sub-Domain")
    #Number of different Companies related to each  FUNCTION (Sub-Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_11:
    def __init__(self):
        self.__if = IF_EG_2_4("Sub-Domain")
    #Number of different INDUSTRIES (Sub-Domain) related to each FUNCTION (Sub-Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_12:
    def __init__(self):
        self.__if = IF_EG_2_5("Sub-Domain")
    #Number of different publications related to each FUNCTION (Sub-Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_13:
    def __init__(self):
        self.__if = IF_EG_2_6("Sub-Domain")
    #Number of different conferences related to each FUNCTION (Sub-Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_14:
    def __init__(self):
        self.__if = IF_EG_2_7("Sub-Domain")
    #Number of different memberships related to each FUNCTION (Sub-Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)
class IF_2_15:
    def __init__(self):
        self.__if = IF_EG_2_8("Sub-Domain")
    #Number of Trainings & Certificates related to each FUNCTION (Sub-Domain)
    def getScore(self, fid):
        return self.__if.getScore(fid)

# print(IF_2_1().getScore("FL-00001"))
# print(IF_2_2().getScore("FL-00001"))
# print(IF_2_3().getScore("FL-00001"))
# print(IF_2_4().getScore("FL-00001"))
# print(IF_2_5().getScore("FL-00001"))
# print(IF_2_6().getScore("FL-00001"))
# print(IF_2_7().getScore("FL-00001"))
# print(IF_2_8().getScore("FL-00001"))
# print(IF_2_9().getScore("FL-00001"))
# print(IF_2_10().getScore("FL-00001"))
# print(IF_2_11().getScore("FL-00001"))
# print(IF_2_12().getScore("FL-00001"))
# print(IF_2_13().getScore("FL-00001"))
# print(IF_2_14().getScore("FL-00001"))
# print(IF_2_15().getScore("FL-00001"))
