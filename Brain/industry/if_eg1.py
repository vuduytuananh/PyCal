from PyCal.Memory.data_factory import DataFactory
import math
class IF_EG_1_1:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()
    """
    STEP 1 (WORK DURATION)
    """
    def __step1(self, fid, sub_industry):
        S1_FACTOR = 1
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [], sub_industry :[], "Duration": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], sub_industry: [], "Duration": []})

        """
        For each JOB ID related to the FREELANCER ID
        1. Check INDUSTRY (Domain) column in the job tab
        A1) If the Input is "Consultancy" then:
        """
        fl_job_consultancy = fl_job[fl_job[sub_industry] == "Consultancy"]

        """
        2. Take the DURATION (months) related to that specific Consultancy JOB ID (Job tab)
        """
        fl_job_consultancy_grouped = fl_job_consultancy.groupby(sub_industry)["Duration"]

        """
        3. At the end sum the DURATIONS (months) related to each Consultancy
        """
        a1_out = {k: math.fsum(list(v)) for k,v in fl_job_consultancy_grouped}


        """
        A2) If the input is "Consultancy" then:
        4. then go to assignment tab and work only with Assignments related to that specific (consultancy) Job ID
        """
        fl_job_consultancy_jid = fl_job_consultancy["JID"].values
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_consultancy_jid)]

        """
        3. then sum up the DURATION (months) related to each particular INDUSTRY (Domain) (Assignment tab)
        """
        fl_assignment_jid_grouped = fl_assignment_jid.groupby(sub_industry)["Duration"]
        a2_out = {k: math.fsum(list(v)) for k,v in fl_assignment_jid_grouped}

        """
        B) If the Input is not "Consultancy" then:
        2. Sum up the the DURATION (months) related to each particular INDUSTRY (Domain) (Job tab)
        """
        fl_job_not_consultancy = fl_job[fl_job[sub_industry] != "Consultancy"]
        fl_job_not_consultancy_grouped = fl_job_not_consultancy.groupby(sub_industry)["Duration"]
        b_out = {k: math.fsum(list(v)) for k,v in fl_job_not_consultancy_grouped}

        """
        Sum up all the DURATIONS (months) related to each INDUSTRY (Domain) and multiply them by the factor x 1 (one)
        """
        res = {k : (a1_out.get(k, 0) + a2_out.get(k, 0) + b_out.get(k, 0)) * S1_FACTOR for k in set(a1_out) | set(a2_out) | set(b_out)}

        return res

    """
    STEP 2 (EDUCATION DURATION)
    """
    def __step2(self, fid, sub_industry):
        S2_FACTOR = 0.5
        """
        1. Check the INDUSTRY (Domain) column in the Education tab
        2. Take the DURATION (months) related to that specific INDUSTRY (Domain)
        """
        fl_edu = self.__data_factory.getTab(self.__data_type, "Education", {"FID": [fid], sub_industry :[], "Duration": []})
        fl_edu_grouped = fl_edu.groupby(sub_industry)["Duration"]

        """
        3. Sum up all the DURATIONS(months) related to each INDUSTRY (Domain) and multiply them by the factor x 0.5 (cero point five)
        """
        res = {k: math.fsum(list(v)) * S2_FACTOR for k, v in fl_edu_grouped}

        return res
    """
    STEP 3 (SUM and obtain TOTAL DURATION)
    """
    def getScore(self, fid, sub_industry):
        eg_1_1 = "EG_1_1"
        result = {}
        """
        1. Sum up all the DURATIONS related to each INDUSTRY(Domain) obtained from step 1 and 2
        """
        s1 = self.__step1(fid, sub_industry)
        s2 = self.__step2(fid, sub_industry)
        result[eg_1_1] = {k: s1.get(k, 0) + s2.get(k,0) for k in set(s1) | set(s2)}
        return result
