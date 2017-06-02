from Vu.Memory.data_factory import DataFactory
from Vu.Brain.function.formulars.if_abstract_formular import IFF
class IF12F(IFF):
    def __init__(self, domainORsubdomain):
        super(IF12F, self).__init__(domainORsubdomain)

    def getResult(self, fid):
        result = {}
        eg17 = "EG17"
        fl_publications = self.data_factory.getTab(self.data_type, "Publications", {"FID": [fid], "Publication ID":[], self.domainORsubdomain:[]})
        fl_publications_grouped = fl_publications.groupby(self.domainORsubdomain)["Publication ID"]
        out = {k: len(set(v)) for k,v in fl_publications_grouped}
        result[eg17] = out
        return result
