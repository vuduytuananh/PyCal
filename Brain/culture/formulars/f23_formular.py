from Vu.Memory.data_factory import DataFactory
from Vu.Brain.culture.formulars.Language import LanguageLookup
import math
class F23F():
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg32 = "EG32"
        result = {}
        fl_training = self.__data_factory.getTab(self.__data_type, "Trainings & Certificates", {"FID": [], "Location": [], "Duration": []})
        fl_personal = self.__data_factory.getTab(self.__data_type, "Personal", {"FID": [fid], "Nationality Location": []})
        nationality_location = fl_personal["Nationality Location"].values
        fl_training = fl_training[~fl_training["Location"].isin(nationality_location)]
        fl_training_grouped = fl_training.groupby("Location")["Duration"]
        result = {k: math.fsum(list(v)) for k,v in fl_training_grouped}
        result = LanguageLookup().lookup(fid, result)
        return {eg32: result}

iff = F23F()
print(iff.getScore("FL-00001"))
