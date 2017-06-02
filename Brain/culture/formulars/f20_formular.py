from Vu.Memory.data_factory import DataFactory
class IF20F:
    def __init__(self):
        self.__data_factory = DataFactory()
        self.__data_type = "DataTab"
    def getResult(self, fid):
        result = {}
        eg = None
        fl = self.__data_factory.getTab(self.__data_type, "Personal", {"FID": [fid], "Nationality Location": []})
        nationalities = fl["Nationality Location"].values
        result = {nationalities[0]: 100}
        return result
