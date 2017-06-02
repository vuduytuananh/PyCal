from Vu.Memory.data_factory import DataFactory

class F50F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg32 = "EG32"
        result = {}
        fl_it = self.__data_factory.getTab(self.__data_type, "IT Application", {"FID": [fid], "Project Management Software": []})
        fl_it_pm = fl_it[fl_it["Project Management Software"] == "yes"]
        count = len(fl_it["Project Management Software"].values)
        result[eg32] = count
        return result

iff = F50F()
print(iff.getScore("FL-00001"))
