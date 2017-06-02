import pandas as pd


class TableDataInterface:
    def get_df(self, tab_name, projection_equal):
        raise NotImplementedError("Cannot get data from Interface, get it from the DataClass instead")

    def filter(self, file_path, tab_name, projection_equal):
        df = pd.read_excel(file_path, sheetname = tab_name)
        keys = list(projection_equal.keys())
        df = df[keys]
        for k in projection_equal:
            if len(projection_equal[k]) != 0: df = df[df[k].isin(projection_equal[k])]
        return df
class EGTab(TableDataInterface):
    def __init__(self):
        super(EGTab, self).__init__()
        self.__file_path = r"/Users/cherryfish/Desktop/Test/sample_EG.xlsx"

    #implement
    def get_df(self, tab_name, projection_equal):
        return self.filter(self.__file_path, tab_name, projection_equal)

class DataTab(TableDataInterface):
    def __init__(self):
        super(DataTab, self).__init__()
        self.__file_path = r"/Users/cherryfish/Desktop/Test/17.27.04_RAW DATA.xlsx"

    #implement
    def get_df(self, tab_name, projection_equal):
        return self.filter(self.__file_path, tab_name, projection_equal)

class ReferenceTab(TableDataInterface):
    def __init__(self):
        super(ReferenceTab, self).__init__()
        self.__file_path = r"/Users/cherryfish/Desktop/Test/ReferenceTab.xlsx"

    #implement
    def get_df(self, tab_name, projection_equal):
        return self.filter(self.__file_path, tab_name, projection_equal)
