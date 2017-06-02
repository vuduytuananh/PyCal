import math
from Vu.Memory.data_factory import DataFactory
from Vu.Brain.function.formulars.if_abstract_formular import IFF
class IF9F(IFF):
    def __init__(self, domainORsubdomain):
        super(IF9F, self).__init__(domainORsubdomain)

    def getResult(self, fid):
        result = {}
        eg13 = "EG13"
        fl_job = self.data_factory.getTab(self.data_type, "Job", {"FID": [fid], "JID":[], "Duration JOB":[], self.domainORsubdomain:[]})
        fl_assignment = self.data_factory.getTab(self.data_type, "Assignment", {"FID": [fid], "JID": [], "Duration":[], self.domainORsubdomain:[]})

        #A2
        #Job Tab
        fdomain_not_empty = fl_job[fl_job[self.domainORsubdomain].notnull()]
        fdomain_not_empty_grouped = fdomain_not_empty.groupby(self.domainORsubdomain)["Duration JOB"]
        fdomain_not_empty_out = {k: math.fsum(list(v)) for k,v in fdomain_not_empty_grouped}
        fdomain_not_empty_jids = fdomain_not_empty["JID"].values
        fdomain_not_empty_fdomains = fdomain_not_empty[self.domainORsubdomain].values
        jid_fdomain = dict(zip(fdomain_not_empty_jids, fdomain_not_empty_fdomains))

        #Assignment tab
        jid_diff_fdomain_duration = {}
        for i in jid_fdomain:
            df = fl_assignment[(fl_assignment["JID"] == i) & (fl_assignment[self.domainORsubdomain] != jid_fdomain[i])]
            total = math.fsum(df["Duration"].values)
            if i in jid_diff_fdomain_duration:
                jid_diff_fdomain_duration[i] += total
            else:
                jid_diff_fdomain_duration[i] = total

        for i in jid_diff_fdomain_duration:
            domain = jid_fdomain[i]
            fdomain_not_empty_out[domain] -= jid_diff_fdomain_duration[i]

        #A3
        df = fl_assignment[fl_assignment["JID"].isin(fdomain_not_empty_jids)][~fl_assignment[self.domainORsubdomain].isin(fdomain_not_empty_fdomains)]
        df_grouped = df.groupby(self.domainORsubdomain)["Duration"]
        #A4
        temp = {k: math.fsum(list(v)) for k,v in df_grouped}
        result[eg13] = {**fdomain_not_empty_out, **temp} #A OUT

        #B2
        fdomain_empty = fl_job[fl_job[self.domainORsubdomain].isnull()]
        fdomain_empty_jids = fdomain_empty["JID"].values

        fdomain_empty_assignment = fl_assignment[fl_assignment["JID"].isin(fdomain_empty_jids)]
        fdomain_empty_assignment_grouped = fdomain_empty_assignment.groupby(self.domainORsubdomain)["Duration"]
        b_out = {k: math.fsum(list(v)) for k,v in fdomain_empty_assignment_grouped} #B OUT
        for i in b_out:
            if i in result[eg13]: result[eg13][i] += b_out[i]
            else: result[eg13][i] = b_out[i]

        return result
