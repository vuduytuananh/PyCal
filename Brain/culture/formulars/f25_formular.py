from Vu.Memory.data_factory import DataFactory
from Vu.Brain.culture.formulars.Language import LanguageLookup
import math
class F25F():
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()
    def getScore(self, fid):
        eg34 = "EG34"
        result = {}

        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid]})
        #to be continued 
