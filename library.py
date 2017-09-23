# coding: utf-8
def getVPIOL(input):
    return {
			'acetamide' : [125.81,-12376,-14.589,5.0824*10**-6,2],
			'acetic acid' : [53.27,-6304.5,-4.2985,8.8865*10**-18,6],
			'acetic anhydride' : [100.95,-8873.2,-11.451,6.1316*10**-6,2],
			'acetone' : [69.006,-5599.6,-7.0985,6.2237*10**-6,2],
			'acetonitrile' : [58.302,-5385.6,-5.4954,5.3634*10**-6,2],
			'acetylene'	: [39.63,-2552.2,-2.78,2.3930*10**-16,6],
			'acrolein' : [138.4,-7122.7,-19.638,2.6447*10**-2,1],
			'acrylic acid' : [46.745,-6587.1,-3.2208,5.2253*10**-7,2],
			'acrylonitrile' : [87.604,-6392.7,-10.101,1.0891*10**-5,2],
			'air' : [21.662,-692.39,-0.392,4.7574*10**-3,1],
			'ammonia' : [90.483,-4669.7,-11.607,1.7194*10**-2,1],
			'anisole' : [128.06,-9307.7,-16.693,1.4919*10**-2,1],
			'argon' : [42.127,-1093.1,-4.1425,5.7254*10**-5,2],
			'benzamide' : [85.474,-11932,-8.3348,1.2850*10**-18,6],
			'benzene' : [83.107,-6486.2,-9.2194,6.9844*10**-6,2],
			'benzenethiol' : [77.765,-8455.1,-7.7404,4.3089*10**-18,6],
			'benzoic acid' : [88.513,-11829,-8.6826,2.3248*10**-19,6],
			'benzonitrile' : [138.5,-11195,-17.085,9.5641*10**-6,2],
			'benzophenone' : [88.404,-11769,-8.9014,1.9334*10**-18,6],
			'benzyl alcohol' : [100.68,-11059,-10.709,3.0582*10**-18,6],
			'benzyl ethyl ether' : [68.541,-7886.2,-6.5804,2.4285*10**-6,2],
			'benzyl mercaptan' : [118.02,-10527,-13.91,6.4794*10**-6,2],
			'biphenyl' : [77.314,-9910.4,-7.5079,2.2385*10**-18,6],
			'bromine' : [108.26,-6592,-14.16,1.6043*10**-2,1],
			'bromobenzene' : [63.749,-7130.2,-5.879,5.2136*10**-18,6],
			'bromoethane' : [62.217,-5113.3,-5.9761,4.7174*10**-17,6],
			'bromomethane' : [72.586,-4698.6,-7.9966,1.1553*10**-5,2],
			'12 butadiene' : [39.714,-3769.9,-2.6407,6.9379*10**-18,6],
			'13 butadiene' : [75.572,-4621.9,-8.5323,1.2269*10**-5,2],
			'butane' : [66.343,-4363.2,-7.046,9.4509*10**-6,2],
			'12 butanediol' : [103.28,-11548,-10.925,4.2560*10**-18,6],
			'13 butanediol' : [123.22,-12620,-13.986,3.9260*10**-6,2],
			'1 butanol' : [106.295,-9866.4,-11.655,1.0832*10**-17,6],
			'2 butanol' : [114.68,-9850.2,-12.963,1.8738*10**-17,6],
			'1 butene' : [51.836,-4019.2,-4.5229,4.8833*10**-17,6],
			'cis 2 butene' : [72.541,-4691.2,-7.9776,1.0368*10**-5,2],
			'trans 2 butene' : [71.704,-4563.1,-7.9053,1.1319*10**-5,2],
			'butyl acetate' : [122.82,-9253.2,-14.99,1.0470*10**-5,2],
			'butylbenzene' : [101.22,-9255.4,-11.538,5.9208*10**-6,2],
			'butyl mercaptan' : [65.382,-6262.4,-6.2585,1.4943*10**-17,6],
			'sec butyl mercaptan' : [60.649,-5785.9,-5.6113,1.5877*10**-17,6],
			'1 butyne' : [77.004,-5054.5,-8.5665,1.0161*10**-5,2],
			'butyraldehyde' : [99.33,-7083.6,-11.733,1.0027*10**-5,2],
			'butyric acid' : [93.815,-9942.2,-9.8019,9.3124*10**-18,6],
			'butyronitrile' : [66.32,-6714.9,6.3087,1.3516*10**-17,6],
			'carbon dioxide' : [140.54,-4735,-21.268,4.0909*10**-2,1],
			'carbon disulfide' : [67.114,-4820.4,-7.5303,9.1695*10**-3,1],
			'carbon monoxide' : [45.698,-1076.6,-4.8814,7.5673*10**-5,2],
			'carbon tetrachloride' : [78.441,-6128.1,-8.5766,6.8465*10**-6,2],
			'carbon tetrafluoride' : [61.89,-2296.3,-7.086,3.4687*10**-5,2],
			'chlorine' : [71.334,-3855,-8.5171,1.2378*10**-2,1],
			'chlorobenzene' : [54.144,-6244.4,-4.5343,4.7030*10**-18,6],
			'chloroethane' : [65.988,-4661.3,-6.8586,7.9404*10**-6,2],
			'chloroform' : [146.43,-7792.3,-20.614,2.4578*10**-2,1],
			'chloromethane' : [64.697,-4048.1,-6.8066,1.0371*10**-5,2],
			'1 chloropropane' : [79.24,-5718.8,-8.789,8.4486*10**-6,2],
			'2 chloropropane' : [46.854,-4445.5,-3.6533,1.3260*10**-17,6],
			'm cresol' : [95.403,-10581,-10.004,4.3032*10**-18,6],
			'o cresol' : [210.88,-13928,-29.483,2.5182*10**-2,1],
			'p cresol' : [118.53,-11957,-13.293,8.6988*10**-18,6],
			'cumene' : [102.81,-8674.6,-11.922,7.0048*10**-6,2],
			'cyanogen' : [81.565,-4808.9,-9.3748,1.3901*10**-5,2],
			'cyclobutane' : [85.899,-4884.4,-10.883,1.4934*10**-2,1],
			'cyclohexane' : [51.087,-5226.4,-4.2278,9.7554*10**-18,6],
			'cyclohexanol' : [189.19,-14337,-24.148,1.0740*10**-5,2],
			'cyclohexanone' : [85.424,-7944.4,-9.2862,4.9957*10**-6,2],
			'cyclohexene' : [88.184,-6624.9,-10.059,8.2566*10**-6,2],
			'cyclopentane' : [66.341,-5198.5,-6.8103,6.1930*10**-6,2],
			'cyclopentene' : [67.952,-5187.5,-7.0785,6.8165*10**-6,2],
			'cyclopropane' : [40.608,-3179.6,-2.8937,5.6131*10**-17,6],
			'cyclohexyl mercaptan' : [85.146,-7843.7,-9.2982,5.1788*10**-6,2],
			'decanal' : [201.64,-15133,-26.264,1.4625*10**-5,2],
			'decane' : [112.73,-9749.6,-13.245,7.1266*10**-6,2],
			'decanoic acid': [123.36,-14680,-13.474,1.9491*10**-18,6],
			'1 decanol' : [156.239,-15212,-18.424,8.5006*10**-18,6],
			'1 decene' : [68.401,-7776.9,-6.4637,6.3750*10**-18,6],
			'decyl mercaptan' : [91.91,-10565,-9.5957,5.7028*10**-18,6],
			'1 decyne' : [142.94,-11119,-17.818,1.1020*10**-5,2],
			'deuterium' : [18.947,-154.47,-0.5723,3.8899*10**-2,1],
			'11 dibromoethane' : [62.711,-6503.5,-5.7669,1.0427*10**-6,2],
			'12 dibromoethane' : [43.751,-5587.7,-3.0891,8.2664*10**-7,2],
			'dibromomethane' : [86.295,-7010.3,-9.5972,6.7794*10**-6,2],
			'dibutyl ether' : [72.227,-7537.6,-7.0596,9.1442*10**-18,6],
			'm dichlorobenzene' : [53.187,-6827.5,-4.3233,2.3112*10**-18,6],
			'o dichlorobenzene' : [77.105,-8111.1,-7.8886,2.7267*10**-6,2],
			'p dichlorobenzene' : [88.31,-8463.4,-9.6308,4.5833*10**-6,2],
			'11 dichloroethane' : [66.611,-5493.1,-6.7301,5.3579*10**-6,2],
			'12 dichloroethane' : [92.355,-6920.4,-10.651,9.1426*10**-6,2],
			'dichloromethane' : [101.6,-6541.6,-12.247,1.2311*10**-5,2],
			'11 dichloropropane' : [83.495,-6661.4,-9.2386,6.7652*10**-6,2],
			'12 dichloropropane' : [65.955,-6015.6,-6.5509,4.3172*10**-6,2],
			'diethanol amine' : [106.38,-13714,-11.06,3.2645*10**-18,6],
			'diethyl amine' : [49.314,-4949,-3.9256,9.1978*10**-18,6],
			'diethyl ether'	: [136.9,-6954.3,-19.254,2.4508*10**-2,1],
			'diethyl sulfide' : [46.705,-5177.4,-3.5985,1.7147*10**-6,2],
			'11 difluoroethane' : [73.491,-4385.9,-8.1851,1.2978*10**-5,2],
			'12 difluoroethane' : [84.625,-5217.4,-9.871,1.3050*10**-5,2],
			'difluoromethane' : [69.132,-3847.7,-7.5868,1.5065*10**-5,2],
			'di isopropyl amine' : [462.84,-18227,-73.734,9.2794*10**-2,1],
			'di isopropyl ether' : [41.631,-4668.7,-2.8551,6.3693*10**-4,1],
			'di isopropyl ketone' : [50.868,-6036.5,-4.066,1.1326*10**-6,2],
			'11 dimethoxyethane' : [53.637,-5251.2,-4.5649,1.675*10**-17,6],
			'12 dimethoxypropane' : [62.097,-6174.9,-5.715,1.2323*10**-17,6],
			'dimethyl acetylene' : [66.592,-4999.8,-6.8387,6.6793*10**-6,2],
			'dimethyl amine' : [71.738,-5302,-7.3324,6.4200*10**-17,6],
			'23 dimethylbutane' : [77.161,-5691.1,-5.501,8.0325*10**-6,2],
			'11 dimethylcyclohexane' : [81.184,-6927,-8.8498,5.4580*10**-6,2],
			'cis 12 dimethylcyclohexane' : [78.952,-7075.4,-8.4344,4.5035*10**-6,2],
			'trans 12 Dimethylcyclohexane'	: [78.429,-6882.1,-8.4129,4.9831*10**-6,2],
			'dimethyl disulfide' : [81.045,-6941.3,-8.777,5.5501*10**-6,2],
			'dimethyl ether' : [44.704,-3525.6,-3.4444,5.4574*10**-17,6],
			'nn dimethyl formamide' : [82.762,-7955.5,-8.8038,4.2431*10**-6,2],
			'23 dimethylpentane' : [78.335,-6348.7,-8.5105,6.4311*10**-6,2],
			'dimethyl phthalate' : [72.517,-10415,-6.755,1.3269*10**-6,2],
			'dimethylsilane' : [63.08,-4062.3,-6.425,1.5115*10**-16,6],
			'dimethyl sulfide' : [84.39,-5740.6,-9.6454,1.0073*10**-5,2],
			'dimethyl sulfoxide' : [56.273,-7620.6,-4.6279,4.3819*10**-7,2],
			'dimethyl terephthalate' : [43.541,-8204.8,-2.7519,1.0466*10**-18,6],
			'14 dioxane' : [44.494,-5406.7,-3.1287,2.8913*10**-18,6],
			'diphenyl ether' : [59.969,-8585.5,-5.1538,1.9983*10**-18,6],	
			'dipropyl amine' : [54,-6018.5,-4.4981,9.9684*10**-18,6],
			'dodecane' : [137.47,-11976,-16.698,8.0906*10**-6,2],
			'eicosane' : [203.66,-19441,-25.525,8.8382*10**-6,2],
			'ethane' : [51.857,-2598.7,-5.1283,1.4913*10**-5,2],
			'ethanol' : [73.304,-7122.3,-7.1424,2.8853*10**-6,2],
			'ethyl acetate'	: [66.824,-6227.6,-6.41,1.7914*10**-17,6],
			'ethyl amine' : [81.56,-5596.9,-9.0779,8.7920*10**-6,2],
			'ethylbenzene' : [59.063,-7733.7,-9.917,5.9860*10**-6,2],
			'ethyl benzoate' : [52.923,-7531.7,-4.2347,1.1835*10**-6,2],
			'2 ethyl butanoic acid'	: [90.464,-10243,-9.2836,5.2573*10**-18,6],
			'ethyl butyrate' : [57.661,-6346.5,-5.032,8.2534*10**-18,6],
			'ethylcyclohexane' : [80.208,-7203.2,-8.6023,4.5901*10**-6,2],
			'ethylcyclopentane'	: [88.671,-7012.7,-10.045,7.4578*10**-6,2],
			'ethylene' : [53.963,-2443,-5.5643,1.9079*10**-5,2],
			'ethylenediamine' : [73.51,-7572.7,-7.1435,1.2124*10**-17,6],
			'ethylene glycol' : [84.09,-10411,-8.1976,1.6536*10**-18,6],
			'ethyleneimine'	: [66.51,-6019.2,-6.3332,1.0394*10**-17,6],
			'ethylene oxide' : [91.944,-52923.4,-11.682,1.4902*10**-2,1],
			'ethylene formate' : [73.833,-5817,-7.809,6.3200*10**-6,2],
			'2 ethyl hexanoic acid'	: [117.52,-12991,-12.895,6.1306*10**-18,6],
			'ethylhexyl ether' : [77.523,-7978.8,-7.7757,1.0076*10**-17,6],
			'ethylisopropyl ether' : [57.723,-5236.9,-5.2136,2.2998*10**-17,6],
			'ethylisopropyl ketone'	: [57.459,-6356.8,-4.9545,5.2015*10**-18,6],
			'ethyl mercaptan' : [65.551,-5027.4,-6.6853,6.3208*10**-6,2],
			'ethyl propionate' : [105.64,-8007,-12.477,9.0000*10**-6,2],
			'ethylpropyl ether'	: [86.898,-6646.4,-9.5758,5.9615*10**-17,6],
			'ethyltrichlorosilane' : [62.614,-6148.2,-5.84,1.0900*10**-17,6],
			'fluorine' : [42.393,-1103.3,-4.1203,5.7815*10**-5,2],
			'fluorobenzene'	: [51.915,-5439,-4.2896,8.7527*10**-18,6],
			'fluoroethane' : [56.639,-3576.5,-5.5801,9.8969*10**-6,2],
			'fluoromethane'	: [59.123,-3043.7,-4.1845,1.6637*10**-5,2],
			'formaldehyde' : [101.51,-4917.2,-13.765,2.2031*10**-2,1],
			'formamide'	: [100.3,-10763,-10.946,3.8503*10**-6,2],
			'formic acid' : [50.323,-5378.2,-4.203,3.4697*10**-6,2],
			'furan'	: [74.738,-5417,-8.0636,7.4700*10**-6,2],
			'helium 4' : [11.533,-8.99,0.6724,2.7430*10**-1,1],
			'heptadecane' : [156.95,-15557,-18.966,6.4559*10**-6,2],
			'heptanal' : [92.252,-8349,-10.274,5.9252*10**-6,2],
			'heptane' : [87.829,-6996.4,-8.8802,7.2099*10**-6,2],
			'heptanoic acid' : [120.47,-13106,-13.31,5.8384*10**-18,6],
			'1 heptanol' : [147.41,-13466,-17.353,1.1284*10**-17,6],
			'2 heptanol' : [124.23,-11637,-14.148,6.9486*10**-17,5.7],
			'3 heptanone' : [78.463,-8077.2,-7.9062,8.0521*10**-18,6],
			'2 heptanone' : [75.494,-7896.5,-7.5047,8.9130*10**-18,6],
			'1 heptene'	: [65.922,-6189,-6.3629,2.0091*10**-17,6],
			'heptyl mercaptan' : [79.858,-8501.8,-8.1043,8.1501*10**-18,6],
			'1 heptyne'	: [59.083,-6031.8,-5.3072,1.4357*10**-17,6],
			'hexadecane' : [156.06,-15015,-18.941,6.8172*10**-6,6],
			'hexanal' : [81.507,-7776.8,-8.4516,1.15143*10**-17,2],
			'hexane' : [104.65,-6995.5,-12.702,1.2381*10**-5,6],
			'hexanoic acid'	: [114.05,-12332,-12.45,5.6253*10**-18,2],
			'1 hexanol'	: [135.421,-12288,-15.732,1.2701*10**-17,6],
			'2 hexanol'	: [109.42,-10449,-12.051,2.6122*10**-46,6],
			'2 hexanone' : [107.44,-8258.6,-12.679,8.4606*10**-6,16],
			'3 hexanone' : [73.155,-7242.9,-7.2569,1.2741*10**-17,2],
			'1 hexene' : [51.024,-4986.4,-4.2463,1.6768*10**-17,6],
			'3 hexyne' : [47.091,-5104,-3.6371,5.1621*10**-4,6],
			'hexyl mercaptan' : [68.467,-7390.5,-6.5456,7.7611*10**-18,1],
			'1 hexyne' : [133.2,-7492.9,-18.405,2.2062*10**-2,6],
			'2 hexyne' : [133.71,-7639,-16.451,1.6495*10**-2,1],
			'hydrazine'	: [76.858,-7245.2,-8.22,6.1557*10**-3,1],
			'hydrogen' : [12.69,-94.896,-1.1125,3.2915*10**-4,2],
			'hydrogen bromide' : [29.315,-2424.5,-1.1354,2.3806*10**-18,6],
			'hydrogen chloride'	: [104.27,-3731.2,-15.047,3.1340*10**-2,1],
			'hydrogen cyanide' : [36.75,-3927.1,-2.1245,3.8948*10**-17,6],
			'hydrogen fluoride'	: [59.544,-4143.8,-6.1764,1.4161*10**-5,2],
			'hydrogen sulfide' : [85.584,-3839.9,-11.199,1.8848*10**-2,1],
			'isobutyric acid' : [110.38,-10540,-12.262,1.4310*10**-17,6],
			'isopropyl amine' : [136.66,-7201.5,-18.934,2.2255*10**-2,1],
			'malonic acid'	: [122.92,-16258,-13.113,2.0609*10**-18,6],
			'methacrylic acid' : [109.53,-10410,-12.289,3.1990*10**-6,2],
			'methane' : [39.205,-1324.4,-3.4366,3.1019*10**-5,2],
			'methanol' : [82.718,-6904.5,-8.8622,7.4664*10**-6,2],
			'n methyl acetamide' : [79.128,-9523.9,-7.7355,3.1616*10**-18,6],
			'methyl acetate' : [61.267,-5618.6,-5.6473,2.1080*10**-17,6],
			'methyl acetylene' : [50.242,-3811.9,-4.2526,6.5326*10**-17,6],
			'methyl acrylate' : [107.69,-7027.2,-13.916,1.5185*10**-2,1],
			'methyl amine' : [75.206,-5082.8,-8.0919,8.1130*10**-6,2],
			'methyl benzoate' : [84.828,-9334.7,-8.7063,6.1723*10**-18,6],
			'3 methyl 12 butadiene' : [66.575,-5213.4,-6.7693,4.8106*10**-6,2],
			'2 methylbutane' : [71.308,-4976,-7.7169,8.7271*10**-6,2],
			'2 methylbutanoic acid' : [85.383,-9575.4,-8.6164,5.6124*10**-18,6],
			'3 methyl 1 butanol' : [121.85,-10976,-13869,1.4283*10**-17,6],
			'2 methyl 1 butene'	: [93.131,-5525.4,-11.852,1.4205*10**-2,1],
			'2 methyl 2 butene'	: [83.927,-5640.5,-9.6453,1.1121*10**-5,2],
			'2 methyl 1 butene 3 yne' : [95.453,-5448.8,-12.384,1.5643*10**-2,1],
			'methylbutyl ether'	: [60.164,-5621.7,-5.53,1.8629*10**-17,6],
			'methylbutyl sulfide' : [96.344,-7856.3,-11.058,7.3080*10**-6,2],
			'3 methyl 1 butyne'	: [69.459,-5250,-7.1125,7.9289*10**-17,6],
			'methyl butyrate' : [71.87,	-6885.7,-7.0944,1.4903*10**-17,6],
			'methylchlorosilane' : [95.984,-5401.7,-11.829,1.8092*10**-5,2],
			'methylcyclohexane'	: [92.684,-7080.8,-10.695,8.1366*10**-6,2],
			'1 methylcyclohexanol' : [134.63,-10682,-16.511,8.4427*10**-6,2],
			'cis 2 methylcyclohexanol' : [125.1,-10288,-15.157,1.0918*10**-5,2],
			'trans 2 methylcyclohexanol' : [54.179,-7477.2,-4.22,3.5225*10**-18,6],
			'methylcyclopentane' : [55.368,-5149.8,-5.0136,3.2220*10**-6,2],
			'1 methycyclopentene' : [52.732,-5286.9,-4.4509,1.0883*10**-17,6],
			'3 methylcyclopentene' : [52.601,-5120.3,-4.4554,1.3288*10**-17,6],
			'methyldichlorosilane'	: [79.788,-5420,-9.0702,1.1489*10**-5,2],
			'methylethyl ether'	: [78.586,-5176.3,-8.7501,9.1727*10**-6,2],
			'methylethyl ketone' : [72.698,-6143.6,-7.5779,5.6476*10**-6,2],
			'methylethyl sulfide' : [79.07,-6114.1,-8.631,6.5333*10**-6,2],
			'methyl formate' : [77.184,-5606.1,-8.392,7.8468*10**-6,2],
			'methylisobutyl ether' : [57.984,-5339.6,-5.2362,2.0767*10**-17,6],
			'methylisobutyl ketone'	: [80.503,-7421.8,-8.379,1.8114*10**-17,6],
			'methyl isocyanate'	: [57.612,-5197.9,-5.1269,2.1702*10**-17,6],
			'methylisopropyl ether'	: [53.867,-4701,-4.7052,2.8791*10**-17,6],
			'methylisopropyl ketone' : [45.242,-5324.4,-3.2551,3.0363*10**-18,6],
			'methylisopropyl sulfide' : [52.82,-5437.7,-4.442,9.5103*10**-18,6],
			'methyl mercaptan' : [54.15,-4337.7,-4.8127,4.5000*10**-17,6],
			'methyl methacrylate' : [107.36,-8085.3,-12.72,8.3307*10**-6,2],
			'2 methyloctanoic acid'	: [105.7,-12458,-11.234,4.4629*10**-18,6],
			'2 methylpentane' : [53.579,-5041.2,-4.6404,1.9443*10**-17,6],
			'methyl pentyl ether' : [61.907,-6188.9,-5.706,1.1767*10**-17,6],
			'2 methylpropane' : [108.43,-5039.9,-15.012,2.2725*10**-2,1],
			'2 methyl 2 propanol' : [172.27,-11589,	-22.113,1.3703*10**-5,2],
			'2 methyl propene' : [78.01,-4634.1,-8.9575,1.3413*10**-5,2],
			'methyl propionate'	: [70.717,-6439.7,-6.9845,2.0129*10**-17,6],
			'methylpropyl ether' : [67.942,-5419.1,-6.8067,4.7778*10**-17,6],
			'methylpropyl sulfide' : [83.711,-6786.9,-9.2526,6.6666*10**-6,2],
			'methylsilane' : [37.205,-2590.3,-2.5993,6.0508*10**-6,2],
			'a methyl styrene'	: [56.485,-6954.2,-4.7889,2.7753*10**-18,6],
			'methyl tert butyl ether' : [57.1511,-5201.7,-5.1429,1.6529*10**-17,6],
			'methyl vinyl ether' : [51.085,-4271,-4.307,3.0530*10**-17,6],
			'napthalene' : [62.964,-8137.5,-5.6317,2.2675*10**-18,6],
			'neon' : [29.755,-271.06,-2.6081,5.2700*10**-4,2],
			'nitroethane' : [75.632,-7202.3,-7.6464,1.8250*10**-17,6],
			'nitrogen' : [58.282,-1084.1,-8.3144,4.4127*10**-2,1],
			'nitrogen trifluoride' : [68.149,-2257.9,-8.9118,2.3233*10**-2,1],
			'nitromethane' : [57.278,-6089,-4.9821,1.2154*10**-17,6],
			'nitrous oxide'	: [96.512,-4045,-12.277,2.8860*10**-5,2],
			'nitric oxide' : [72.974,-2650,-8.261,9.7000*10**-15,6],
			'nonadecane' : [182.54,-17897,-22.498,7.4008*10**-6,2],
			'nonanal' : [337.71,-18506,-50.224,4.7345*10**-2,1],
			'nonane' : [109.35,-9030.4,-12.882,7.8544*10**-6,2],
			'nonanoic acid' : [137.6,-14948,-15.618,5.5660*10**-18,6],
			'1 nonanol'	: [162.854,-15205,-19.424,1.0722*10**-17,6],
			'2 nonanol'	: [146.46,-13813,-17.158,8.6279*10**-40,14],
			'1 nonene' : [63.313,-7040.4,-5.8055,7.5753*10**-18,6],
			'nonyl mercaptan' : [106.2,-10982,-11.696,8.8955*10**-18,6],
			'1 nonyne' : [114.77,-9430.8,-13.631,8.1918*10**-6,2],		
			'octadecane' : [157.68,-16093,-18.954,5.9272*10**-6,2],
			'octanal' : [83.601,-8865.8,-8.5711,7.9446*10**-18,6],
			'octane' : [96.084,-7900.2,-11.003,7.1802*10**-6,2],
			'octanoic acid'	: [140.16,-14813,-16.004,6.4239*10**-18,6],
			'1 octanol'	: [144.111,-13667,-16.826,9.3666*10**-18,6],
			'2 octanol'	: [133.41,-12630,-15.369,2.9939*10**-41,14],
			'2 octanone' : [63.775,-7711.3,-5.7359,3.0902*10**-18,6],
			'3 octanone' : [72.382,-8054.8,-7.0002,5.8276*10**-18,6],
			'1 octene' : [74.936,-7155.9,-7.5843,1.7106*10**-17,6],
			'octyl mercaptan' : [78.368,-8855.4,-7.8202,5.6629*10**-18,6],
			'1 octyne' : [64.612,-6802.5,-6.0261,1.1013*10**-17,6],
			'oxalic acid' : [122.04,-16050,-12.986,2.0871*10**-18,6],
			'oxygen' : [51.245,-1200.2,-6.4361,2.8405*10**-2,1],
			'ozone'	: [40.067,-2204.8,-2.9351,7.7520*10**-16,6],
			'pentadecane' : [135.57,-13478,-16.022,5.6136*10**-6,2],
			'pentanal' : [149.58,-8890,-20.697,2.2101*10**-2,1],
			'pentane' : [78.741,-5420.3,-8.8253,9.6171*10**-6,2],
			'pentanoic acid' : [101.7,-10955,-10.829,7.1880*10**-18,6],
			'1 pentanol' : [114.748,-10643,-12.858,1.2491*10**-17,6],
			'2 pentanol' : [122.26,-10774,-13.943,1.0700*10**-42,15],
			'2 pentanone' : [84.635,-7078.4,-9.3,6.2702*10**-6,2],
			'3 pentanone' : [44.286,-5415.1,-3.0913,1.8580*10**-18,6],
			'1 pentene'	: [46.994,-4289.5,-3.7345,2.5424*10**-17,6],
			'2 pentyl mercaptan' : [58.985,-6193.1,-5.2746,7.3986*10**-18,6],
			'pentyl mercaptan' : [67.309,-6880.8,-6.4449,1.0148*10**-17,6],
			'1 pentyne'	: [82.805,-5683.8,-9.4301,1.0767*10**-5,2],
			'2 pentyne'	: [137.29,-7447.1,-19.01,2.1415*10**-2,1],
			'phenanthrene' : [72.958,-10943,-6.7902,1.0850*10**-18,6],
			'phenol' : [95.444,-10113,-10.09,6.7603*10**-18,6],
			'phenyl isocyanate'	: [86.779,-8101.8,-9.5303,6.1367*10**-6,2],
			'phthalic anhydride' : [126.5,-12551,-15.002,7.7521*10**-6,2],
			'propadiene' : [57.069,-3682.7,-5.5662,6.5133*10**-6,2],
			'propane' : [59.078,-3492.6,-6.0669,1.0919*10**-5,2],
			'1 propanol' : [84.6642,-8307.2,-8.5767,7.5091*10**-18,6],
			'2 propanol' : [96.094,-8575.4,-10.292,1.6665*10**-17,6],
			'propenylcyclohexane' : [64.268,-7298.9,-5.9109,4.8482*10**-18,6],
			'propionaldehyde' : [80.581,-5896.1,-8.9301,8.2236*10**-6,2],
			'propionic acid' : [54.552,-7149.4,-4.2769,1.1843*10**-18,6],
			'propionitrile'	: [82.699,-6703.5,-9.1506,7.5424*10**-6,2],
			'propyl acetate' : [115.16,-8433.9,-13.934,1.0346*10**-5,2],
			'propyl amine' : [58.398,-5312.7,-5.2876,1.9913*10**-6,2],
			'propylbenzene'	: [91.379,-8276.8,-10.176,5.6240*10**-6,2],
			'propylene'	: [43.905,-3097.8,-3.4425,9.9989*10**-17,6],
			'propyl formate' : [104.08,-7535.9,-12.348,9.6020*10**-6,2],
			'2 propyl mercaptan' : [60.43,-5276.9,-5.6572,2.6039*10**-17,6],
			'propyl mercaptan' : [62.165,-5624,-5.8595,2.0597*10**-17,6],
			'1,2 propylene glycol' : [212.8,-15420,-28.109,2.1564*10**-5,2],
			'quinone' : [48.651,-7289.5,-3.4453,1.0068*10**-18,6],
			'silicon tetrafluoride'	: [272.85,-9548.9,-40.089,6.3699*10**-15,6],
			'styrenen' : [105.93,-8685.9,-12.42,7.5583*10**-6,2],
			'succinic acid'	: [128.65,-16958,-13.872,2.1559*10**-18,6],
			'sulfur dioxide' : [47.365,-4084.5,-3.6469,1.7990*10**-17,6],
			'sulfur hexafluoride' : [29.16,-2383.6,-1.1342,0,0],
			'sulfur trioxide' : [180.99,-12060,-22.839,7.2350*10**-17,6],
			'terephthalic acid'	: [248.72,-32238,-30.009,4.7950*10**-6,2],
			'o terphenyl' : [110.52,-14045,-11.861,2.2121*10**-18,6],
			'tetradecane' : [140.47,-13231,-16.859,6.5877*10**-6,2],
			'tetrahydrofuran' : [54.898,-5305.4,-4.7627,1.4291*10**-17,6],
			'1234 tetrahydronaphthalene'	: [137.23,-10620,-17.908,1.4506*10**-2,1],
			'tetrahydrothiphene' : [75.881,-6910.6,-7.9499,4.4315*10**-6,2],
			'2233 tetramethyl butane' : [57.963,-5901.5,-5.2048,9.1301*10**-18,6],
			'thiophene'	: [93.193,-7001.5,-10.738,8.2308*10**-6,2],
			'toluene' : [76.945,-6729.8,-8.179,5.3017*10**-6,2],
			'112 trichloroethane'	: [54.153,-6041.8,-4.5383,4.9833*10**-18,6],
			'tridecane'	: [137.45,-12549,-16.543,7.1275*10**-6,2],
			'triethyl amine' : [56.55,-5681.9,-4.9815,1.2363*10**-17,6],
			'trimethyl amine' : [134.68,-6055.8,-19.415,2.8619*10**-2,1],
			'123 trimethylbenzene' : [78.341,-8019.8,-8.1458,3.8671*10**-6,2],
			'124 trimethylbenzene' : [85.301,-8215.9,-9.2166,4.7979*10**-6,2],
			'224 trimethylpentane' : [84.912,-6722.2,-9.5157,7.2244*10**-6,2],
			'233 trimethylpentane' : [83.105,-6903.7,-9.1858,6.4703*10**-6,2],
			'135 trinitrobenzene'	: [506.33,-37483,-69.22,2.7381*10**-5,2],
			'246 trinitrotoluene'	: [302,-24324,-40.13,1.7403*10**-5,2],
			'undecane' : [131,-11143,-15.855,8.1871*10**-6,2],
			'1 undecanol' : [182.571,-17112,-22.125,1.12835*10**-17,6],
			'vinyl acetate'	: [57.406,-5702.8,-5.0307,1.1042*10**-17,6],
			'vinyl acetylene' : [55.682,-4439.3,-5.0136,1.9650*10**-17,6],
			'vinyl chloride' : [91.432,-5141.7,-10.981,1.4318*10**-5,2],
			'vinyl trichlorosilane'	: [54.571,-5561.5,-4.712,1.0702*10**-17,6],
			'water'	: [73.649,-7258.2,-7.3037,4.1653*10**-6,2],
			'm xylene' : [85.099,-7615.9,-9.3072,5.5643*10**-6,2],
			'o xylene' : [90.405,-7955.2,-10.086,5.9594*10**-6,2],
			'p xylene' : [88.72,-7741.2,-9.8693,6.0770*10**-6,2],


    }.get(input)  # add new parameter if input not found

# print(getVPIOL('Acetamide')[0:])