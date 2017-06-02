from Vu.Memory.data_factory import DataFactory

class IF48F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg30 = "EG30"
        result = {}
        fl_training = self.__data_factory.getTab(self.__data_type, "Trainings & Certificates", {"FID": [fid], "TNCID": [], "Project Management": [], "Information": []})
        fl_training_query = fl_training[(fl_training["Project Management"] == "yes") & (fl_training["Information"] == "certificate")]
        result[eg30] = len(fl_training_query["TNCID"].values)
        return result

f =IF48F()
print(f.getScore("FL-00001"))
