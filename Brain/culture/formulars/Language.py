from Vu.Memory.data_factory import DataFactory
class LanguageLookup:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def lookup(self, fid, data):
        fl_language = self.__data_factory.getTab(self.__data_type, "Language", {"FID":[fid], "Country": [], "Level": []})
        for i in data:
            level = fl_language[fl_language["Country"].isin([i])]["Level"].values
            if len(level) > 0: level = max(level)
            if level >= 3: data[i] *= 2
        return data
