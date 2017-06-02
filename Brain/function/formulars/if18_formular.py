from Vu.Memory.data_factory import DataFactory
from Vu.Brain.function.formulars.if_abstract_formular import IFF
class IF18F(IFF):
    def __init__(self, domainORsubdomain):
        super(IF18F, self).__init__(domainORsubdomain)

    def getResult(self, fid):
        result = {}
        eg27 = "EG27"
        fl_norm_and_standard = self.data_factory.getTab(self.data_type, "Norm & Standards", {"FID": [fid], "Norms and Standards ID":[], self.domainORsubdomain:[]})
        fl_norm_and_standard_grouped = fl_norm_and_standard.groupby(self.domainORsubdomain)["Norms and Standards ID"]
        out = {k: len(set(v)) for k,v in fl_norm_and_standard_grouped}
        result[eg27] = out
        return result
