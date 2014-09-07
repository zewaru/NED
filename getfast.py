#find ../../data/* -name "*.fits" > alldata
#deleted bunch of test and continuum subtracted files from list
# version 2 on github, added use of dictionary instead of multiple lists while reading from fits files.

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

a = open("Fast_available.dat", 'w')
b = open("Fast_data_needed.dat", 'w')
c = open("Fast_data_notneeded.dat",'w')
    
g.write("#Fast sources collected from the 2mrs_1175_done.dat. Output of getfast.py\n")

for i in range(10):
    f.next()
    i +=1

Coord_RA = []
Coord_Dec = []
source = []
zvel = []
origin = []

d = {}



telescope = ['F', 'C', 'O', 'D']

i = 0

for line in f:
    data = line.split()
    if data[26] in telescope:
        d[str(i)] = [data[0], trunc(float(data[1]), 5), trunc(float(data[2]),5), float(data[24]), data[26]]
        source.append(data[0])
        Coord_RA.append(trunc(float(data[1]), 5))
        Coord_Dec.append(trunc(float(data[2]),5))
        zvel.append(float(data[24]))
        origin.append(data[26])
        h.write("%s %s %f\n" %(data[1], data[2], float(data[24])/300000 + 1))
        g.write("2MASSXJ%s \n" %(data[0]))
        i += 1
#print Coord_RA[0], Coord_Dec[0]
#print type(Coord_RA[0]), type(Coord_Dec[0])
print len(d)

observed = []

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
        ra_deg = float(ra_ha[0]) * 360 /24 + float(ra_ha[1]) * 360 / 24 /60 + float(ra_ha[2]) /3600 * 360/ 24
        dec = hdu[0].header['DEC']
        dec_ha = dec.split(':')
        dec_deg = float(dec_ha[0]) + float(dec_ha[1]) / 60 + float(dec_ha[2]) /3600
        velocity = hdu[0].header['VELOCITY']
    ra_trunc = trunc(ra_deg, 5)
    dec_trunc = trunc(dec_deg, 5)
    for i in range(0, len(d)):
        angdist.append(angulardistance(ra_deg, dec_deg, d[str(i)][1], d[str(i)][2] ))
#        angdist.append(angulardistance(ra_deg, dec_deg, Coord_RA[i], Coord_Dec[i]))

    maxang = max(angdist)
    j = angdist.index(maxang)

    if trunc(maxang,3) == 1.000:
        dist_arcsec = 0
    else:
        dist = math.degrees(math.acos(float(maxang)))
        dist_arcsec = dist * 3600

    if dist_arcsec <= 5 and math.fabs(d[str(j)][3] - velocity) <= 50 : 
        k += 1
        a.write("%s %s %s %s %s %s %s %s \n" %(path, dist_arcsec, ra, dec, ra_deg, dec_deg, d[str(j)], data[26]))
        observed.append(d[str(j)][0])
    else:
        q += 1

for i in range(0, len(observed)):
    if observed[i] not in source:
	print i
 
for i in range(0, len(source)):
    if source[i] not in observed:
	# 6386
        b.write("%s %s %s %s %s\n" %(source[i], Coord_RA[i], Coord_Dec[i], zvel[i], origin[i]))
    elif source[i] in observed:
	# 5363
	c.write("%s %s %s %s %s\n" %(source[i], Coord_RA[i], Coord_Dec[i], zvel[i], origin[i]))
    else:
	print "shiiiiiiit " + i + " " + source[i]

print len(source) # 11749
print len(observed) # 5731

#print len(Coord_RA), len(Coord_Dec)
print k, q

c.close()
a.close()
b.close()
g.close()
f.close()
h.close()
