import fileinput
import operator

XuanPian = dict()

for line in fileinput.input():
    if (line == "\n"):
    	break
    templist = line.split()
    print templist
    diglist = [int(s) for s in templist if s.isdigit()]
    print diglist
    for ele in diglist:
		if (ele in XuanPian):
			XuanPian[ele] += 1
		else:
			XuanPian[ele] = 1
    print XuanPian

od = sorted(XuanPian.items(), key=operator.itemgetter(1))
od = od[-8:]
print ("Selection: {}").format(od[::-1])
