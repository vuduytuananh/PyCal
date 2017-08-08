from PyCal.Memory.data_factory import DataFactory
import math
class DurationAbstract:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def __getTabScore(self, df, actCategory):
        """
        Look up ASSIGNMENT and count selected number of activities.
        Check for x-Activities and count
        Divide x-Activity sum by number of selected overall activities
        Multiple result with duration in months of ASSIGNMENT and JOB
        """
        df["Relative-Activity"] = df[actCategory]/(df["E-Activity"] + df["A-Activity"] + df["M-Activity"])*df["Duration"]
        return math.fsum(df["Relative-Activity"].values)
    def getJobDuration(self, fid, actCategory, eg):
        result = {}
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid],"E-Activity": [], "A-Activity": [], "M-Activity": [], "Duration": []})
        job_out = self.__getTabScore(fl_job, actCategory)
        result[eg] = job_out
        return result

    def getAssignmentDuration(self, fid, actCategory, eg):
        result = {}
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "E-Activity": [], "A-Activity": [], "M-Activity": [], "Duration": []})
        assignment_out = self.__getTabScore(fl_assignment, actCategory)
        result[eg] = assignment_out
        return result

    def getScore(self, fid, actCategory, eg):
        return {eg: self.getAssignmentDuration(fid, actCategory, eg)[eg] + self.getJobDuration(fid, actCategory, eg)[eg]}
