from Vu.Memory.data_factory import DataFactory

class F42F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg22 = "EG22"
        result = {}

        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "Assignment ID": [], "Internal": [], "Management position":[]})
        fl_assignment_query = fl_assignment[(fl_assignment["Internal"] == "yes") & (fl_assignment["Management position"] == "yes")]
        count = len(fl_assignment_query["Assignment ID"].values)
        result[eg22] = count
        return result

iff = F42F()
print(iff.getScore("FL-00001"))
