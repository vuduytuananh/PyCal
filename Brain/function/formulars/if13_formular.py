from Vu.Memory.data_factory import DataFactory
from Vu.Brain.function.formulars.if_abstract_formular import IFF
class IF13F(IFF):
    def __init__(self, domainORsubdomain):
        super(IF13F, self).__init__(domainORsubdomain)

    def getResult(self, fid):
        result = {}
        eg18 = "EG18"
        fl_conferences = self.data_factory.getTab(self.data_type, "Conference-Speakerships", {"FID": [fid], "Conference Speakership ID":[], self.domainORsubdomain:[]})
        fl_conferences_grouped = fl_conferences.groupby(self.domainORsubdomain)["Conference Speakership ID"]
        out = {k: len(set(v)) for k,v in fl_conferences_grouped}
        result[eg18] = out
        return result
