from PyCal.Memory.data_factory import DataFactory
from PyCal.Brain.function.if_abstract_formular import IFF
class IF_EG_2_5(IFF):
    def __init__(self, domainORsubdomain):
        super(IF_EG_2_5, self).__init__(domainORsubdomain)

    def getScore(self, fid):
        result = {}
        eg12 = "EG_2_5"
        fl_publications = self.data_factory.getTab(self.data_type, "Publications", {"FID": [fid], "Publication ID":[], self.domainORsubdomain:[]})
        """
        1. Check the FUNCTION (Domain) column in the Publications tab
        """
        fl_publications_grouped = fl_publications.groupby(self.domainORsubdomain)["Publication ID"]
        """
        2. then count  in the PUBLICATION ID column, the number of publications related to the specific FUNCTION (Domain)
        """
        out = {k: len(set(v)) for k,v in fl_publications_grouped}
        result[eg12] = out
        return result
