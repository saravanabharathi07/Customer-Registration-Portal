#Merge two sorted lists
'''def merge_lists():
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    print(sorted(list1+list2))
merge_lists()'''
from itertools import repeat

#Find two numbers in a list whose sum equals target
'''def target():
    goal=10
    list1=[2,5,3,7,8]
    for i in range(len(list1)):
       for j in range(i+1,len(list1)):
           if list1[i]+list1[j]==goal:
               print(list1[i],"+",list1[j],"=",goal)

target()'''

#Find the first non-repeating character in a string
'''def non_duplicate():
    word="swiss"
    for i in range(len(word)):
        repeat=False
        for j in range(len(word)):
            if i!=j and word[i]==word[j]:
                repeat=True
                break
        if not repeat:
            return word[i]
print(f"The First non repeating character is,{non_duplicate()}")'''

#Check if two strings are anagrams
'''def anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        print(f"The {s1} is anagram of {s2}")
s1=input("Enter a Word : ")
s2=input("Enter a Word to Check the anagram : ")
anagram(s1,s2)'''

#Flatten a nested list
'''def flatten():
    list1=[1,2,3,[4,5,6],7,8]
    flat=[]
    for items in list1:
        if type(items)==list:
            for sub in items:
                flat.append(sub)
        else:
            flat.append(items)
    print(flat)
flatten()'''
