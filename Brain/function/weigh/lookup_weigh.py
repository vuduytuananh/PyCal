from PyCal.Memory.data_factory import DataFactory
import pandas as pd
class LookupWeigh:
    def __init__(self):
        self.data_factory = DataFactory()
        self.data_type = "EG"

    def getScore(self, influencer):
        df_eg = self.data_factory.getTab(self.data_type, "Weigh-Function", {"IF": [], "Weigh": []})
        df_eg_filtered = df_eg[df_eg["IF"].isin([influencer])]
        weigh = df_eg_filtered["Weigh"].values[0]
        return weigh
