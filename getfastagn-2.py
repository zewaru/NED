# to get galaxies identified as active by NED, this time searched by activity on
#http://ned.ipac.caltech.edu/forms/gmd.html 
#Build data table from input list


f = open("Fast-types.dat", 'r')
g = open("Fast-Agn-types.dat", 'w')

i = 0
while i < 3:
    f.readline()
    i += 1

for line in f:
    columns = line.split("|")
    characters = list(columns[15])
    if not columns[15].startswith("  "):
        g.write("%s %s\n" % (columns[2], columns[15]))
        