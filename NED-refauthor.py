
filesort = open("NED_references.sort",'r')
filein = open("references-authors-2.dat",'r')
fileout = open("NED_references_authors.out", 'w')
fileout2 = open("NED_references_authors.sort", 'w')

filesort.readline()

reflist = []
nofrefs = []
refitem = []

for line in filesort:
    item = line.split()
    reflist.append(item[0])
    nofrefs.append(int(item[1]))

for line in filein:
    item = line.split()
    if item[0] in reflist:
        i = reflist.index(item[0])
        refitem.append((nofrefs[i], line))

refsort = sorted(refitem, reverse = True, key=lambda refitem: refitem[0])

print len(refsort)

fileout.write('\n'.join('%s %s' % x for x in refsort))

filesort.close()
filein.close()
fileout.close()