from PyCal.Memory.data_factory import DataFactory
from PyCal.Brain.function.if_abstract_formular import IFF
class IF_EG_2_6(IFF):
    def __init__(self, domainORsubdomain):
        super(IF_EG_2_6, self).__init__(domainORsubdomain)

    def getScore(self, fid):
        result = {}
        eg13 = "EG_2_6"
        fl_conferences = self.data_factory.getTab(self.data_type, "Conferences Speakership", {"FID": [fid], "Conference Speakership ID":[], self.domainORsubdomain:[]})
        """
        1. Check the FUNCTION (Domain) column in the Conferences Speakership tab
        """
        fl_conferences_grouped = fl_conferences.groupby(self.domainORsubdomain)["Conference Speakership ID"]
        """
        2. then count  in the CONFERENCE SPEAKERSHIP ID column, the number of conference speakerships related to the specific FUNCTION (Domain)
        """
        out = {k: len(set(v)) for k,v in fl_conferences_grouped}
        result[eg13] = out
        return result
