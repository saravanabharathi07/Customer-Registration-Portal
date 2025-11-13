#FIND EVEN OR ODD
'''class Solution:
    def isEven(self,n):
        if n%2==0:
            return True
        else:
            return False
obj=Solution()
print(obj.isEven(26))
'''

#TO FIRST AND LAST DIGIT
'''def first_digit(n):
    while n>=10:
        n=n/10
    return int(n)
n=int(input("Enter the number : "))
print(f"the first digit of this number={n} is {first_digit(n)}")'''

'''def lasto():
    a=int(input("Enter a number : "))
    b=int(input("Enter the power number : "))
    if b==0:
        return 1
    last_digit=a%10
    pattern=[last_digit]
    while True:
        next_digit=(pattern[-1]*last_digit)%10
        if next_digit in pattern:
            break
        pattern.append(next_digit)
    index=(b%len(pattern))-1
    return pattern[index]
print(lasto())'''

def count():
    n=20
    number=0
    for i in str(n):
        if n%int(i)==0 and i!=0:
            number=number+1
    return number
print(count())


