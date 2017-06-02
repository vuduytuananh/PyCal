from Vu.Memory.data_factory import DataFactory
from Vu.Brain.function.formulars.if_abstract_formular import IFF
class IF10F(IFF):
    def __init__(self, domainORsubdomain):
        super(IF10F, self).__init__(domainORsubdomain)

    def getResult(self, fid):
        result = {}
        eg14 = "EG14"
        eg15 = "EG15"
        fl_job = self.data_factory.getTab(self.data_type, "Job", {"FID": [fid], "JID":[], "Company name":[], self.domainORsubdomain:[]})
        fl_assignment = self.data_factory.getTab(self.data_type, "Assignment", {"FID": [fid], "JID": [], "Client name":[], self.domainORsubdomain:[]})

        #A2
        fdomain_empty = fl_job[fl_job[self.domainORsubdomain].isnull()]
        fdomain_empty_jids = fdomain_empty["JID"].values
        #A3
        fdomain_empty_assignment = fl_assignment[fl_assignment["JID"].isin(fdomain_empty_jids)]
        fdomain_empty_grouped = fdomain_empty_assignment.groupby(self.domainORsubdomain)["Client name"]
        #A4
        a_out = {k: len(set(v)) for k, v in fdomain_empty_grouped} #A OUT
        result[eg14] = a_out
        #B2
        fdomain_not_empty = fl_job[fl_job[self.domainORsubdomain].notnull()]
        fdomain_not_empty_grouped = fdomain_not_empty.groupby(self.domainORsubdomain)["Company name"]
        b_out = {k: len(set(v)) for k, v in fdomain_not_empty_grouped} #B OUT
        result[eg15] = b_out

        return result
