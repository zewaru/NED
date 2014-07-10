#get galaxies radio, xray, uvexcess, gamm, emission line and QSO from NED and 2MRS

import math

def trunc(item,n):
    if type(item) is float:
        slen = len('%.*f' %(n, item)) #rounds coordinate to n decimals, measures length
        return str(item)[:slen] # truncates coordinate so that n decimals are included
    elif type(item) is str:
        return str(item)[:n] # truncates coord to length n


f1 = open("result-QSO.txt", 'r')
f2 = open("result-emsl.txt", 'r')
f3 = open("result-gamma.txt",'r')
f4 = open("result-radio.txt",'r')
f5 = open("result-uvx.txt", 'r')
f6 = open("result-xray.txt",'r')

g1 = open("2mrs_1175_done.dat",'r')

g2 = open("NED-idz.dat",'r')
g2.readline()

o = open("ned-candidates.dat", 'w')
q = open("2mrs-candidates.dat", 'w')

ned_ra= []
ned_dec = []
mrs_ra = []
mrs_dec= []

ned_cand = []
mrs_cand = []

for i in range(10):
    g1.next()
    i +=1
    
for line in g2:
    column = line.split()
    ned_ra.append(trunc(float(column[1]),2))
    ned_dec.append(trunc(float(column[2]),2))

for line in g1:
    column = line.split()
    mrs_ra.append(trunc(float(column[1]),2))
    mrs_dec.append(trunc(float(column[2]),2))

files = [f1, f2, f3, f4, f5, f6]


for file in files:
    for i in range(26):
        file.next()
        i += 1
    for line in file:
        column = line.split( '|')
#        print column[2], column[3]
        ra_trunc = trunc(float(column[2]), 2)
        dec_trunc = trunc(float(column[3]), 2)
#        print ra_trunc, dec_trunc
        if float(column[6]) <= 0.05:
            if ra_trunc in ned_ra:
                if dec_trunc == ned_dec[ned_ra.index(ra_trunc)]:
                    if column[1] not in ned_cand:
                        ned_cand.append(column[1])
                        o.write("%s \n" %(column[1]))
            if ra_trunc in mrs_ra:
                if dec_trunc == mrs_dec[mrs_ra.index(ra_trunc)]:
                    if column[1] not in mrs_cand:
                        mrs_cand.append(column[1])
                        q.write("%s \n" %(column[1]))
    file.close()
            
q.close()
o.close()





