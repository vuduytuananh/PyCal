from PyCal.Memory.data_factory import DataFactory
import math
def countForTopic(df, unit):
    df_grouped = df.groupby("Topic")[unit]
    return {k: len(list(v)) for k,v in df_grouped}
class IF_6_1:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()
    """
    Time period (time units) spent studying/working in a Topic
    """
    def getScore(self, fid):
        result = {}
        eg_6_1 = "EG_6_1"

        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [], "Duration": []})
        fl_job_topic = self.__data_factory.getTab(self.__data_type, "Topic Job", {"FID": [fid], "JID": [], "Topic": []})
        fl_assignment_topic = self.__data_factory.getTab(self.__data_type, "Topic Assignment", {"FID": [fid], "JID": [], "Assignment ID": [], "Topic": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "Assignment ID":[], "JID": [], "Duration": []})
        """
        STEP 1 (WORK DURATION)
        For each JOB ID related to the FREELANCER ID:
        1. Check TOPIC column in the job tab
        """
        def step1_A(jid):
            """
            2. Use the next formula to calculate the duration (months):
            DURATION (months) related to the specific TOPIC obtained from Job tab
            -(minus)-
            the sum of DURATIONS (months) related to the ASSIGNMENTS of the same Job ID which have TOPICs (assignment tab) different from the TOPIC in the job tab.
            """
            fl_job_jid = fl_job[fl_job["JID"] == jid]
            job_jid_duration = math.fsum(fl_job_jid["Duration"].values)

            fl_assignment_jid = fl_assignment[fl_assignment["JID"] == jid]


            fl_job_topic_jid = fl_job_topic[fl_job_topic["JID"] == jid]
            fl_job_topic_jid_values = fl_job_topic_jid["Topic"].values
            fl_assignment_topic_jid = fl_assignment_topic[fl_assignment_topic["JID"] == jid]
            # the ASSIGNMENTS of the same Job ID which have TOPICs (assignment tab) different from the TOPIC in the job tab
            fl_assignment_topic_jid_diff = fl_assignment_topic_jid[~fl_assignment_topic_jid["Topic"].isin(fl_job_topic_jid_values)]
            # assignment id
            fl_assignment_topic_jid_diff_aid = fl_assignment_topic_jid_diff["Assignment ID"].values
            # assignment that have id coresponding to the topics that is different form method job tab
            fl_assignment_diff = fl_assignment_jid[fl_assignment_jid["Assignment ID"].isin(fl_assignment_topic_jid_diff_aid)]
            # duration of assingments that have topics different from the job topic
            assignment_diff_duration = math.fsum(fl_assignment_diff["Duration"].values)
            duration = job_jid_duration - assignment_diff_duration
            duration_per_job_topic = duration/len(set(fl_job_topic_jid_values))
            a2 = {k: duration_per_job_topic for k in set(fl_job_topic_jid_values)}

            """
            3. then go to assignment tab and work only with Assignments related to that specific Job ID
            4. then sum up only the DURATION (months) related to each particular TOPIC (Assignment tab) which is different from TOPICs (Job tab)
            """
            # topics that are different

            assignment_topic_diff = fl_assignment_topic_jid_diff["Topic"].values
            assignment_topic_diff_len = len(assignment_topic_diff)
            duration_per_assignment_topic = 0
            if assignment_topic_diff_len != 0: duration_per_assignment_topic = assignment_diff_duration/len(assignment_topic_diff)
            a3 = {k: duration_per_assignment_topic for k in set(assignment_topic_diff)}
            return {k: a2.get(k, 0) + a2.get(k, 0) for k in set(a2) | set(a2)}

        def step1_B(jid):
            fl_assignment_jid = fl_assignment[fl_assignment["JID"] == jid]
            total_duration = math.fsum(fl_assignment_jid["Duration"].values)
            fl_assignment_topic_jid = fl_assignment_topic[fl_assignment_topic["JID"] == jid]
            topics = set(fl_assignment_topic_jid["Topic"].values)
            duration_per_topic = total_duration/len(topics)
            return {k: duration_per_topic/2 for k in topics}

        """
        A) If there is an input there (it means its not a consultancy) then:
        """
        step1A_result = {}
        fl_job_wt = fl_job_topic[fl_job_topic["Topic"].notnull()]
        for jid in fl_job_wt["JID"].values:
            jid_result = step1_A(jid)
            step1_result = {k: step1A_result.get(k, 0) + jid_result.get(k,0) for k in set(step1A_result) | set(jid_result)}

        """
        B) If there is no input (its because its a Consultancy) then:
        """
        step1B_result = {}
        fl_job_nt = fl_job_topic[fl_job_topic["Topic"].isnull()]
        for jid in fl_job_nt["JID"].values:
            jid_result = step1_B(jid)
            step1B_result = {k: step1B_result.get(k, 0) + jid_result.get(k,0) for k in set(step1B_result) | set(jid_result)}

        """
        STEP 2 (EDUCATION DURATION)
        1. Check the TOPIC column in the Education tab
        """
        fl_edu = self.__data_factory.getTab(self.__data_type, "Education", {"FID": [fid], "Duration": [], "Topic": []})
        fl_edu_grouped = fl_edu.groupby("Topic")["Duration"]
        step2_result = {k: math.fsum(list(v)) for k,v in fl_edu_grouped}

        result[eg_6_1] = {k: step1A_result.get(k,0) + step1B_result.get(k,0) + step2_result.get(k,0) for k in set(step1A_result) | set(step1B_result) | set(step2_result)}
        return result

class IF_6_2:
    def __init__(self):
        self.__data_factory = DataFactory()
        self.__data_type = "DataTab"

    def getScore(self, fid):
        eg_6_2 = "EG_6_2"
        eg_6_3 = "EG_6_3"
        result = {}

        fl_job_topic = self.__data_factory.getTab(self.__data_type, "Topic Job", {"FID": [fid], "JID": [], "Topic": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Assignment ID": [], "Client name": []})
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [], "Company Name": []})
        fl_assignment_topic = self.__data_factory.getTab(self.__data_type, "Topic Assignment", {"FID": [fid],"JID": [], "Assignment ID":[] ,"Topic": []})
        """
        1. Check TOPIC column in the job tab
        A) If there is no Input (its because its a consultancy) then:
        """
        fl_job_topic_nt = fl_job_topic[fl_job_topic["Topic"].isnull()]
        fl_job_topic_nt_jid = fl_job_topic_nt["JID"].values
        """
        2. go to assignment tab and work only with Assignments related to that specific Consultancy Jobs ID
        """
        fl_assignment_topic_jid = fl_assignment_topic[fl_assignment_topic["JID"].isin(fl_job_topic_nt_jid)]
        fl_assignment_topic_jid_aid = fl_assignment_topic_jid["Assignment ID"].values
        fl_assignment_jid_aid = fl_assignment[fl_assignment["JID"].isin(fl_job_topic_nt_jid)][fl_assignment["Assignment ID"].isin(fl_assignment_topic_jid_aid)]
        """
        3. then count the number of different CLIENT NAMES related to each particular TOPIC (Assignment tab)
        """
        fl_assignment_jid_aid_grouped = fl_assignment_jid_aid.groupby("Assignment ID")["Client name"]
        assignment_client_name = {k:list(v)[0] for k,v in fl_assignment_jid_aid_grouped}
        fl_assignment_topic_jid["Assignment ID"] = fl_assignment_topic_jid["Assignment ID"].map(lambda i : assignment_client_name[i])
        assignment_topic_jid_grouped = fl_assignment_topic_jid.groupby("Topic")["Assignment ID"]
        """
        4. then sum up all the obtained results (from the different consultancy jobs) related to each TOPIC (Domain)
        """
        a_out = {k: len(set(v)) for k,v in assignment_topic_jid_grouped}
        result[eg_6_2] = a_out

        """
        B) If there is an input (its not a consultancy) then:
        """
        fl_job_topic_wt = fl_job_topic[fl_job_topic["Topic"].notnull()]
        fl_job_topic_wt_jid = fl_job_topic_wt["JID"].values
        fl_job_jid = fl_job[fl_job["JID"].isin(fl_job_topic_wt_jid)]
        """
        2. count the number of different COMPANY NAMES (column in job tab) of each particular TOPIC
        """
        fl_job_jid_grouped = fl_job_jid.groupby("JID")["Company Name"]
        jid_company_name = {k:list(v)[0] for k,v in fl_job_jid_grouped}
        fl_job_topic_wt["JID"] = fl_job_topic_wt["JID"].map(lambda i : jid_company_name[i])
        fl_job_topic_wt_grouped = fl_job_topic_wt.groupby("Topic")["JID"]
        """
        3. then sum up all the obtained results (from the different jobs (non-consultancy jobs)) related to each TOPIC
        """
        b_out = {k: len(set(v)) for k,v in fl_job_topic_wt_grouped}
        result[eg_6_3] = b_out

        return result
class IF_6_3:
    def __init__(self):
        self.__data_factory = DataFactory()
        self.__data_type = "DataTab"

    def getScore(self, fid):
        eg_6_4 = "EG_6_4"
        result = {}

        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID":[], "Industry/Domain": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID":[], "Assignment ID":[], "Industry/Domain": []})
        fl_job_topic = self.__data_factory.getTab(self.__data_type, "Topic Job", {"FID": [fid], "JID": [], "Topic": []})
        fl_assignment_topic = self.__data_factory.getTab(self.__data_type, "Topic Assignment", {"FID": [fid], "JID": [], "Assignment ID": [], "Topic": []})
        """
        1. Check TOPIC column in the job tab
        A) If there is no Input (its because its a consultancy) then:
        """
        fl_job_topic_nt = fl_job_topic[fl_job_topic["Topic"].isnull()]
        fl_job_topic_nt_jid = fl_job_topic_nt["JID"].values
        fl_assignment_topic_jid = fl_assignment_topic[fl_assignment_topic["JID"].isin(fl_job_topic_nt_jid)]
        """
        2. go to assignment tab and work only with Assignments related to that specific Consultancy Jobs ID
        """
        fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_topic_nt_jid)]
        fl_assignment_jid_grouped = fl_assignment_jid.groupby("Assignment ID")["Industry/Domain"]
        assignment_idomain = {k: list(v)[0] for k, v in fl_assignment_jid_grouped}
        fl_assignment_topic_jid["Industry/Domain"] = fl_assignment_topic_jid["Assignment ID"].map(lambda i : assignment_idomain[i])
        fl_assignment_topic_jid_grouped = fl_assignment_topic_jid.groupby("Topic")["Industry/Domain"]
        """
        3. then count the number of different INDUSTRIES (Domain) related to each particular TOPIC (Assignment tab)
        """
        a_out = {k: len(set(v)) for k,v in fl_assignment_topic_jid_grouped}
        """
        B) If there is an input (its because its not a consultancy) then
        """
        fl_job_topic_wt = fl_job_topic[fl_job_topic["Topic"].notnull()]
        fl_job_topic_wt_jid = fl_job_topic_wt["JID"].values
        fl_job_jid = fl_job[fl_job["JID"].isin(fl_job_topic_wt_jid)] # job id which is the job_topic not nulls
        fl_job_jid_grouped = fl_job_jid.groupby("JID")["Industry/Domain"]
        job_idomain = {k: list(v)[0] for k,v in fl_job_jid_grouped}
        fl_job_topic_jid = fl_job_topic[fl_job_topic["JID"].isin(fl_job_topic_wt_jid)]
        fl_job_topic_wt["JID"] = fl_job_topic_wt["JID"].map(lambda i : job_idomain[i])
        """
        2. Count the number of different INDUSTRIES (Domain) (column in job tab) of each particular TOPIC
        """
        fl_job_topic_wt_grouped = fl_job_topic_wt.groupby("Topic")["JID"]
        b_out = {k: len(set(v)) for k,v in fl_job_topic_wt_grouped}

        result[eg_6_4] = {k: a_out.get(k,0) + b_out.get(k,0) for k in set(a_out) | set(b_out)}
        return result

class IF_6_4:
    def __init__(self):
        self.__data_factory = DataFactory()
        self.__data_type = "DataTab"

    def getScore(self, fid):
        eg_6_5 = "EG_6_5"
        result = {}
        df = self.__data_factory.getTab(self.__data_type, "Publications", {"FID": [fid], "Topic": [], "Publication ID": []})
        """
        1. Check the TOPIC column in the Publications tab
        2. then count, in the PUBLICATION ID column, the number of publications related to the specific TOPIC
        """
        result[eg_6_5] = countForTopic(df, "Publication ID")
        return result

class IF_6_5:
    def __init__(self):
        self.__data_factory = DataFactory()
        self.__data_type = "DataTab"

    def getScore(self, fid):
        eg_6_6 = "EG_6_6"
        result = {}
        df = self.__data_factory.getTab(self.__data_type, "Conferences Speakership", {"FID": [fid], "Topic": [], "Conference Speakership ID": []})
        """
        1. Check the TOPIC column in the Conferences Speakership tab
        2. then count, in the CONFERENCE SPEAKERSHIP ID column, the number of conference speakerships related to the specific TOPIC
        """
        result[eg_6_6] = countForTopic(df, "Conference Speakership ID")
        return result

class IF_6_6:
    def __init__(self):
        self.__data_factory = DataFactory()
        self.__data_type = "DataTab"

    def getScore(self, fid):
        eg_6_7 = "EG_6_7"
        result = {}
        df = self.__data_factory.getTab(self.__data_type, "Memberships", {"FID": [fid], "Topic": [], "Membership ID": []})
        """
        1. Check the TOPIC column in the Memberships tab
        2. then count, in the MEMBERSHIP ID column, the number of memberships related to the specific TOPIC
        """
        result[eg_6_7] = countForTopic(df, "Membership ID")
        return result

class IF_6_7:
    def __init__(self):
        self.__data_factory = DataFactory()
        self.__data_type = "DataTab"

    def getScore(self, fid):
        eg_6_8 = "EG_6_8"
        result = {}
        df = self.__data_factory.getTab(self.__data_type, "Trainings & Certificates", {"FID": [fid], "Topic": [], "TNCID": []})
        """
        1. Check the TOPIC column in the Trainings & Certificates tab
        2. then in the Trainings & Certificates ID column, count the number of Training & Certificates related to the specific TOPIC
        """
        result[eg_6_8] = countForTopic(df, "TNCID")
        return result

# print(IF_6_1().getScore("FL-00001"))
# print(IF_6_2().getScore("FL-00001"))
# print(IF_6_3().getScore("FL-00001"))
# print(IF_6_4().getScore("FL-00001"))
# print(IF_6_5().getScore("FL-00001"))
# print(IF_6_6().getScore("FL-00001"))
# print(IF_6_7().getScore("FL-00001"))
