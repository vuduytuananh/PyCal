from PyCal.Memory.data_factory import DataFactory
from PyCal.Brain.function.if_abstract_formular import IFF
class IF_EG_2_7(IFF):
    def __init__(self, domainORsubdomain):
        super(IF_EG_2_7, self).__init__(domainORsubdomain)

    def getScore(self, fid):
        result = {}
        eg14 = "EG_2_7"
        fl_memberships = self.data_factory.getTab(self.data_type, "Memberships", {"FID": [fid], "Membership ID":[], self.domainORsubdomain:[]})
        """
        1. Check the FUNCTION (Domain) column in the Memberships tab
        """
        fl_memberships_grouped = fl_memberships.groupby(self.domainORsubdomain)["Membership ID"]
        """
        2. then count  in the MEMBERSHIP ID column, the number of memberships related to the specific FUNCTION (Domain)
        """
        out = {k: len(set(v)) for k,v in fl_memberships_grouped}
        result[eg14] = out
        return result
