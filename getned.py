
import math
import sys

f = open("2mrs_1175_done.dat",'r')

g = open("Ned_references.out",'w')

ned_id = open("Ned-id.txt",'w')

ref_list = open("NED_reference.list",'w')

ref_sort = open("NED_references.sort", 'w')

g.write("#Ned references collected from the 2mrs_1175_done.dat. Output of getned.py\n")
ref_list.write("#List of unique references from 2mrs_1175_done.dat\n")
ref_sort.write("#Sorted list of references from most frequent to least\n")


for i in range(9):
    f.next()
    i +=1

ref = []
ref_count = []

for line in f:
    data = line.split()
    if data[26] == "N" :
        ned_id.write("%s %s %f\n" %(data[1], data[2], float(data[24])/300000 + 1))
        g.write("%s %s %s %s %s\n" %(data[0], data[1], data[2], data[24], data[27]))
        if data[27] not in ref:
            ref.append(data[27])
#            ref_list.write("%s \n" %(data[27]))
            ref_count.append(1)
        else:
            i = ref.index("%s" % (data[27]))
            ref_count[i] = ref_count[i] + 1

print len(ref_count)
print len(ref)

for i in range(0, len(ref)-1):
    ref_list.write("%s %s\n" %(ref[i], ref_count[i]))
    i += 1

for i in range(0, len(ref)):
    j = ref_count.index(max(ref_count))
    ref_sort.write("%s %s\n" %(ref[j],ref_count[j]))
    ref.pop(j)
    ref_count.pop(j)




print ref_count

g.close()
f.close()
ref_list.close()
ref_sort.close()
ned_id.close()