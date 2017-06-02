from Vu.Memory.data_factory import DataFactory
from Vu.Brain.function.formulars.if_abstract_formular import IFF
class IF14F(IFF):
    def __init__(self, domainORsubdomain):
        super(IF14F, self).__init__(domainORsubdomain)

    def getResult(self, fid):
        result = {}
        eg19 = "EG19"
        fl_memberships = self.data_factory.getTab(self.data_type, "Memberships", {"FID": [fid], "Membership ID":[], self.domainORsubdomain:[]})
        fl_memberships_grouped = fl_memberships.groupby(self.domainORsubdomain)["Membership ID"]
        out = {k: len(set(v)) for k,v in fl_memberships_grouped}
        result[eg19] = out
        return result
