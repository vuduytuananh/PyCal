from PyCal.Memory.data_factory import DataFactory
from PyCal.Brain.function.if_abstract_formular import IFF
class IF_EG_2_8(IFF):
    def __init__(self, domainORsubdomain):
        super(IF_EG_2_8, self).__init__(domainORsubdomain)

    def getScore(self, fid):
        result = {}
        eg15 = "EG_2_8"
        fl_trainings = self.data_factory.getTab(self.data_type, "Trainings & Certificates", {"FID": [fid], "TNCID":[], self.domainORsubdomain:[]})
        """
        1. Check the FUNCTION (Domain) column in the Trainings & Certificates tab
        """
        fl_trainings_grouped = fl_trainings.groupby(self.domainORsubdomain)["TNCID"]
        """
        2. then in the Trainings & Certificates ID column, count the number of Training & Certificates related to the specific FUNCTION (Domain)
        """
        out = {k: len(set(v)) for k,v in fl_trainings_grouped}
        result[eg15] = out
        return result
