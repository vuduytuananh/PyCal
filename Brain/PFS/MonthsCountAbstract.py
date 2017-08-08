from PyCal.Memory.data_factory import DataFactory
import math
class MonthsCountAbstract:
    def __init__(self):
        self.__data_type = "DataTab"
        self.__data_factory = DataFactory()

    def getAssignmentScore(self, fid, perspective, eg):
        result = {}

        fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], perspective: [], "Duration": []})
        fl_assignment_perspective = fl_assignment[fl_assignment[perspective].notnull()]
        fl_assignment_perspective_grouped = fl_assignment_perspective.groupby(perspective)["Duration"]
        result[eg] = {k: math.fsum(list(v)) for k,v in fl_assignment_perspective_grouped}

        return result

    def getJobScore(self, fid, perspective, eg):
        result = {}

        fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], perspective: [], "Duration": []})
        fl_job_perspective = fl_job[fl_job[perspective].notnull()]
        fl_job_perspective_grouped = fl_job_perspective.groupby(perspective)["Duration"]
        result[eg] = {k: math.fsum(list(v)) for k,v in fl_job_perspective_grouped}

        return result
