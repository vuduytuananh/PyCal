from Vu.Memory.data_factory import DataFactory

class F49F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid):
        eg31 = "EG31"
        result = {}
        fl_method = self.__data_factory.getTab(self.__data_type, "Method Assignment", {"FID": [fid], "Project Management Method": []})
        fl_method_pm = fl_method[fl_method["Project Management Method"] == "yes"]
        count = len(fl_method_pm["Project Management Method"].values)
        result[eg31] = count
        return result
iff = F49F()
print(iff.getScore("FL-00001"))
