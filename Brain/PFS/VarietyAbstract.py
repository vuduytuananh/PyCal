from PyCal.Memory.data_factory import DataFactory
import math
class VarietyAbstract:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()
    def __getTabVariety(self, df, actCategory, perspective):
        """
        Check for x-Activities
        if at least one x-Activity was selected in ASSIGNMENT or JOB count as "1"
        if not, then count as "0"
        """
        df = df[df[actCategory] != 0]
        return set(df[perspective].values)

    def getScore(self, fid, actCategory, jobTabPerspective, assignmentTabPerspective, eg):
        result = {}

        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], actCategory: [], assignmentTabPerspective: []})
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], actCategory: [], jobTabPerspective: []})
        """
        Look up ASSIGNMENT and JOBS and count selected number of activities.
        """
        assignment_out = self.__getTabVariety(fl_assignment, actCategory, assignmentTabPerspective)
        job_out = self.__getTabVariety(fl_job, actCategory, jobTabPerspective)
        """
        Check CLIENT NAME of ASSIGNMENT and JOBS
        Count number of different CLIENT NAME related to each FREELANCER
        """
        assignment_out.update(job_out)
        result[eg] = len(assignment_out)
        return result

    def getAssignmentVariety(self, fid, actCategory, assignmentTabPerspective, eg):
        result = {}
        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], actCategory: [], assignmentTabPerspective: []})
        assignment_out = self.__getTabVariety(fl_assignment, actCategory, assignmentTabPerspective)
        result[eg] = len(assignment_out)
        return result

    def getJobVariety(self, fid, actCategory, jobTabPerspective, eg):
        result = {}
        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], actCategory: [], jobTabPerspective: []})
        job_out = self.__getTabVariety(fl_job, actCategory, jobTabPerspective)
        result[eg] = len(job_out)
        return result
