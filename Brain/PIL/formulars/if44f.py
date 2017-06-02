from Vu.Memory.data_factory import DataFactory

class F44F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg24= "EG24"
        result = {}

        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "Assignment ID": [], "Internal": [], "Management position":[]})
        fl_assignment_query = fl_assignment[(fl_assignment["Internal"] == "no") & (fl_assignment["Management position"] == "yes")]
        count = len(fl_assignment_query["Assignment ID"].values)
        result[eg24] = count
        return result

f = F44F()
print(f.getScore("FL-00001"))
