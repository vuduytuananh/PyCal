from Vu.Memory.data_factory import DataFactory
from Vu.Brain.culture.formulars.Language import LanguageLookup
import math
class F21F:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()
    def getScore(self, fid):
        consultancy = self.__getScore(fid, True)
        notConsultancy = self.__getScore(fid, False)
        return {"EG30": consultancy, "EG29": notConsultancy}
    def __getScore(self, fid, consultancyOrNot):
        result = {}
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID":[], "Location": [], "Industry/Domain":[], "Duration JOB": []})
        #consultancyOrNot
        if consultancyOrNot:
            fl_job = fl_job[fl_job["Industry/Domain"].isin(["Consultancy"])]
        else:
            fl_job = fl_job[~fl_job["Industry/Domain"].isin(["Consultancy"])]
        fl_personal = self.__data_factory.getTab(self.__data_type, "Personal", {"FID": [fid], "Nationality Location": []})
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Duration": [], "Location": []})
        fl_language = self.__data_factory.getTab(self.__data_type, "Language", {"FID":[fid], "Country": [], "Level": []})

        nationality_location = fl_personal["Nationality Location"].values
        # ignore the Country which is the same with nationality
        fl_assignment = fl_assignment[~fl_assignment["Location"].isin(nationality_location)]

        #Job Tab
        diff_nationality = fl_job[~fl_job["Location"].isin(nationality_location)]
        diff_nationality_grouped = diff_nationality.groupby("Location")["Duration JOB"]
        diff_nationality_out = {k: math.fsum(list(v)) for k,v in diff_nationality_grouped}
        diff_nationality_jid = diff_nationality["JID"].values
        diff_nationality_location = diff_nationality["Location"].values
        jid_location = dict(zip(diff_nationality_jid, diff_nationality_location))

        #Assignment tab
        jid_diff_nationality_duration = {}
        for i in jid_location:
            df = fl_assignment[(fl_assignment["JID"] == i) & (fl_assignment["Location"] != jid_location[i])]
            total = math.fsum(df["Duration"].values)
            if i in jid_diff_nationality_duration:
                jid_diff_nationality_duration[i] += total
            else:
                jid_diff_nationality_duration[i] = total
        for i in jid_diff_nationality_duration:
            location = jid_location[i]
            diff_nationality_out[location] -= jid_diff_nationality_duration[i]

        adf = fl_assignment[fl_assignment["JID"].isin(diff_nationality_jid)][~fl_assignment["Location"].isin(diff_nationality_location)]
        adf_grouped = adf.groupby("Location")["Duration"]
        temp = {k: math.fsum(list(v)) for k, v in adf_grouped}
        result = {**diff_nationality_out, **temp}
        result = LanguageLookup().lookup(fid, result)
        return result
#Test
data = F21F()
print(data.getScore("FL-00001"))
