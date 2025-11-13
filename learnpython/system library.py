'''import sys

password = input("Enter password: ")
if password != "bruh123":
    sys.exit("❌ Wrong password, program stopped!")
print("✅ Access granted!")
'''

'''import sys
print("Python version running is:", sys.version)
'''

'''import sys
for path in sys.path:
    print(path)'''

'''import sys

# sys.argv[0] is always the filename
name = sys.argv[1]   # first argument
age = sys.argv[2]    # second argument

print(f"Yo {name}, you are {age} years old!")'''



# Password checking program with command line argument
import sys
import getpass
secret="bruh123"

if len(sys.argv)>2:
        print("Access Denied!,Too many arguments!")
elif len(sys.argv)==1:
    password=getpass.getpass("Enter password: ")
    if password==secret:
        print("�� Correct password")
    else:
        sys.exit("Access Denied!")
elif sys.argv[1]==secret:
    print("Access Granted!")
else:
    print("Access Denied!")


