#USED TO WRITE DATA TO FILE
'''names=input("Enter Your Name: ")
with open("notes.txt","a") as file:
    file.write(names+"\n")'''

'''
#USED TO READ DATA FROM FILE
names=[]
# by default,open the file in read mode
# 'with' statement ensures the file is closed after reading, even if an error occurs
with open("notes.txt") as file:
    for line in file:
# rstrip() removes trailing newline character from each line
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}!")'''