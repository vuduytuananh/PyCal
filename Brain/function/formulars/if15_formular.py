from Vu.Memory.data_factory import DataFactory
from Vu.Brain.function.formulars.if_abstract_formular import IFF
import numpy as np
class IF15F(IFF):
    def __init__(self, domainORsubdomain):
        super(IF15F, self).__init__(domainORsubdomain)

    def __convertEduType(self, type):
        if type == "Apprenticeship": return 1
        elif type == "Vocational Training": return 1
        elif type == "Bachelor": return 2
        elif type == "Master": return 3
        elif type == "MBA": return 4
        elif type == "PhD": return 5
        else: raise Exception("@vu -> Invalid Education Type")
    def getResult(self, fid):
        result = {}
        eg20 = "EG20"
        fl_educations = self.data_factory.getTab(self.data_type, "Education", {"FID": [fid], "Education Type":[], self.domainORsubdomain:[]})
        fl_educations["Education Type"] = fl_educations["Education Type"].apply(lambda x: self.__convertEduType(x))
        fl_educations_grouped = fl_educations.groupby(self.domainORsubdomain)["Education Type"]
        out = {k: np.amax(list(v)) for k,v in fl_educations_grouped}
        result[eg20] = out
        return result
