from collections import Counter

numbers =[4,2,4,7,2,9,7,1]

nonduplist =[]
duplist =[]

counts = Counter(numbers)

print(counts)


for key,value in counts.items():
    if (value==1):
        nonduplist.append(key)
    else:
        duplist.append(key)
        
        

print(" Non Duplicate Numbers -" ,nonduplist)
print(" Duplicate Numbers -" ,duplist)
        