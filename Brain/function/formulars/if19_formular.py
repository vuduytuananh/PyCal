from Vu.Memory.data_factory import DataFactory
from Vu.Brain.function.formulars.if_abstract_formular import IFF
class IF19F(IFF):
    def __init__(self, domainORsubdomain):
        super(IF19F, self).__init__(domainORsubdomain)

    def getResult(self, fid):
        result = {}
        eg28 = "EG28"
        fl_it_application = self.data_factory.getTab(self.data_type, "IT Application", {"FID": [fid], "IT Applications ID":[], self.domainORsubdomain:[]})
        fl_it_application_grouped = fl_it_application.groupby(self.domainORsubdomain)["IT Applications ID"]
        out = {k: len(set(v)) for k,v in fl_it_application_grouped}
        result[eg28] = out
        return result
