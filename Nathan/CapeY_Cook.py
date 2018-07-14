from PIL import Image
import random

#def claimroute():
board = Image.open('fixed_board_1.png')
blackTrak = Image.open('smallBlakTrak.png')
blueTrak = Image.open('smallBlueTrak.png')
redTrak = Image.open('smallRedTrak.png')
orangeTrak = Image.open('smallOrangeTrak.png')
yellowTrak = Image.open('smallYellowTrak.png')
pinkTrak = Image.open('smallPinkTrak.png')
greenTrak = Image.open('smallGreenTrak.png')

trakList=[blackTrak, blueTrak, redTrak, orangeTrak, yellowTrak, pinkTrak, greenTrak]
#t=5

#playerList=[1, 2, 3, 4, 5, 6]


#player2=random.randomint(0,6)
#while player1==player2:
#    player2=random.randomint(0,6)
player1Colour=6
player2Colour=1
player3Colour=2
player4Colour=3
player5Colour=4
player6Colour=5

xIndex=[778, 796, 805, 811, 835, 853, 869, 873, 863, 840, 852, 786, 785, 770, 882, 904, 923, 936, 726, 758, 765, 774, 794, 956, 973, 679, 657, 643, 647, 639, 610, 580, 573, 578, 583, 587, 593, 597, 603, 559, 564, 568, 573, 578, 584, 590, 998, 1002, 993, 974, 922, 896, 880, 871, 860, 816, 806, 785, 757, 728, 701, 677, 837, 848, 847, 844, 948, 928, 900, 870, 820, 796, 787, 932, 903, 886, 794, 797, 801, 873, 855, 826, 953, 943, 925, 905, 878, 850, 820, 801, 799, 798, 810, 785, 758, 727, 748, 756, 750, 714, 707, 682, 683, 651, 624, 852, 838, 822, 690, 667, 637, 608, 578, 549, 578, 547, 609, 613, 603, 588, 566, 544, 623, 646, 659, 665, 663, 703, 695, 678, 652, 625, 536, 509, 485, 462, 442, 418, 393, 578, 547, 520, 500, 479, 401, 431, 456, 365, 344, 315, 286, 391, 391, 377, 354, 330, 283, 301, 252, 228, 207, 213, 242, 272, 290, 279, 287, 325, 341, 357, 317, 332, 347, 313, 342, 388, 417, 445, 474, 502, 387, 416, 445, 474, 502, 449, 478, 508, 524, 351, 374, 404, 317, 289, 273, 264, 273]
yIndex=[114, 118, 146, 102, 120, 142, 168, 199, 226, 196, 224, 169, 200, 224, 261, 284, 310, 336, 235, 263, 292, 321, 343, 378, 404, 222, 202, 177, 147, 111, 103, 112, 147, 177, 208, 238, 269, 299, 330, 148, 178, 209, 239, 270, 301, 332, 448, 477, 506, 528, 359, 371, 395, 421, 448, 369, 399, 417, 427, 435, 447, 463, 356, 385, 414, 445, 521, 497, 484, 474, 468, 483, 513, 539, 546, 571, 559, 590, 623, 622, 645, 651, 567, 597, 620, 640, 657, 669, 664, 668, 700, 731, 758, 662, 668, 551, 572, 602, 631, 528, 500, 483, 557, 552, 538, 271, 297, 324, 534, 515, 507, 508, 511, 516, 533, 531, 374, 401, 430, 456, 477, 497, 354, 371, 400, 427, 456, 258, 286, 310, 323, 335, 125, 136, 151, 171, 194, 214, 231, 356, 353, 342, 324, 301, 244, 242, 258, 269,291, 303, 312, 270, 300, 325, 343, 360, 333, 358, 340, 355, 385, 414, 448, 460, 389, 416, 446, 395, 422, 450, 401, 428, 454, 483, 486, 467, 476, 485, 496, 504, 478, 487, 496, 507, 515, 557, 561, 561, 537, 565, 546, 543, 598, 595, 551, 506, 480]

t=0



def capeYToWeipa():
#area = (778, 114, 808, 126)
    area = (xIndex[0], yIndex[0], xIndex[0] + 30, yIndex[0] + 12)
    board.paste(trakList[t], area)

def capeToCooktown():
#area = (796, 118, 826, 130)
    area = (xIndex[1], yIndex[1], xIndex[1] + 30, yIndex[1] + 12)
    board.paste(trakList[t], area)
#area = (805, 146, 835, 158)
    area = (xIndex[2], yIndex[2], xIndex[2] + 30, yIndex[2] + 12)
    board.paste(trakList[t], area)


def capeYToMackay():
#area = (811, 102, 841, 114)
    area = (xIndex[3], yIndex[3], xIndex[3] + 30, yIndex[3] + 12)
    board.paste(trakList[t], area)
#area = (835, 120, 865, 132)
    area = (xIndex[4], yIndex[4], xIndex[4] + 30, yIndex[4] + 12)
    board.paste(trakList[t], area)
#area = (853, 142, 883, 154)
    area = (xIndex[5], yIndex[5], xIndex[5] + 30, yIndex[5] + 12)
    board.paste(trakList[t], area)
#area = (869, 168, 899, 180)
    area = (xIndex[6], yIndex[6], xIndex[6] + 30, yIndex[6] + 12)
    board.paste(trakList[t], area)
#area = (873, 199, 903, 211)
    area = (xIndex[7], yIndex[7], xIndex[7] + 30, yIndex[7] + 12)
    board.paste(trakList[t], area)
#area = (863, 226, 893, 238)
    area = (xIndex[8], yIndex[8], xIndex[8] + 30, yIndex[8] + 12)
    board.paste(trakList[t], area)

def cooktownToMackay():
#area = (825, 190, 855, 202)
    area = (xIndex[9] - 15, yIndex[9] - 6, xIndex[9] + 15, yIndex[9] + 6)
    board.paste(trakList[t], area)
#area = (837, 218, 867, 230)
    area = (xIndex[10] - 15, yIndex[10] - 6, xIndex[10] + 15, yIndex[10] + 6)
    board.paste(trakList[t], area)

def weipaToKarumba():
#area = (771, 163, 801, 175)
    area = (xIndex[11] - 15, yIndex[11] - 6, xIndex[11] + 15, yIndex[11] + 6)
    board.paste(trakList[t], area)
#area = (770, 194, 800, 206)
    area = (xIndex[12] - 15, yIndex[12] - 6, xIndex[12] + 15, yIndex[12] + 6)
    board.paste(trakList[t], area)
#area = (755, 218, 785, 230)
    area = (xIndex[13] - 15, yIndex[13] - 6, xIndex[13] + 15, yIndex[13] + 6)
    board.paste(trakList[t], area)

def MackayToBundy():
#area = (867, 255, 897, 267)
    area = (xIndex[14] - 15, yIndex[14] - 6, xIndex[14] + 15, yIndex[14] + 6)
    board.paste(trakList[t], area)
#area = (889, 278, 919, 290)
    area = (xIndex[15] - 15, yIndex[15] - 6, xIndex[15] + 15, yIndex[15] + 6)
    board.paste(trakList[t], area)
#area = (908, 304, 938, 316)
    area = (xIndex[16] - 15, yIndex[16] - 6, xIndex[16] + 15, yIndex[16] + 6)
    board.paste(trakList[t], area)
#area = (921, 330, 951, 342)
    area = (xIndex[17] - 15, yIndex[17] - 6, xIndex[17] + 15, yIndex[17] + 6)
    board.paste(trakList[t], area)

def karumbaToBurketown():
#area = (711, 229, 741, 241)
    area = (xIndex[18] - 15, yIndex[18] - 6, xIndex[18] + 15, yIndex[18] + 6)
    board.paste(trakList[t], area)

def karumbaToMtIsa():
#area = (743, 257, 773, 269)
    area = (xIndex[19] - 15, yIndex[19] - 6, xIndex[19] + 15, yIndex[19] + 6)
    board.paste(trakList[t], area)
#area = (750, 286, 780, 298)
    area = (xIndex[20] - 15, yIndex[20] - 6, xIndex[20] + 15, yIndex[20] + 6)
    board.paste(trakList[t], area)
#area = (759, 315, 789, 327)
    area = (xIndex[21] - 15, yIndex[21] - 6, xIndex[21] + 15, yIndex[21] + 6)
    board.paste(trakList[t], area)
#area = (779, 337, 809, 349)
    area = (xIndex[22] - 15, yIndex[22] - 6, xIndex[22] + 15, yIndex[22] + 6)
    board.paste(trakList[t], area)

def bundyToBrisbane():
#area = (941, 372, 971, 384)
    area = (xIndex[23] - 15, yIndex[23] - 6, xIndex[23] + 15, yIndex[23] + 6)
    board.paste(trakList[t], area)
    #area = (958, 398, 988,410)
    area = (xIndex[24] - 15, yIndex[24] - 6, xIndex[24] + 15, yIndex[24] + 6)
    board.paste(trakList[t], area)

def burketownToNhulunbuy():
#area = (664, 216, 694, 228)
    area = (xIndex[25] - 15, yIndex[25] - 6, xIndex[25] + 15, yIndex[25] + 6)
    board.paste(trakList[t], area)
#area = (642, 196, 672, 208)
    area = (xIndex[26] - 15, yIndex[26] - 6, xIndex[26] + 15, yIndex[26] + 6)
    board.paste(trakList[t], area)
#area = (628, 171, 658, 183)
    area = (xIndex[27] - 15, yIndex[27] - 6, xIndex[27] + 15, yIndex[27] + 6)
    board.paste(trakList[t], area)
#area = (632, 146, 662, 158)
    area = (xIndex[28] - 15, yIndex[28] - 6, xIndex[28] + 15, yIndex[28] + 6)
    board.paste(trakList[t], area)

def nhulunbuyToDarwin():
    area = (xIndex[29] - 15, yIndex[29] - 6, xIndex[29] + 15, yIndex[29] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[30] - 15, yIndex[30] - 6, xIndex[30] + 15, yIndex[30] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[31] - 15, yIndex[31] - 6, xIndex[31] + 15, yIndex[31] + 6)
    board.paste(trakList[t], area)

def darwinToAliceA():
    area = (xIndex[32] - 15, yIndex[32] - 6, xIndex[32] + 15, yIndex[32] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[33] - 15, yIndex[33] - 6, xIndex[33] + 15, yIndex[33] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[34] - 15, yIndex[34] - 6, xIndex[34] + 15, yIndex[34] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[35] - 15, yIndex[35] - 6, xIndex[35] + 15, yIndex[35] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[36] - 15, yIndex[36] - 6, xIndex[36] + 15, yIndex[36] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[37] - 15, yIndex[37] - 6, xIndex[37] + 15, yIndex[37] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[38] - 15, yIndex[38] - 6, xIndex[38] + 15, yIndex[38] + 6)
    board.paste(trakList[t], area)

def darwinToAliceB():
    area = (xIndex[39] - 15, yIndex[39] - 6, xIndex[39] + 15, yIndex[39] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[40] - 15, yIndex[40] - 6, xIndex[40] + 15, yIndex[40] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[41] - 15, yIndex[41] - 6, xIndex[41] + 15, yIndex[41] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[42] - 15, yIndex[42] - 6, xIndex[42] + 15, yIndex[42] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[43] - 15, yIndex[43] - 6, xIndex[43] + 15, yIndex[43] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[44] - 15, yIndex[44] - 6, xIndex[44] + 15, yIndex[44] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[45] - 15, yIndex[45] - 6, xIndex[45] + 15, yIndex[45] + 6)
    board.paste(trakList[t], area)

def brisbaneToSydney():
    area = (xIndex[46] - 15, yIndex[46] - 6, xIndex[46] + 15, yIndex[46] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[47] - 15, yIndex[47] - 6, xIndex[47] + 15, yIndex[47] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[48] - 15, yIndex[48] - 6, xIndex[48] + 15, yIndex[48] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[49] - 15, yIndex[49] - 6, xIndex[49] + 15, yIndex[49] + 6)
    board.paste(trakList[t], area)

def bundyToBourke():
    area = (xIndex[50] - 15, yIndex[50] - 6, xIndex[50] + 15, yIndex[50] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[51] - 15, yIndex[51] - 6, xIndex[51] + 15, yIndex[51] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[52] - 15, yIndex[52] - 6, xIndex[52] + 15, yIndex[52] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[53] - 15, yIndex[53] - 6, xIndex[53] + 15, yIndex[53] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[54] - 15, yIndex[54] - 6, xIndex[54] + 15, yIndex[54] + 6)
    board.paste(trakList[t], area)

def mtIsaToCooberPedy():
    area = (xIndex[55] - 15, yIndex[55] - 6, xIndex[55] + 15, yIndex[55] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[56] - 15, yIndex[56] - 6, xIndex[56] + 15, yIndex[56] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[57] - 15, yIndex[57] - 6, xIndex[57] + 15, yIndex[57] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[58] - 15, yIndex[58] - 6, xIndex[58] + 15, yIndex[58] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[59] - 15, yIndex[59] - 6, xIndex[59] + 15, yIndex[59] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[60] - 15, yIndex[60] - 6, xIndex[60] + 15, yIndex[60] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[61] - 15, yIndex[61] - 6, xIndex[61] + 15, yIndex[61] + 6)
    board.paste(trakList[t], area)

def mtIsaToBourke():
    area = (xIndex[62] - 15, yIndex[62] - 6, xIndex[62] + 15, yIndex[62] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[63] - 15, yIndex[63] - 6, xIndex[63] + 15, yIndex[63] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[64] - 15, yIndex[64] - 6, xIndex[64] + 15, yIndex[64] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[65] - 15, yIndex[65] - 6, xIndex[65] + 15, yIndex[65] + 6)
    board.paste(trakList[t], area)

def sydneyToBourke():
    area = (xIndex[66] - 15, yIndex[66] - 6, xIndex[66] + 15, yIndex[66] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[67] - 15, yIndex[67] - 6, xIndex[67] + 15, yIndex[67] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[68] - 15, yIndex[68] - 6, xIndex[68] + 15, yIndex[68] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[69] - 15, yIndex[69] - 6, xIndex[69] + 15, yIndex[69] + 6)
    board.paste(trakList[t], area)

def bourkeToBrokenHill():
    area = (xIndex[70] - 15, yIndex[70] - 6, xIndex[70] + 15, yIndex[70] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[71] - 15, yIndex[71] - 6, xIndex[71] + 15, yIndex[71] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[72] - 15, yIndex[72] - 6, xIndex[72] + 15, yIndex[72] + 6)
    board.paste(trakList[t], area)

def sydneyToCanberra():
    area = (xIndex[73] - 15, yIndex[73] - 6, xIndex[73] + 15, yIndex[73] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[74] - 15, yIndex[74] - 6, xIndex[74] + 15, yIndex[74] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[75] - 15, yIndex[75] - 6, xIndex[75] + 15, yIndex[75] + 6)
    board.paste(trakList[t], area)

def brokenHillToMelbs():
    area = (xIndex[76] - 15, yIndex[76] - 6, xIndex[76] + 15, yIndex[76] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[77] - 15, yIndex[77] - 6, xIndex[77] + 15, yIndex[77] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[78] - 15, yIndex[78] - 6, xIndex[78] + 15, yIndex[78] + 6)
    board.paste(trakList[t], area)

def canberraToMelbs():
    area = (xIndex[79] - 15, yIndex[79] - 6, xIndex[79] + 15, yIndex[79] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[80] - 15, yIndex[80] - 6, xIndex[80] + 15, yIndex[80] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[81] - 15, yIndex[81] - 6, xIndex[81] + 15, yIndex[81] + 6)
    board.paste(trakList[t], area)

def sydneyToMelbs():
    area = (xIndex[82] - 15, yIndex[82] - 6, xIndex[82] + 15, yIndex[82] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[83] - 15, yIndex[83] - 6, xIndex[83] + 15, yIndex[83] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[84] - 15, yIndex[84] - 6, xIndex[84] + 15, yIndex[84] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[85] - 15, yIndex[85] - 6, xIndex[85] + 15, yIndex[85] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[86] - 15, yIndex[86] - 6, xIndex[86] + 15, yIndex[86] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[87] - 15, yIndex[87] - 6, xIndex[87] + 15, yIndex[87] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[88] - 15, yIndex[88] - 6, xIndex[88] + 15, yIndex[88] + 6)
    board.paste(trakList[t], area)

def melbsToHobart():
    area = (xIndex[89] - 15, yIndex[89] - 6, xIndex[89] + 15, yIndex[89] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[90] - 15, yIndex[90] - 6, xIndex[90] + 15, yIndex[90] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[91] - 15, yIndex[91] - 6, xIndex[91] + 15, yIndex[91] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[92] - 15, yIndex[92] - 6, xIndex[92] + 15, yIndex[92] + 6)
    board.paste(trakList[t], area)

def melbsToPortland():
    area = (xIndex[93] - 15, yIndex[93] - 6, xIndex[93] + 15, yIndex[93] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[94] - 15, yIndex[94] - 6, xIndex[94] + 15, yIndex[94] + 6)
    board.paste(trakList[t], area)

def adelaideToPortland():
    area = (xIndex[95] - 15, yIndex[95] - 6, xIndex[95] + 15, yIndex[95] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[96] - 15, yIndex[96] - 6, xIndex[96] + 15, yIndex[96] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[97] - 15, yIndex[97] - 6, xIndex[97] + 15, yIndex[97] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[98] - 15, yIndex[98] - 6, xIndex[98] + 15, yIndex[98] + 6)
    board.paste(trakList[t], area)

def adelaideToCooberPedy():
    area = (xIndex[99] - 15, yIndex[99] - 6, xIndex[99] + 15, yIndex[99] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[100] - 15, yIndex[100] - 6, xIndex[100] + 15, yIndex[100] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[101] - 15, yIndex[101] - 6, xIndex[101] + 15, yIndex[101] + 6)
    board.paste(trakList[t], area)

def adelaideToCeduna():
    area = (xIndex[102] - 15, yIndex[102] - 6, xIndex[102] + 15, yIndex[102] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[103] - 15, yIndex[103] - 6, xIndex[103] + 15, yIndex[103] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[104] - 15, yIndex[104] - 6, xIndex[104] + 15, yIndex[104] + 6)
    board.paste(trakList[t], area)

def mackayToMtIsa():
    area = (xIndex[105] - 15, yIndex[105] - 6, xIndex[105] + 15, yIndex[105] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[106] - 15, yIndex[106] - 6, xIndex[106] + 15, yIndex[106] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[107] - 15, yIndex[107] - 6, xIndex[107] + 15, yIndex[107] + 6)
    board.paste(trakList[t], area)

def adelaideToBorderVillage():
    area = (xIndex[108] - 15, yIndex[108] - 6, xIndex[108] + 15, yIndex[108] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[109] - 15, yIndex[109] - 6, xIndex[109] + 15, yIndex[109] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[110] - 15, yIndex[110] - 6, xIndex[110] + 15, yIndex[110] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[111] - 15, yIndex[111] - 6, xIndex[111] + 15, yIndex[111] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[112] - 15, yIndex[112] - 6, xIndex[112] + 15, yIndex[112] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[113] - 15, yIndex[113] - 6, xIndex[113] + 15, yIndex[113] + 6)
    board.paste(trakList[t], area)

def cedunaToBorderVillage():
    area = (xIndex[114] - 15, yIndex[114] - 6, xIndex[114] + 15, yIndex[114] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[115] - 15, yIndex[115] - 6, xIndex[115] + 15, yIndex[115] + 6)
    board.paste(trakList[t], area)

def aliceToBorderVillage():
    area = (xIndex[116] - 15, yIndex[116] - 6, xIndex[116] + 15, yIndex[116] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[117] - 15, yIndex[117] - 6, xIndex[117] + 15, yIndex[117] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[118] - 15, yIndex[118] - 6, xIndex[118] + 15, yIndex[118] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[119] - 15, yIndex[119] - 6, xIndex[119] + 15, yIndex[119] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[120] - 15, yIndex[120] - 6, xIndex[120] + 15, yIndex[120] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[121] - 15, yIndex[121] - 6, xIndex[121] + 15, yIndex[121] + 6)
    board.paste(trakList[t], area)

def aliceToCooberPedy():
    area = (xIndex[122] - 15, yIndex[122] - 6, xIndex[122] + 15, yIndex[122] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[123] - 15, yIndex[123] - 6, xIndex[123] + 15, yIndex[123] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[124] - 15, yIndex[124] - 6, xIndex[124] + 15, yIndex[124] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[125] - 15, yIndex[125] - 6, xIndex[125] + 15, yIndex[125] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[126] - 15, yIndex[126] - 6, xIndex[126] + 15, yIndex[126] + 6)
    board.paste(trakList[t], area)

def burketownToAlice():
    area = (xIndex[127] - 15, yIndex[127] - 6, xIndex[127] + 15, yIndex[127] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[128] - 15, yIndex[128] - 6, xIndex[128] + 15, yIndex[128] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[129] - 15, yIndex[129] - 6, xIndex[129] + 15, yIndex[129] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[130] - 15, yIndex[130] - 6, xIndex[130] + 15, yIndex[130] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[131] - 15, yIndex[131] - 6, xIndex[131] + 15, yIndex[131] + 6)
    board.paste(trakList[t], area)

def darwinToBroome():
    area = (xIndex[132] - 15, yIndex[132] - 6, xIndex[132] + 15, yIndex[132] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[133] - 15, yIndex[133] - 6, xIndex[133] + 15, yIndex[133] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[134] - 15, yIndex[134] - 6, xIndex[134] + 15, yIndex[134] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[135] - 15, yIndex[135] - 6, xIndex[135] + 15, yIndex[135] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[136] - 15, yIndex[136] - 6, xIndex[136] + 15, yIndex[136] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[137] - 15, yIndex[137] - 6, xIndex[137] + 15, yIndex[137] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[138] - 15, yIndex[138] - 6, xIndex[138] + 15, yIndex[138] + 6)
    board.paste(trakList[t], area)

def aliceToHallsCreek():
    area = (xIndex[139] - 15, yIndex[139] - 6, xIndex[139] + 15, yIndex[139] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[140] - 15, yIndex[140] - 6, xIndex[140] + 15, yIndex[140] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[141] - 15, yIndex[141] - 6, xIndex[141] + 15, yIndex[141] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[142] - 15, yIndex[142] - 6, xIndex[142] + 15, yIndex[142] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[143] - 15, yIndex[143] - 6, xIndex[143] + 15, yIndex[143] + 6)
    board.paste(trakList[t], area)

def broomeToHallsCreek():
    area = (xIndex[144] - 15, yIndex[144] - 6, xIndex[144] + 15, yIndex[144] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[145] - 15, yIndex[145] - 6, xIndex[145] + 15, yIndex[145] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[146] - 15, yIndex[146] - 6, xIndex[146] + 15, yIndex[146] + 6)
    board.paste(trakList[t], area)


def broomeToKaratha():
    area = (xIndex[147] - 15, yIndex[147] - 6, xIndex[147] + 15, yIndex[147] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[148] - 15, yIndex[148] - 6, xIndex[148] + 15, yIndex[148] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[149] - 15, yIndex[149] - 6, xIndex[149] + 15, yIndex[149] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[150] - 15, yIndex[150] - 6, xIndex[150] + 15, yIndex[150] + 6)
    board.paste(trakList[t], area)


def broomeToNewman():
    area = (xIndex[151] - 15, yIndex[151] - 6, xIndex[151] + 15, yIndex[151] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[152] - 15, yIndex[152] - 6, xIndex[152] + 15, yIndex[152] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[153] - 15, yIndex[153] - 6, xIndex[153] + 15, yIndex[153] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[154] - 15, yIndex[154] - 6, xIndex[154] + 15, yIndex[154] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[155] - 15, yIndex[155] - 6, xIndex[155] + 15, yIndex[155] + 6)
    board.paste(trakList[t], area)

def karathaToNewman():
    area = (xIndex[156] - 15, yIndex[156] - 6, xIndex[156] + 15, yIndex[156] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[157] - 15, yIndex[157] - 6, xIndex[157] + 15, yIndex[157] + 6)
    board.paste(trakList[t], area)

def karathaToExmouth():
    area = (xIndex[158] - 15, yIndex[158] - 6, xIndex[158] + 15, yIndex[158] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[159] - 15, yIndex[159] - 6, xIndex[159] + 15, yIndex[159] + 6)
    board.paste(trakList[t], area)

def exmouthToCarnarvan():
    area = (xIndex[160] - 15, yIndex[160] - 6, xIndex[160] + 15, yIndex[160] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[161] - 15, yIndex[161] - 6, xIndex[161] + 15, yIndex[161] + 6)
    board.paste(trakList[t], area)

def carnarvanToMtMagnet():
    area = (xIndex[162] - 15, yIndex[162] - 6, xIndex[162] + 15, yIndex[162] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[163] - 15, yIndex[163] - 6, xIndex[163] + 15, yIndex[163] + 6)
    board.paste(trakList[t], area)

def newmanToMtMagnet():
    area = (xIndex[164] - 15, yIndex[164] - 6, xIndex[164] + 15, yIndex[164] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[165] - 15, yIndex[165] - 6, xIndex[165] + 15, yIndex[165] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[166] - 15, yIndex[166] - 6, xIndex[166] + 15, yIndex[166] + 6)
    board.paste(trakList[t], area)

def newmanToKarlgoolieA():
    area = (xIndex[167] - 15, yIndex[167] - 6, xIndex[167] + 15, yIndex[167] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[168] - 15, yIndex[168] - 6, xIndex[168] + 15, yIndex[168] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[169] - 15, yIndex[169] - 6, xIndex[169] + 15, yIndex[169] + 6)
    board.paste(trakList[t], area)

def newmanToKarlgoolieB():
    area = (xIndex[170] - 15, yIndex[170] - 6, xIndex[170] + 15, yIndex[170] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[171] - 15, yIndex[171] - 6, xIndex[171] + 15, yIndex[171] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[172] - 15, yIndex[172] - 6, xIndex[172] + 15, yIndex[172] + 6)
    board.paste(trakList[t], area)

def mtMagnetToKarlgoolie():
    area = (xIndex[173] - 15, yIndex[173] - 6, xIndex[173] + 15, yIndex[173] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[174] - 15, yIndex[174] - 6, xIndex[174] + 15, yIndex[174] + 6)
    board.paste(trakList[t], area)

def karlgoolieToBorberVillageA():
    area = (xIndex[175] - 15, yIndex[175] - 6, xIndex[175] + 15, yIndex[175] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[176] - 15, yIndex[176] - 6, xIndex[176] + 15, yIndex[176] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[177] - 15, yIndex[177] - 6, xIndex[177] + 15, yIndex[177] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[178] - 15, yIndex[178] - 6, xIndex[178] + 15, yIndex[178] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[179] - 15, yIndex[179] - 6, xIndex[179] + 15, yIndex[179] + 6)
    board.paste(trakList[t], area)

def karlgoolieToBorberVillageB():
    area = (xIndex[180] - 15, yIndex[180] - 6, xIndex[180] + 15, yIndex[180] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[181] - 15, yIndex[181] - 6, xIndex[181] + 15, yIndex[181] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[182] - 15, yIndex[182] - 6, xIndex[182] + 15, yIndex[182] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[183] - 15, yIndex[183] - 6, xIndex[183] + 15, yIndex[183] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[184] - 15, yIndex[184] - 6, xIndex[184] + 15, yIndex[184] + 6)
    board.paste(trakList[t], area)

def esperanceToBorderVillage():
    area = (xIndex[185] - 15, yIndex[185] - 6, xIndex[185] + 15, yIndex[185] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[186] - 15, yIndex[186] - 6, xIndex[186] + 15, yIndex[186] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[187] - 15, yIndex[187] - 6, xIndex[187] + 15, yIndex[187] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[188] - 15, yIndex[188] - 6, xIndex[188] + 15, yIndex[188] + 6)
    board.paste(trakList[t], area)

def albanyToEsperance():
    area = (xIndex[189] - 15, yIndex[189] - 6, xIndex[189] + 15, yIndex[189] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[190] - 15, yIndex[190] - 6, xIndex[190] + 15, yIndex[190] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[191] - 15, yIndex[191] - 6, xIndex[191] + 15, yIndex[191] + 6)
    board.paste(trakList[t], area)

def albanyToBunbury():
    area = (xIndex[192] - 15, yIndex[192] - 6, xIndex[192] + 15, yIndex[192] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[193] - 15, yIndex[193] - 6, xIndex[193] + 15, yIndex[193] + 6)
    board.paste(trakList[t], area)

def perthToBunbury():
    area = (xIndex[194] - 15, yIndex[194] - 6, xIndex[194] + 15, yIndex[194] + 6)
    board.paste(trakList[t], area)

def perthToMtMagnet():
    area = (xIndex[195] - 15, yIndex[195] - 6, xIndex[195] + 15, yIndex[195] + 6)
    board.paste(trakList[t], area)
    area = (xIndex[196] - 15, yIndex[196] - 6, xIndex[196] + 15, yIndex[196] + 6)
    board.paste(trakList[t], area)

#if 1 == 1:
#    t=player1Colour
#    capeYToWeipa()

#p=0

#def playerTurn(player,a):
#    if (player,a) == 1:
#        t = player1Colour
#    elif (player,a) == 2:
#        t = player2Colour
#    elif (player,a) == 3:
#        t = player3Colour
#    elif (player,a) == 4:
#        t = player4Colour
#    elif (player,a) == 5:
#        t = player5Colour
#    else:
#        t == player6Colour
#    return t

#def claimRoute():
#    turn = playerList[p]
#    t=1
#    playerTurn(player,1)
capeYToWeipa()

board.show()
