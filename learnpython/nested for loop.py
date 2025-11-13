'''def main():
    print_square(4)


def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()

main()
'''

'''a="I Love Myself"
b=a.split()
c={}
for i in b:
    count=0
    for j in i:
        count=count+1
    c[i]=count
print(c)'''

'''size=5
for i in range(size):
    for j in range(size):
        print("*",end="")
    print()'''

'''height=5
for i in range(1,height+1):
    for j in range(i):
        print("*",end="")
    print()'''
#PROGRAM TO PRINT A RIGHT ANGLE TRIANGLE
'''def table():
    x=3
    y=int(input("enter how many table You want to print : "))
    for i in range(1,x+1):
        for j in range(1,y+1):
            print(i,"*",j,"=",i*j)
        print()
table()'''

#PRINT A RIGHT ANGLE INVERTED TRIANGLE
def triangle():
    pattern=0
    for i in range(5,pattern,-1):
        for j in range(i):
            print("*",end="")
        print()
triangle()

#PRINT A NUMBER TRIANGLE
'''def num_triangle():
    size=5
    for i in range(1,size+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
num_triangle()'''

#PRINT A HOLLOW SQUARE
'''def hollow_sqr():
    n=5
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        print()
hollow_sqr()'''

#TO PRINT RIGHT ALIGNED TRIANGLE
'''def right_align_triangle():
    size=5
    for i in range(1,size+1):
        for j in range(size-i):
            print(" ",end="")
        for k in range(i):
            print("*",end="")
        print()
right_align_triangle()'''

#TO PRINT TRIANGLE
'''def triangle():
    n=5
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        print()
triangle()'''

#PRINT A CHESS BOARD PATTERN
'''n = 8
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()'''
