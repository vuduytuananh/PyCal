from PyCal.Memory.data_factory import DataFactory
from PyCal.Brain.function.eg.lookup import Lookup
import pandas as pd
class LookupStandard(Lookup):
    def __init__(self):
        super(LookupStandard, self).__init__()

    def getScore(self, egNo, f_result):
        result ={}
        df_eg = self.data_factory.getTab(self.data_type, "EG1D", {"EG":[egNo], "Lower": [], "Upper": [], "Score": []})
        for i in f_result:

            df_eg_fil_lower = df_eg[df_eg["Lower"] <= f_result[i]]

            df_eg_fil_upper = df_eg_fil_lower[(df_eg_fil_lower["Upper"] > f_result[i]) | (pd.isnull(df_eg_fil_lower["Upper"]))]
            print(df_eg_fil_upper)
            result[i] = df_eg_fil_upper["Score"].values[0]
        return result
class Lookup1D(Lookup):
    def __init__(self):
        super(Lookup1D, self).__init__()
    def getScore(self, egNo, f_result):
        df_eg = self.data_factory.getTab(self.data_type, "EG1D", {"EG":[egNo], "Lower": [], "Upper": [], "Score": []})
        df_eg_fil_lower = df_eg[df_eg["Lower"] <= f_result]

        df_eg_fil_upper = df_eg_fil_lower[(df_eg_fil_lower["Upper"] > f_result) | (pd.isnull(df_eg_fil_lower["Upper"]))]
        print(df_eg_fil_upper)
        if len(df_eg_fil_upper["Score"]) == 0: return 0
        return df_eg_fil_upper["Score"].values[0]
class Lookup2D(Lookup):
    def __init__(self):
        super(Lookup2D, self).__init__()

    def getScore(self, egNo, f_result):
        result = 0
        df_eg = self.data_factory.getTab(self.data_type, "EG2D", {"EG":[egNo], "LowerX": [], "UpperX": [],"LowerY": [], "UpperY": [], "Score": []})
        # empty
        if len(df_eg["Score"].values) == 0: return 0
        df_eg["LowerX"] = df_eg["LowerX"].astype(str)
        df_eg["UpperX"] = df_eg["UpperX"].astype(str)
        for i in f_result:
            df_eg_fil_X = df_eg[(df_eg["LowerX"] == i) & (df_eg["UpperX"] == i)]
            df_eg_fil_Y = df_eg_fil_X[(df_eg_fil_X["LowerY"] <= f_result[i]) & ((df_eg_fil_X["UpperY"] > f_result[i]) | pd.isnull(df_eg_fil_X["UpperY"]))]
            print(df_eg_fil_Y)
            if len(df_eg_fil_Y["Score"] > 0):
                result += df_eg_fil_Y["Score"].values[0]
        return result
