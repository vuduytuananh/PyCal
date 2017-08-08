from PyCal.Memory.data_factory import DataFactory
from PyCal.Brain.function.if_abstract_formular import IFF
class IF_EG_2_4(IFF):
    def __init__(self, domainORsubdomain):
        super(IF_EG_2_4, self).__init__(domainORsubdomain)

    def getScore(self, fid):
        result = {}
        eg_2_4 = "EG_2_4"
        fl_job = self.data_factory.getTab(self.data_type, "Job", {"FID": [fid], "JID":[], "Industry/Domain":[], self.domainORsubdomain:[]})
        fl_assignment = self.data_factory.getTab(self.data_type, "Assignment", {"FID": [fid], "JID": [], "Industry/Domain":[], self.domainORsubdomain:[]})

        """
        1. Check FUNCTION (Domain) column in the job tab
        A) If there is no Input (its because its a consultancy) then:
        """
        fdomain_empty = fl_job[fl_job[self.domainORsubdomain].isnull()]
        fdomain_empty_jids = fdomain_empty["JID"].values
        """
        2. go to assignment tab and work only with Assignments related to that specific Consultancy Jobs ID
        """
        fdomain_empty_assignment = fl_assignment[fl_assignment["JID"].isin(fdomain_empty_jids)]
        fdomain_empty_grouped = fdomain_empty_assignment.groupby(self.domainORsubdomain)["Industry/Domain"]
        """
        3. then count the number of different INDUSTRIES (Domain)  related to each particular FUNCTION (Domain) (Assignment tab)
        """
        a_out = {k: len(set(v)) for k, v in fdomain_empty_grouped} #A OUT
        result[eg_2_4] = a_out
        """
        B) If there is an input (its because its not a consultancy) then:
        """
        fdomain_not_empty = fl_job[fl_job[self.domainORsubdomain].notnull()]
        """
        2. count the number of different INDUSTRIES (Domain) (column in job tab) of each particular FUNCTION (Domain)
        """
        fdomain_not_empty_grouped = fdomain_not_empty.groupby(self.domainORsubdomain)["Industry/Domain"]
        b_out = {k: len(set(v)) for k, v in fdomain_not_empty_grouped} #B OUT
        """
        At the end for each Freelancer ID sum all the different INDUSTRIES (Domain) related to each FUNCTION (Domain) and use the EG to obtain a score
        """
        for i in b_out:
            if i in result[eg_2_4]: result[eg_2_4][i] += b_out[i]
            else: result[eg_2_4][i] = b_out[i]
        return result
