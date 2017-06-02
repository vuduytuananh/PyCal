from Vu.Memory.data_factory import DataFactory
from Vu.Brain.function.eg.lookup import Lookup
import pandas as pd
class LookupStandard(Lookup):
    def __init__(self):
        super(LookupStandard, self).__init__()

    def getScore(self, egNo, f_result):
        result ={}
        df_eg = self.data_factory.getTab(self.data_type, "EG", {"EG":[egNo], "Lower": [], "Upper": [], "Score": []})
        for i in f_result:
            df_eg_fil_lower = df_eg[df_eg["Lower"] <= f_result[i]]
            df_eg_fil_upper = df_eg_fil_lower[(df_eg_fil_lower["Upper"] > f_result[i]) | (pd.isnull(df_eg_fil_lower["Upper"]))]
            result[i] = df_eg_fil_upper["Score"].values[0]
        return result
