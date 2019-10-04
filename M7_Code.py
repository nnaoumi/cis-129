# M7 Assignment - Apgar Medical Group
# Author - Nicholas Naoumi

bPatient = open('Best_Patients.txt')
cPatient = open('Cushing_Patients.txt')

bList = []
cList = []

# To add elements to the bList variable
for line1 in bPatient :
    bList.append(line1)

# To add elements to the cList variable
for line2 in cPatient :
    cList.append(line2)

# To merge and sort patient lists
mergedList = bList + cList
mergedList.sort()

# To remove newline character from each list element
mergedList = [newline.rstrip('\n') for newline in mergedList]

# Output of merged patient lists
with open('Merged_Patients.txt', 'x') as newfile :
    print(*mergedList, sep='\n', file=newfile)

newfile.close()

print('Both patient lists have been merged. The merged list is exported as Merged_Patients.txt')