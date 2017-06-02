from Vu.Memory.data_factory import DataFactory
from Vu.Brain.function.formulars.if_abstract_formular import IFF
import math
class IF17F(IFF):
    def __init__(self, domainORsubdomain):
        super(IF17F, self).__init__(domainORsubdomain)

    def getResult(self, fid):
        result = {}
        eg22 = "EG22"
        fl_job = self.data_factory.getTab(self.data_type, "Job", {"FID": [fid], "JID":[], "Company Size":[], "Duration JOB": [], self.domainORsubdomain:[]})
        fl_assignment = self.data_factory.getTab(self.data_type, "Assignment", {"FID": [fid], "JID": [], "Client Size":[], "Duration":[], self.domainORsubdomain:[]})

        #A2
        fdomain_empty = fl_job[fl_job[self.domainORsubdomain].isnull()]
        fdomain_empty_jids = fdomain_empty["JID"].values
        #A3
        fdomain_empty_assignment = fl_assignment[fl_assignment["JID"].isin(fdomain_empty_jids)][fl_assignment["Client Size"].isin(["over 50.000"])]
        fdomain_empty_grouped = fdomain_empty_assignment.groupby(self.domainORsubdomain)["Duration"]
        a_out = {k: math.fsum(list(v)) for k, v in fdomain_empty_grouped}
        result[eg22] = a_out

        #B2
        fdomain_not_empty = fl_job[fl_job[self.domainORsubdomain].notnull()][fl_job["Company Size"].isin(["over 50.000"])]
        fdomain_not_empty_grouped = fdomain_not_empty.groupby(self.domainORsubdomain)["Duration JOB"]
        b_out = {k: math.fsum(list(v)) for k,v in fdomain_not_empty_grouped}
        for i in b_out:
            if i in result[eg22]: result[eg22][i] += b_out[i]
            else: result[eg22][i] = b_out[i]
        return result
