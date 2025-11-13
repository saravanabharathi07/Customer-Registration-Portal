'''def house():
    name=input("enter your name")
    if name=="Harry" or name=="Hermione" or name=="Ron":
        print("Gryffindor")
    elif name=="Draco":
        print("Slytherin")
    else:
        print("Sorry, you ain't getting into this mf")
house()'''

#THE ABOVE FUNCTION CAN BE WRITE USING MATCH FUNCTION
def house():
    name=input("enter your name : ").strip()
    match name.capitalize():
        case "Harry"|"Hermione"|"Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Sorry, you ain't getting into this mf")
house()
