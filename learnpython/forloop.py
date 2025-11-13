'''for _ in range(5):
    print(_)'''

'''fruits = ['apple','banana','orange']
for fruit in fruits:
    print(fruit)'''

'''for letter in 'python':
    print(letter)'''

'''for _ in range(2,11,2):
    print(_)'''

'''for i in range(10):
    if i%2==0:
        print(i,'even')'''

'''for i in range(10,0,-2):
    print(i)'''

'''for i in range(5,0,-1):
    print(i)
print('Blastoff')'''

'''for i in range(5,0,-1):
    print(i,end=' ')
print('Blastoff')'''

'''for i in range(1,11):
    print(i,end=' ')'''

'''total=0
n=int(input('Enter a number: '))
for i in range(1,n+1):
    total=total+i
print(f'sum of first {n} natural numbers is : ',total)'''

#LENGTH OF HOMOGENEOUS
'''count=0
for i in (1,2,3,4,5):
    count=count+1
print(f'length of this tuple is : {count}')'''

#REMOVE DUPLICATE
'''same=[]
for i in (2,3,5,5,6,7,7,8,8):
    if i not in same:
        same.append(i)
print(same)
'''
#REVERSE A STRING
'''count=""
for i in 'Balu':
    count=i+count
print(count)'''

'''count=[]
for i in 1,2,3,4:
    count.append(i)
print(count)'''

#PRINT ALL THE EVEN NUMBERS PRESENT IN A LIST
'''even=[]
for i in [2,3,4,5,6,7,8]:
    if i%2==0:
        even.append(i)
print(f'the even numbers in the list are : {even}')'''

#FIND ALL THE KEY and VALUES
'''data={"a":12,"c":54,"e":"man"}
emp={}
for key,value in data.items():
    print(f"'{key}': {value}")'''

'''a='powerstar'
b=a.split()
c={}
for i in b:
    c[i]=len(i)
print(c)'''

'''a='apple'
c={}
for i in a:
    if i not in c:
        c[i] = 1
    else:
        c[i]=c[i]+1
print(c)'''

'''students=['Hermione','harry','ron']
for i in range(len(students)):
    print(students[i])'''

'''def rank():
    students=['Hermione','harry','ron']
    for i in range(len(students)):
        print(i+1,students[i])
rank()'''

'''students= {'Hermione':'gryffindor',
           'harry':'gryffindor',
           'ron':'gryffindor',
           'draco':'slytherin'}
print(students['Hermione'])
print(students['harry'])
print(students['ron'])
print(students['draco'])

for student in students:
    print(f"'{student}' : '{students[student]}'")'''

students=[
    {'Name':'Hermione','House':'Gryffindor','patronus':'Otter'},
    {'Name':'Harry','House':'Gryffindor','patronus':'Stag'},
    {'Name':'Ron','House':'Gryffindor','patronus':'JackRussel'},
    {'Name':'Draco','House':'Gryffindor','patronus':None}
    ]
for student in students:
    print(student['Name'],student['House'],student['patronus'],sep=',')
