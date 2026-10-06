numbers =[4,2,4,7,2,9,7,1]
print(" Total Values -" , numbers)

count = len(numbers)
duplist =[]
nonduplist =[]

for i in range(count):
    for j in range(i+1, count):
        if(numbers[i]==numbers[j]):
            duplist.append(numbers[i])

print(" Duplicate values -" , duplist)

for d in range(len(numbers)):
    if(numbers[d]) not in duplist:
        nonduplist.append(numbers[d])
    
print(" Non Duplicate Values -" , nonduplist)

            