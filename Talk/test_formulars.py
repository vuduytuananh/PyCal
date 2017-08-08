from PyCal.Brain.industry.main import IF_1_1, IF_1_2, IF_1_3, IF_1_4, IF_1_5, IF_1_6, IF_1_7, IF_1_8, IF_1_9, IF_1_10, IF_1_11, IF_1_12, IF_1_13, IF_1_14, IF_1_15, IF_1_16, IF_1_17, IF_1_18, IF_1_19, IF_1_20, IF_1_21, IF_1_22, IF_1_23
from PyCal.Brain.function.main import IF_2_1, IF_2_2, IF_2_3, IF_2_4, IF_2_5, IF_2_6, IF_2_7, IF_2_8, IF_2_9, IF_2_10, IF_2_11, IF_2_12, IF_2_13, IF_2_14, IF_2_15
from PyCal.Brain.culture.main import IF_3_1, IF_3_2
from PyCal.Brain.PIL.main import IF_4_1, IF_4_2, IF_4_3, IF_4_4, IF_4_5, IF_4_6, IF_4_7, IF_4_8, IF_4_9, IF_4_10, IF_4_11
from PyCal.Brain.PFS.main import IF_5_1, IF_5_2, IF_5_3, IF_5_4, IF_5_5, IF_5_6, IF_5_7, IF_5_8, IF_5_9, IF_5_10, IF_5_11, IF_5_12, IF_5_13, IF_5_14, IF_5_15, IF_5_16, IF_5_17, IF_5_18, IF_5_19, IF_5_20, IF_5_21
from PyCal.Brain.topics.main import IF_6_1, IF_6_2, IF_6_3, IF_6_4, IF_6_5, IF_6_6, IF_6_7
from PyCal.Brain.function.eg.lookup_standard import LookupStandard, Lookup2D, Lookup1D
from PyCal.Brain.function.weigh.lookup_weigh import LookupWeigh

lookup_standard = LookupStandard()
lookup1d = Lookup1D()
lookup2d = Lookup2D()
weighing = LookupWeigh()

def getInfluencerResult(fid, ifNum, if_tag):
    constructor = globals()[if_tag + str(ifNum)]
    instance = constructor()
    return instance.getScore(fid)
def print2LevelDimension(IO, freelancer_id, start , end, if_tag, dimension_name):
    final_out = {}
    revert = {}
    for i in range(start, end + 1):
        influencer = getInfluencerResult(freelancer_id, i, if_tag)
        influencer_name = if_tag +str(i)
        print(influencer)
        IO.write("******************\r\n")
        for j in influencer:
            weigh = weighing.getScore(influencer_name)
            IO.write(freelancer_id+"\t|\t" +influencer_name+"\t|\t" + j +"\t|\t" + str(float(weigh*100))+"%\r\n")
            eg_score = lookup_standard.getScore(j, influencer[j])
            print(eg_score)
            for k in influencer[j]:
                if k in revert and influencer_name in revert[k]: revert[k][influencer_name] = max(revert[k][influencer_name],eg_score[k])
                elif k in revert: revert[k][influencer_name] = eg_score[k]
                else:
                    revert[k] = {}
                    revert[k][influencer_name] = eg_score[k]
                IO.write("| \t\t" + k + ": " + str(influencer[j][k]) + "\t ===> EG Score:" + str(eg_score[k]) +"\t\r\n")
            IO.write("\r\n")
        IO.write("******************\r\n")
    final_out[dimension_name] = revert
    return final_out
def print1LevelDimension(IO, freelancer_id, start, end, if_tag, dimension_name):
    final_out = {}
    final_out[dimension_name] = 0
    for i in range(1, end + 1):
        influencer = getInfluencerResult(freelancer_id, i, if_tag)
        influencer_name = if_tag +str(i)
        print(influencer)
        IO.write("******************\r\n")
        for j in influencer:
            weigh = weighing.getScore(influencer_name)
            IO.write(freelancer_id+"\t|\t" +influencer_name+"\t|\t" + j +"\t|\t" + str(float(weigh*100))+"%\r\n")
            eg_score = lookup2d.getScore(j, influencer[j])
            # not 2D EG score
            if eg_score == 0: eg_score = lookup1d.getScore(j, influencer[j])
            print(eg_score)
            final_out[dimension_name] += eg_score * weigh
            IO.write("| \t\t" + influencer_name + ": " + str(influencer[j]) + "\t ===> EG Score:" + str(eg_score) +"\t\r\n")
        IO.write("******************\r\n")
    return final_out
def sumMap(floatMap):
    sum = 0
    for f in floatMap:
        sum += floatMap[f]
    return sum
def print1LevelFinal(final_out_data, out_file, freelancer_id):
    for i in final_out_data:
        out_file.write(i + ":\t\t" + str(final_out_data[i]) + "\r\n")

def printFinalResult(final_out_data, out_file, freelancer_id):
    for i in final_out_data:
        out_file.write(i + "\r\n")
        for j in final_out_data[i]:
            for k in final_out_data[i][j]:
                final_out_data[i][j][k] *= weighing.getScore(k)
            final_out_data[i][j] = sumMap(final_out_data[i][j])
            out_file.write("\t\t"+freelancer_id+"\t|\t" + j + ": " + str(final_out_data[i][j]) + "\r\n")

fid = open("fid.txt", "r")
output = open("CALCULATION.txt", "w")
final_result = open("RESULT.txt", "w")
lines = fid.readlines()
for l in lines:
    l = l.strip()
    output.write("------------------------------------ "+l+" ------------------------------------\n\r")
    industry_out = print2LevelDimension(output, l, 1, 23, "IF_1_", "I-N-D-U-S-T-R-Y")
    function_out = print2LevelDimension(output, l, 1, 15, "IF_2_", "F-U-N-C-T-I-O-N")
    culture_out = print2LevelDimension(output, l, 1, 2, "IF_3_", "C-U-L-T--U-R-E")
    pil_out = print1LevelDimension(output, l, 1, 11, "IF_4_", "P-I-L")
    pfs_out = print1LevelDimension(output, l, 1, 21, "IF_5_", "P-F-S")
    topic_out = print2LevelDimension(output, l, 1, 7, "IF_6_", "T-O-P-I-C")
    final_result.write("------------------------------------ "+l+" ------------------------------------\n\r")
    printFinalResult(industry_out, final_result, l)
    printFinalResult(function_out, final_result, l)
    printFinalResult(culture_out, final_result, l)
    print1LevelFinal(pil_out, final_result, l)
    print1LevelFinal(pfs_out, final_result, l)
    printFinalResult(topic_out, final_result, l)
output.close()
final_result.close()
