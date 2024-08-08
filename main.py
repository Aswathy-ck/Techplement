import json
def addDetails():

    try:
        with open('file.txt', 'r') as data:
            mydict=json.load(data)


    except FileNotFoundError:
        mydict={}
        print( "FILE NOT FOUND CREATE A FILE")

    name = str(input("Enter the name: "))

    if name not in mydict:

        phonenumber = int(input("Enter the phone number:"))

        mydict[name] = phonenumber

        print("Successfully added contact details!!!")
        print(f"name:{name}\nphone number:{phonenumber}")
    else:
        print("Name already exists try another")
        addDetails()
    with open('file.txt', 'w') as data:
        json.dump(mydict, data, indent=4)

def updateDetails():
    try:
        with open('file.txt', 'r') as data:
            mydict=json.load(data)

    except FileNotFoundError:
        print("File not Found")
    name = str(input("enter the name to change the phone number  :"))
    if name not in mydict:
        print("Name not found Add details first ")
    else:
        for key in mydict:
            if name == key:
                phonenumber = int(input("Enter the phone number :"))
                mydict[name] = phonenumber

      
    with open('file.txt', 'w') as data:
        json.dump(mydict, data, indent=4)


def searchDetails():
    try:
        with open('file.txt', 'r') as data:
            mydict = json.load(data)

    except FileNotFoundError:
        print("File not Found")

    name = str(input("Enter the name to search phone number :"))
    if name not in mydict:
        print("No contact information found on this name.")
    else:
        for key in mydict:
            if name == key:
                print(f"phone number :{mydict[key]}")
def deleteDetails():
    try:
        with open('file.txt', 'r') as data:
            mydict = json.load(data)

    except FileNotFoundError:
        print("File not Found")
    name = str(input("Enter the name to delete :"))
    if name not in mydict:
        print("Name not found  ")
    else:
        print(f"Deleted the details :{name, mydict[name]}")
        del mydict[name]

    with open('file.txt', 'w') as data:
        json.dump(mydict,data,indent=4)
def displayDetails():
    try:
        with open('file.txt', 'r') as data:
            mydict = json.load(data)


    except FileNotFoundError:
        print("File not Found")
    print(f"The Contact informations are :")
    for key in mydict:
        print(f"{key, mydict[key]}")


def contact(value):
    match value:
        case '1':
            return addDetails()
        case '2':
            updateDetails()
        case '3':
            searchDetails()
        case '4':
            deleteDetails()
        case '5':
            displayDetails()
        case __:
            print("Invalid option")
def main():
    print("________CONTACT MANAGEMENT SYSTEM_____________")


    while(True):

        uinput = input("\n1:ADD CONTACT DETAILS\n2:UPDATE CONTACT DETAILS\n3.SEARCH CONTACT DETAILS\n4:DELETE CONTACT DETAILS\n5:See Full contact information\nq: for quit\n\n")
        if uinput == "q":
            break
        else:
            contact(uinput)

main()