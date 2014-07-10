# gives list of sources with no data in 6dF, SDSS or FAST at time of paper publication


import math
import sys

f = open("2mrs_1175_done.dat",'r')
g = open("fast-ref.out",'w')
q = open("nospec.out", 'w')

q.write("#List of sources with no 6dF, SDSS or Fast data as of paper publication.Output of getnednospec.py, will be modified against our list of 6dF and SDSS data\n")

for i in range(10):
    f.next()
    i +=1

#ref = []
#ref_count = []

count = 0
FLWO = 0
CTIO = 0
McDo = 0
JPH = 0
MMT = 0
ZMA = 0
DaSt = 0
JRM = 0
ORS = 0
SAAO = 0
ThWB = 0

for line in f:
    data = line.split()
    if data[26] != "S" and data[26] != "6" and data[26]!= "F":
        q.write("%s %s %s %f %s\n" %(data[0], data[1], data[2], float(data[24])/300000, data[26]))
    if data[27].find('FLWO') != -1:
        FLWO += 1 
        g.write("%s %s %s %f %s %s\n" %(data[0], data[1], data[2], float(data[24])/300000, data[26], data[27]))
    elif data[27].find('CTIO') != -1:
        CTIO += 1
        g.write("%s %s %s %f %s %s\n" %(data[0], data[1], data[2], float(data[24])/300000, data[26], data[27]))
    elif data[27].find('McDo') != -1:
        McDo += 1
        g.write("%s %s %s %f %s %s\n" %(data[0], data[1], data[2], float(data[24])/300000, data[26], data[27]))
    elif data[27].find('JPH') != -1:
        JPH += 1
        g.write("%s %s %s %f %s %s\n" %(data[0], data[1], data[2], float(data[24])/300000, data[26], data[27]))
    elif data[27].find('MMT') != -1:
        MMT += 1
        g.write("%s %s %s %f %s %s\n" %(data[0], data[1], data[2], float(data[24])/300000, data[26], data[27]))
    elif data[27].find('ZMA') != -1:
        ZMA += 1
        g.write("%s %s %s %f %s %s\n" %(data[0], data[1], data[2], float(data[24])/300000, data[26], data[27]))
    elif data[27].find('DaSt') != -1: 
        DaSt += 1
        g.write("%s %s %s %f %s %s\n" %(data[0], data[1], data[2], float(data[24])/300000, data[26], data[27]))
    elif data[27].find('JRM') != -1:
        JRM += 1
        g.write("%s %s %s %f %s %s\n" %(data[0], data[1], data[2], float(data[24])/300000, data[26], data[27]))
    elif data[27].find('ORS') != -1:
        ORS += 1
        g.write("%s %s %s %f %s %s\n" %(data[0], data[1], data[2], float(data[24])/300000, data[26], data[27]))
    elif data[27].find('SAAO') != -1:
        SAAO += 1
        g.write("%s %s %s %f %s %s\n" %(data[0], data[1], data[2], float(data[24])/300000, data[26], data[27]))
    elif data[27].find('ThWB') != -1:
        ThWB += 1
        g.write("%s %s %s %f %s %s\n" %(data[0], data[1], data[2], float(data[24])/300000, data[26], data[27]))
    count += 1
    

print "FLWO = %s\n" %(FLWO)
print "CTIO = %s\n" %(CTIO)
print "McDo = %s\n" %(McDo)
print "JPH = %s\n" %(JPH)
print "MMT = %s\n" %(MMT)
print "ZMA = %s\n" %(ZMA)
print "DaSt = %s\n" %(DaSt)
print "JRM = %s\n" %(JRM)
print "ORS = %s\n" %(ORS)
print "SAAO %s\n" %(SAAO)
print "ThWB = %s\n" %(ThWB)
print count

g.close()        
f.close()
q.close()