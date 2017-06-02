from Vu.Memory.data_factory import DataFactory

class IFF:
    def __init__(self, domainORsubdomain):
        self.data_factory = DataFactory()
        self.data_type = "DataTab"
        if domainORsubdomain == "Domain": self.domainORsubdomain = "Function/Domain"
        elif domainORsubdomain == "Sub-Domain": self.domainORsubdomain = "Function/Sub-Domain"
        else: raise Exception("@Vu --> the second arg must be either 'Domain' or 'Sub-Domain'")

    def getResult(self, fid):
        raise NotImplementedException("@Vu --> Need to implement the function or use the implemented class!!!!!")
