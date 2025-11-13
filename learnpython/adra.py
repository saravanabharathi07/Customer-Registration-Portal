'''def least():
    arr=[2,5,3,8,5,9,3]
    seen=set()
    last_index=-1
    for i in range(len(arr)-1,0,-1):
        if arr[i] in seen:
            last_index=i
        else:
            seen.add(arr[i])
    if last_index !=-1:
        return arr[last_index]
    else:
        return None

print(least())'''
from itertools import count

'''arr=[9,2,11,5,2,11]
maxus=arr[0]
minimas=arr[0]
for i in arr:
    if i>maxus:
        maxus=i
    if i<minimas:
        minimas=i
print(maxus,minimas)'''

'''arr=[9,3,6,8,3]
count=0
for i in arr:
    count=count+i
print(count)'''

'''arr=[5,8,6,5,8,2,9]
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left=left+1
    right=right-1
print("Reversed array is : ",arr)'''

'''arr=[9,4,8,2,6,9]
e={}
for i in arr:
    if i in e:
        e[i]=e[i]+1
    else:
        e[i]=1
for j in arr:
    if e[j]==1:
        print("The First non repeating element is",j)
        break'''

'''arr=[9,6,3,5,4,1]
a=sorted(arr)
print(a[1])'''

'''shine="programming"
result=""
for i in shine:
    if i not in result:
        result=result+i
print("The string without repeating values : ",result)'''

sentence = "Hello world from ChatGPT"

# Step 1: Split words
words = sentence.split()

# Step 2: Reverse list
words.reverse()
print(words)

# Step 3: Join back into string
reversed_sentence = ' '.join(words)

print("Reversed sentence:", reversed_sentence)



