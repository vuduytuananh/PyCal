import math
from PyCal.Memory.data_factory import DataFactory
from PyCal.Brain.function.if_abstract_formular import IFF
class IF_EG_2_1(IFF):
    def __init__(self, subFunction):
        super(IF_EG_2_1, self).__init__(subFunction)
    """
    STEP 1 (WORK DURATION)
    """
    def __step1(self, fid):
        result = {}
        fl_job = self.data_factory.getTab(self.data_type, "Job", {"FID": [fid], "JID":[], "Duration":[], self.domainORsubdomain:[]})
        fl_assignment = self.data_factory.getTab(self.data_type, "Assignment", {"FID": [fid], "JID": [], "Duration":[], self.domainORsubdomain:[]})

        """
        For each JOB ID related to the FREELANCER ID:
        1. Check FUNCTION (Domain) column in the job tab
        A) If there is an input there (it means its not a consultancy) then:
        """
        fdomain_not_empty = fl_job[fl_job[self.domainORsubdomain].notnull()]
        """
        2. Use the next formula to calculate the duration (months):
        DURATION (months) related to the specific FUNCTION obtained from Job tab
        """
        fdomain_not_empty_grouped = fdomain_not_empty.groupby(self.domainORsubdomain)["Duration"]
        fdomain_not_empty_out = {k: math.fsum(list(v)) for k,v in fdomain_not_empty_grouped}
        fdomain_not_empty_jids = fdomain_not_empty["JID"].values

        fdomain_not_empty_fdomains = fdomain_not_empty[self.domainORsubdomain].values
        jid_fdomain = dict(zip(fdomain_not_empty_jids, fdomain_not_empty_fdomains))

        """
        -(minus)- the sum of DURATIONS (months) related to the ASSIGNMENTS of the same Job ID which have FUNCTIONS (Domain) (assignment tab) different from the FUNCTION (Domain) in the job tab.
        """
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

        """
        3. then go to assignment tab and work only with Assignments related to that specific Job ID
        """
        df = fl_assignment[fl_assignment["JID"].isin(fdomain_not_empty_jids)][~fl_assignment[self.domainORsubdomain].isin(fdomain_not_empty_fdomains)]
        df_grouped = df.groupby(self.domainORsubdomain)["Duration"]
        """
        4. then sum up only the DURATION (months) related to each particular FUNCTION (Domain) (Assignment tab) which is different from FUNCTION (Domain) (Job tab)
        """
        temp = {k: math.fsum(list(v)) for k,v in df_grouped}
        a_out = {**fdomain_not_empty_out, **temp} #A OUT

        """
        B) If there is no input (its because its a Consultancy) then:
        2. go to assignment tab and work only with Assignments related to that specific (consultancy) Job ID
        """
        fdomain_empty = fl_job[fl_job[self.domainORsubdomain].isnull()]
        fdomain_empty_jids = fdomain_empty["JID"].values
        fdomain_empty_assignment = fl_assignment[fl_assignment["JID"].isin(fdomain_empty_jids)]

        """
        3. then sum up the DURATION (months) related to each particular FUNCTION (Domain) (Assignment tab)
        """
        fdomain_empty_assignment_grouped = fdomain_empty_assignment.groupby(self.domainORsubdomain)["Duration"]
        b_out = {k: math.fsum(list(v)) for k,v in fdomain_empty_assignment_grouped} #B OUT
        result = a_out
        for i in b_out:
            if i in result: result[i] += b_out[i]
            else: result[i] = b_out[i]

        return result

    """
    STEP 2: (EDUCATION DURATION)
    """
    def __step2(self, fid):
        result = {}
        """
        1. Check the FUNCTION (Domain) column in the Education tab
        """
        fl_edu = self.data_factory.getTab(self.data_type, "Education", {"FID": [fid], "Duration":[], self.domainORsubdomain:[]})

        """
        2. Take the DURATION (months) related to that specific FUNCTION (Domain)
        """
        fl_edu_grouped = fl_edu.groupby(self.domainORsubdomain)["Duration"]
        """
        3. Sum up all the DURATIONS(months) related to each FUNCTION (Domain) and multiply them by the factor x 0.5 (cero point five)
        """
        result = {k: math.fsum(list(v)) for k,v in fl_edu_grouped}
        return result

    """
    STEP 3 (SUM and obtain TOTAL DURATION)
    1. Sum up all the DURATIONS related to each FUNCTION (Domain) obtained from step 1 and 2
    """
    def getScore(self, fid):
        result = {}
        eg_2_1 = "EG_2_1"
        step1 = self.__step1(fid)
        step2 = self.__step2(fid)
        result[eg_2_1] = {k: step1.get(k, 0) + step2.get(k, 0) for k in set(step1) | set(step2)}

        return result
