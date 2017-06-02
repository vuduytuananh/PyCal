from Vu.Memory.data_factory import DataFactory
from Vu.Brain.culture.formulars.Language import LanguageLookup
import math
class F24F():
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()
    def getScore(self, fid):
        eg33 = "EG33"
        result = {}

        fl_personal = self.__data_factory.getTab(self.__data_type, "Personal", {"FID": [fid], "Nationality Location": [], "Location Personal Reasons": [], "Duration For Location": []})
        nationality_location = fl_personal["Nationality Location"].values
        #ignore same nationality
        fl_personal = fl_personal[~fl_personal["Location Personal Reasons"].isin(nationality_location)]
        fl_personal_grouped = fl_personal.groupby("Location Personal Reasons")["Duration For Location"]
        result = {k: math.fsum(list(v)) for k,v in fl_personal_grouped}
        result = LanguageLookup().lookup(fid, result)
        return {eg33: result}
iff = F24F()
print(iff.getScore("FL-00001"))
