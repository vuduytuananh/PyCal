from Vu.Memory.data_factory import DataFactory

class F47F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg29 = "EG29"
        result = {}
        fl_training = self.__data_factory.getTab(self.__data_type, "Trainings & Certificates", {"FID": [fid], "TNCID": [], "Project Management": []})
        fl_training_query = fl_training[fl_training["Project Management"] == "yes"]
        result[eg29] = len(fl_training_query["TNCID"].values)
        return result

f = F47F()
print(f.getScore("FL-00001"))
