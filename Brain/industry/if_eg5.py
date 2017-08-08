from PyCal.Memory.data_factory import DataFactory

class IF_EG_1_5:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()
    def getScore(self, fid, sub_industry):
        eg_1_5 = "EG_1_5"
        result = {}
        """
        1. Check the INDUSTRY (Domain) column in the Memberships tab
        """
        fl_membership = self.__data_factory.getTab(self.__data_type, "Memberships", {"FID": [], sub_industry: [], "Membership ID": []})
        fl_membership_grouped = fl_membership.groupby(sub_industry)["Membership ID"]
        """
        2. then count  in the MEMBERSHIP ID column, the number of memberships related to the specific INDUSTRY (Domain)
        """
        result[eg_1_5] = {k: len(list(v)) for k,v in fl_membership_grouped}
        return result
