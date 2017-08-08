from PyCal.Memory.data_factory import DataFactory

class IF_EG_1_6:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getScore(self, fid, sub_industry):
        eg_1_6 = "EG_1_6"
        result = {}
        """
        1. Check the INDUSTRY (Domain) column in the Trainings & Certificates tab
        """
        fl_tnc = self.__data_factory.getTab(self.__data_type, "Trainings & Certificates", {"FID": [fid], "TNCID":[], sub_industry: []})
        """
        2. then in the Trainings & Ceritficates ID column, count the number of Training & Certificates related to the specific INDUSTRY (Domain)
        """
        fl_tnc_grouped = fl_tnc.groupby(sub_industry)["TNCID"]
        result[eg_1_6] = {k: len(list(v)) for k,v in fl_tnc_grouped}
        return result
