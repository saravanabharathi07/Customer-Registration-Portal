#PRINT DUPLICATE ELEMENTS WITHOUT USING LIST AND DICTIONARY
'''a=[1,2,3,2,4,1,5]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            print("Duplicate:",a[i])'''

#PRINT ALL PAIRS IN A SET
'''a=[1,2,3,4]
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]!=a[j]:
            print("set is : ",{a[i],a[j]})
    print()'''

a=[3,4,2,7,9]
max_sum=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]>max_sum:
            max_sum = a[i] + a[j]
            pair=(a[i],a[j])
print("the pair with maximum sum is : ",pair,"and their sum is : ",max_sum)
