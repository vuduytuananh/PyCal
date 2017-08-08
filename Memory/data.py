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
# EG file data
class EGTab(TableDataInterface):
    def __init__(self):
        super(EGTab, self).__init__()
        self.__file_path = r"/home/vubuntu/Vu/Test/sample_EG.xlsx"

    #implement
    def get_df(self, tab_name, projection_equal):
        return self.filter(self.__file_path, tab_name, projection_equal)
#Freelancer data file
class DataTab(TableDataInterface):
    def __init__(self):
        super(DataTab, self).__init__()
        self.__file_path = r"/home/vubuntu/Vu/Test/17.27.04_RAW DATA.xlsx"

    #implement
    def get_df(self, tab_name, projection_equal):
        return self.filter(self.__file_path, tab_name, projection_equal)

#Reference Data file
class ReferenceTab(TableDataInterface):
    def __init__(self):
        super(ReferenceTab, self).__init__()
        self.__file_path = r"/home/vubuntu/Vu/Test/ReferenceTab.xlsx"

    #implement
    def get_df(self, tab_name, projection_equal):
        return self.filter(self.__file_path, tab_name, projection_equal)


#test
