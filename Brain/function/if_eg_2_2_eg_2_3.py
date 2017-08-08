from PyCal.Memory.data_factory import DataFactory
from PyCal.Brain.function.if_abstract_formular import IFF
class IF_EG_2_2_EG_2_3(IFF):
    def __init__(self, domainORsubdomain):
        super(IF_EG_2_2_EG_2_3, self).__init__(domainORsubdomain)

    def getScore(self, fid):
        result = {}
        eg9 = "EG_2_2"
        eg10 = "EG_2_3"
        fl_job = self.data_factory.getTab(self.data_type, "Job", {"FID": [fid], "JID":[], "Company Name":[], self.domainORsubdomain:[]})
        fl_assignment = self.data_factory.getTab(self.data_type, "Assignment", {"FID": [fid], "JID": [], "Client name":[], self.domainORsubdomain:[]})

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
        """
        3. then count the number of different CLIENT NAMES related to each particular FUNCTION (Domain) (Assignment tab)
        4. then sum up all the obtained results (from the different consultancy jobs) related to each FUNCTION (Domain)
        """
        fdomain_empty_grouped = fdomain_empty_assignment.groupby(self.domainORsubdomain)["Client name"]
        a_out = {k: len(set(v)) for k, v in fdomain_empty_grouped}
        result[eg9] = a_out
        """
        B) If there is an input (its not a consultancy) then:
        """
        fdomain_not_empty = fl_job[fl_job[self.domainORsubdomain].notnull()]
        """
        2. count the number of different COMPANY NAMES (column in job tab) of each particular FUNCTION (Domain)
        3. then sum up all the obtained results (from the different jobs (non-consultancy jobs)) related to each FUNCTION (Domain)
        """
        fdomain_not_empty_grouped = fdomain_not_empty.groupby(self.domainORsubdomain)["Company Name"]
        b_out = {k: len(set(v)) for k, v in fdomain_not_empty_grouped}
        result[eg10] = b_out

        return result
