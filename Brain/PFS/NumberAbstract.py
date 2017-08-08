from PyCal.Memory.data_factory import DataFactory
import math
class NumberAbstract:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def __getTabScore(self, df, actCategory):
        """
        Check for E-Activities and count
        Divide E-Activity sum by number of selected overall activities
        """
        df["Relative-Activity"] = df[actCategory]/(df["E-Activity"] + df["A-Activity"] + df["M-Activity"])
        return math.fsum(df["Relative-Activity"].values)
    def getScore(self, fid, actCategory, eg):
        result = {}

        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "E-Activity": [], "A-Activity": [], "M-Activity": []})
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid],"E-Activity": [], "A-Activity": [], "M-Activity": []})
        """
        Look up ASSIGNMENT and JOBS and count selected number of activities.
        """
        assignment_out = self.__getTabScore(fl_assignment, actCategory)
        job_out = self.__getTabScore(fl_job, actCategory)
        result[eg] = assignment_out + job_out
        return result
    def getAssignmentNumber(self, fid, actCategory, eg):
        result = {}
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "E-Activity": [], "A-Activity": [], "M-Activity": []})
        assignment_out = self.__getTabScore(fl_assignment, actCategory)
        result[eg] = assignment_out
        return result
    def getJobNumber(self, fid, actCategory, eg):
        result = {}
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid],"E-Activity": [], "A-Activity": [], "M-Activity": []})
        job_out = self.__getTabScore(fl_job, actCategory)
        result[eg] = job_out
        return result
