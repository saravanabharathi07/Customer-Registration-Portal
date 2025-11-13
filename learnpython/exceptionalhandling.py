#Here When I give An Integer As an input to the function, it will print the value of x.
#But When I give a string as an input to the function, it will Throw an error message.
#To handle this error, we can add a try-except block.
'''def print_num():
    x=int(input("enter value of x: "))
    print("x is : ",x)
print_num()'''
from wsgiref.validate import validator

#TRY EXCEPT METHOD
'''def print_num():
   try:
        x = int(input("enter value of x: "))
        print("x is : ", x)
   except ValueError:
       print("Invalid input! Please enter an integer.")

print_num()'''


#TRY TO HANDLE MORE THAN ONE EXCEPTION
'''try:
    x = int(input("enter value of x: "))
except ValueError:
    print("Invalid input! Please enter an integer.")
else:
    print("x is : ", x)'''

#REPEATS THE CODE UNTIL THE USER ENTERS A VALID INPUT
'''while True:
    try:
        x=int(input("enter value of x: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
    else:
        print("x is : ", x)
        break'''

#MINIMIZE THE PREVIOUS CODE
'''def main():
    x=print_num()
    print("x is : ", x)

def print_num():
    while True:
        try:
            return int(input("enter value of x: "))
        except ValueError:
            pass
main()'''

#FILE HANDLING
'''try:
    f = open("notes.txt", "r")   # risky: file might not exist
    data = f.read()
except FileNotFoundError:
    print("File doesn't exist — creating one.")
    with open("notes.txt", "w") as f:
        f.write("")              # creates an empty file
else:
    print("File loaded, length:", len(data))
finally:
    try:
        f.close()                # cleanup
    except UnboundLocalError:
        pass'''



