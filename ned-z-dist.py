# histograms for various purposes.
# for redshift cutoff, change upper limit in z in line 38 (?)
# to make histograms for redshift distribution for different telescopes
# change code for selection in line ()
# Ned-z-dist.out gives the list of sources with their coordinates and redshifts
# this should really come only from NED_references.out


import sys
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig

def zselect(z, n):
    if 0.00 <= z <= n:
        ydata.append(z)
    elif z <= 0.00:
        ydata.append(0.0001)


f = open("NED_references.out",'r')
g = open("Ned-z-dist.out",'w')
q = open("nospec.out", 'r')

detected = 0

ref = []
ref_count = []

n = 0.05
histbins = [0.001*i for i in range(0, int(n*1000))]


test = []

print len(histbins)
histo = [0] * len(histbins)
ydata = []

q.readline()
#f.readline()

for line in q:
    data = line.split()
#    z = float(data[3])/300000 
    z = float(data[3])
    g.write("%s %s %f\n" %(data[1], data[2], z + 1))
    zselect(z, n)
    if data[4] not in ref:
        ref.append(data[4])
        ref_list.write("%s \n" %(data[27]))
        ref_count.append(1)
    else:
        i = ref.index("%s" % (data[4]))
        ref_count[i] = ref_count[i] + 1


barp = plt.hist(ydata, bins = histbins)
savefig("z-hist.png")

print len(ydata)

g.close()
q.close()
f.close()