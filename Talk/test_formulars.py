from Vu.Brain.function.formulars.if9_formular import IF9F
from Vu.Brain.function.formulars.if10_formular import IF10F
from Vu.Brain.function.formulars.if11_formular import IF11F
from Vu.Brain.function.formulars.if12_formular import IF12F
from Vu.Brain.function.formulars.if13_formular import IF13F
from Vu.Brain.function.formulars.if14_formular import IF14F
from Vu.Brain.function.formulars.if15_formular import IF15F
from Vu.Brain.function.formulars.if16_formular import IF16F
from Vu.Brain.function.formulars.if17_formular import IF17F
from Vu.Brain.function.formulars.if18_formular import IF18F
from Vu.Brain.function.formulars.if19_formular import IF19F
from Vu.Brain.function.eg.lookup_standard import LookupStandard
from Vu.Brain.function.weigh.lookup_weigh import LookupWeigh

lookup = LookupStandard()
weighing = LookupWeigh()

def getInfluencerResult(fid, domainORsubdomain, ifNum):
    constructor = globals()["IF" + str(ifNum) + "F"]
    instance = constructor(domainORsubdomain)
    return instance.getResult(fid)
def printSubDimension(domainORsubdomain, IO, freelancer_id):
    final_out = {}
    revert = {}
    for i in range(9, 20):
        influencer = getInfluencerResult(freelancer_id, domainORsubdomain, i)
        IO.write("******************\r\n")
        for j in influencer:
            influencer_name = "IF" +str(i)
            weigh = weighing.getScore(influencer_name)
            IO.write("| " + domainORsubdomain + "\t|\t"+influencer_name+"\t|\t" + j +"\t|\t" + str(float(weigh*100))+"%\r\n")
            eg_score = lookup.getScore(int(j[2:]), influencer[j])
            for k in influencer[j]:
                if k in revert and influencer_name in revert[k]: revert[k][influencer_name] = max(revert[k][influencer_name],eg_score[k])
                elif k in revert: revert[k][influencer_name] = eg_score[k]
                else:
                    revert[k] = {}
                    revert[k][influencer_name] = eg_score[k]
                IO.write("| \t\t" + k + ": " + str(influencer[j][k]) + "\t ===> EG Score:" + str(eg_score[k]) +"\t\r\n")
            IO.write("\r\n")
        IO.write("******************\r\n")
    final_out[domainORsubdomain] = revert
    return final_out
def sumMap(floatMap):
    sum = 0
    for f in floatMap:
        sum += floatMap[f]
    return sum
def printFinalResult(final_out_data, out_file):
    for i in final_out_data:
        out_file.write(i + "\r\n")
        for j in final_out_data[i]:
            for k in final_out_data[i][j]:
                final_out_data[i][j][k] *= weighing.getScore(k)
            final_out_data[i][j] = sumMap(final_out_data[i][j])
            out_file.write("\t" + j + ": " + str(final_out_data[i][j]) + "\r\n")

fid = open("fid.txt", "r")
output = open("CALCULATION.txt", "w")
final_result = open("RESULT.txt", "w")
lines = fid.readlines()
for l in lines:
    l = l.strip()
    output.write("------------------------------------ "+l+" ------------------------------------\n\r")
    final_out_domain = printSubDimension("Domain", output, l)
    final_out_sub_domain = printSubDimension("Sub-Domain", output, l)
    final_out = {}
    final_out["Domain"] = final_out_domain["Domain"]
    final_out["Sub-Domain"] = final_out_sub_domain["Sub-Domain"]

    final_result.write("------------------------------------ "+l+" ------------------------------------\n\r")
    printFinalResult(final_out, final_result)
output.close()
final_result.close()
