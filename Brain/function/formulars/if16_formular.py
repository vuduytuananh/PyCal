from Vu.Memory.data_factory import DataFactory
from Vu.Brain.function.formulars.if_abstract_formular import IFF
class IF16F(IFF):
    def __init__(self, domainORsubdomain):
        super(IF16F, self).__init__(domainORsubdomain)

    def getResult(self, fid):
        result = {}
        eg21 = "EG21"
        fl_trainings = self.data_factory.getTab(self.data_type, "Trainings & Certificates", {"FID": [fid], "TNCID":[], self.domainORsubdomain:[]})
        fl_trainings_grouped = fl_trainings.groupby(self.domainORsubdomain)["TNCID"]
        out = {k: len(set(v)) for k,v in fl_trainings_grouped}
        result[eg21] = out
        return result
