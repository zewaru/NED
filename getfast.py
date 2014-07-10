#find ../../data/* -name "*.fits" > alldata
#deleted bunch of test and continuum subtracted files from list

import math
import sys
import pyfits

def trunc(item,n):
    if type(item) is float:
        slen = len('%.*f' %(n, item)) #rounds coordinate to n decimals, measures length
        stritem = str(item)[:slen] # truncates coordinate so that n decimals are included
        return float(stritem)
    elif type(item) is str:
        return str(item)[:n] # truncates coord to length n

def angulardistance(x, y, a, b):
    return math.sin(math.radians(y)) * math.sin(math.radians(b)) + math.cos(math.radians(y)) * math.cos(math.radians(b)) * math.cos(math.radians(a-x))

f = open("2mrs_1175_done.dat",'r')

filelist = open("alldata",'r')

g = open("Fast-2MASSXJ.dat",'w')

h = open("Fast-id.dat", 'w')

g.write("#Fast sources collected from the 2mrs_1175_done.dat. Output of getfast.py\n")

for i in range(10):
    f.next()
    i +=1

Coord_RA = []
Coord_Dec = []
source = []
zvel = []

for line in f:
    data = line.split()
    source.append(data[0])
    Coord_RA.append(trunc(float(data[1]), 5))
    Coord_Dec.append(trunc(float(data[2]),5))
    zvel.append(float(data[24]))
    if data[26] == "F" :
        h.write("%s %s %f\n" %(data[1], data[2], float(data[24])/300000 + 1))
        g.write("2MASSXJ%s \n" %(data[0]))

#print Coord_RA[0], Coord_Dec[0]
#print type(Coord_RA[0]), type(Coord_Dec[0])

k = 0
q = 0
i = 0
for line in filelist:
    path = line.strip()
    angdist = []
    with pyfits.open(path) as hdu:
        name = hdu[0].header['OBJECT']
        observatory = hdu[0].header['OBSERVAT']
        ra = hdu[0].header['RA']
        ra_ha =ra.split(':')
        ra_deg = float(ra_ha[0]) *360 /24 + float(ra_ha[1]) * 360 / 24 /60 + float(ra_ha[2]) /3600 * 360/ 24
        dec = hdu[0].header['DEC']
        dec_ha = dec.split(':')
        dec_deg = float(dec_ha[0]) + float(dec_ha[1]) / 60 + float(dec_ha[2]) /3600
        velocity = hdu[0].header['VELOCITY']
    ra_trunc = trunc(ra_deg, 5)
    dec_trunc = trunc(dec_deg, 5)
#    print ra_trunc, dec_trunc
#    print type(ra_trunc), type(dec_trunc)
    for i in range(0, len(Coord_RA)):
        angdist.append(angulardistance(ra_deg, dec_deg, Coord_RA[i], Coord_Dec[i]))
#        if angdist <= 0.1:
#            print source[i], Coord_RA[i], Coord_Dec[i], path, ra, dec
    maxang = max(angdist)
#    print len(angdist), len(Coord_RA)
    j = angdist.index(maxang)
#    print j
    if trunc(maxang,3) == 1.000:
        dist_arcsec = 0
    else:
        dist = math.degrees(math.acos(float(maxang)))
        dist_arcsec = dist * 3600
    if dist_arcsec <= 10 and math.fabs(zvel[j] - velocity) <= 100 : 
        print path, dist_arcsec, ra, dec, ra_deg, dec_deg, source[j], Coord_RA[j], Coord_Dec[j], zvel[j]- velocity, data[26]
        k += 1
    else:
        print path, dist_arcsec 
        q += 1
    

#print len(Coord_RA), len(Coord_Dec)
print k, q

g.close()
f.close()
h.close()
