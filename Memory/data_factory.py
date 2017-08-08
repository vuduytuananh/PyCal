from PyCal.Memory.data import TableDataInterface, EGTab, DataTab, ReferenceTab
class DataFactory:
    def __init__(self):
        self.__product_map = dict(EG = EGTab(), DataTab = DataTab(), ReferenceTab = ReferenceTab())

    def getTab(self, name, tab_name, projection_equal):
        if name in self.__product_map:
            return self.__product_map[name].get_df(tab_name, projection_equal)
        else: raise Exception("@Vu --> Invalid data name (first arg)")
