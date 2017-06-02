from Vu.Memory.data_factory import DataFactory

class F43F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg23 = "EG23"
        result = {}

        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "Assignment ID": [], "Internal": [], "Management position":[]})
        fl_assignment_query = fl_assignment[(fl_assignment["Internal"] == "yes") & (fl_assignment["Management position"] == "no")]
        count = len(fl_assignment_query["Assignment ID"].values)
        result[eg23] = count
        return result

f = F43F()
print(f.getScore("FL-00001"))
