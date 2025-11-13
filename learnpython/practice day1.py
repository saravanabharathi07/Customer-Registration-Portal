#REVERSE A STRING
'''def reverse_string():
    x=input("Enter a string: ")
    word1=" "
    for i in x:
        word1=i+word1
    print("Reversed string is:",word1)
reverse_string()'''

#CHECK IF STRING IS A PALINDROME
'''def is_palindrome(s):
    empty=""
    for i in s:
        empty=i+empty
    if empty==s:
        print("The string is a palindrome.")
    else:
        print("it's not a palindrome.")
def get_input():
    x=input("Enter a string: ")
    is_palindrome(x)
get_input()'''

#FIND THE MAXIMUM ELEMENT IN A LIST
'''def element(list1):
    max_element=list1[0]
    for i in list1:
        if i > max_element:
            max_element=i
    print("The maximum element in the list is:", max_element)

element([3, 27, 2, 10, 15])'''

#FIND THE MAX OF ANY TWO ELEMENTS IN A LIST
'''fun=[2,5,4,6,9]
empty=0
for i in fun:
    for j in fun:
        if i!=j:
            kun=i+j
            if kun > empty:
                empty=kun
print(empty)'''


#REMOVE DUPLICATES FROM A LIST
'''kun=[23,56,78,23,55,6,78]
list1=[]
for i in kun:
    if i not in list1:
        list1.append(i)
print(list1)'''


#COUNT FREQUENCY OF CHARACTERS IN A STRING
'''x="apple"
list1={}
for i in x:
    if i not in list1:
        list1[i]=1
    else:
        list1[i]=list1[i]+1
print(list1)'''




