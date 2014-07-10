# transform ra and dec from degrees to hms, dms and arcmin

import math

f = open("NED-batch.dat",'r')
g = open("NED-batch.inp", 'w')

g.write("#output file from transform.py, formatted for NED batch jobs\n")

for line in f:
    coord = []
    data = line.split()
    rah = float(data[0]) * 24. /360
    h, m = divmod(rah, 1.)
    coord.append(h)
    p, q = divmod( m * 60., 1.)
    coord.append(p)
    coord.append(q * 60.)
    d, m = divmod(float(data[2]), 1.)
    coord.append(d)
    p, q = divmod(m*60., 1.)
    coord.append(p)
    coord.append(q * 60.)
    g.write("%dh%dm%ss, %dd%dm%ss, 0.05\n" %(coord[0], coord[1], coord[2], coord[3], coord[4], coord[5]))
    
f.close()
g.close()