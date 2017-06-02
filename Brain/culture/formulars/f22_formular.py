from Vu.Memory.data_factory import DataFactory
from Vu.Brain.culture.formulars.Language import LanguageLookup
import math
class F22F():
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg31 = "EG31"
        result = {}
        fl_education = self.__data_factory.getTab(self.__data_type, "Education", {"FID": [fid], "Location": [], "Duration": []})
        fl_personal = self.__data_factory.getTab(self.__data_type, "Personal", {"FID": [fid], "Nationality Location": []})
        nationality_location = fl_personal["Nationality Location"].values
        #ignore same nationality_location
        fl_education = fl_education[~fl_education["Location"].isin(nationality_location)]
        fl_education_grouped = fl_education.groupby("Location")["Duration"]
        result = {k: math.fsum(list(v)) for k, v in fl_education_grouped}
        result = LanguageLookup().lookup(fid, result)
        return {eg31: result}
#test
iff = F22F()
print(iff.getScore("FL-00001"))
