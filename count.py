
import sys

g = open("6dF-detections.out",'w')
detected = 0

name = []

for i in range(1, 14):
    with open("6dF-%sk.out" %i, 'r') as f:
        print f
        f.readline()
        for line in f:
             cols = line.split(',')       
             if float(cols[8]) != 0:
                 detected += 1
                 g.write(line)
                 if cols[0] not in name:
                     name.append(cols[0])
                
print len(name)

print detected            
g.close()