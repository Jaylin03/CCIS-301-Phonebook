import phonebook

def newContact():

    # Enter and return first name
    def enterFName():
        fName = input("Enter first name: ")
        return fName

    # Enter and return last name
    def enterLName():
        lName = input("Enter last name (Press enter to skip): ")
        return lName

    # Enter and return phone nubmer
    def enterNumber():
        number = input("Enter phone number: ")
        return number

    # Enter and return email
    def enterEmail():
        email = input("Enter email (Press enter to skip): ")
        return email

    # Enter and return prnouns
    def enterPronouns():
        pronouns = input("Enter pronouns (Press enter to skip): ")
        return pronouns

    # Display all info for given contact
    def displayInfo(fName, number, lName="" , email="", pronouns=""):
        # Display entered information
        print ("\nWhat you entered:")
        print(f"Name: {fName} {lName}\nNumber: {number}\nEmail: {email}\nPronouns: {pronouns}")

    # Enter and return last name
    create = "no"
    while create != "yes":
        fName = enterFName()
        lName = enterLName()
        number = enterNumber()
        email = enterEmail()
        pronouns = enterPronouns()
        displayInfo(fName, number, lName , email, pronouns)

        create = input("Is this correct? Enter \"yes\" or \"no\": ")

        if (create.lower().startswith("y")):
            phonebook.Phonebook(fName , number , lName , email , pronouns)
            with open("myPhonebook.txt" , "a") as myPhonebook:
                myPhonebook.write(fName + " " + lName + "," + number + "," + email + "," + pronouns)
            break
        else:
            change = input("Which part is incorrect? If there are multiple incorrect section, separate with commas: ")
            changeInternal = change.split(",")
            changeInternal = [changeInternal[x].strip() for x in range(len(changeInternal))]
            if ("name" in changeInternal):
                fName = enterFName()
                lName = enterLName()
            if ("number" in changeInternal):
                number = enterNumber()
            if ("email" in changeInternal):
                email = enterEmail()
            if ("pronouns" in changeInternal):
                pronouns = enterPronouns()
            displayInfo(fName , number , lName , email , pronouns)
        create = input("Is this correct? Enter \"yes\" or \"no\": ")

newContact()

##### Testing #####

'''
All fields complete and correct
    fName = Jaylin
    lName = Lee
    number = 0123456789
    email = jaylin@gmail.com
    pronouns = she/her

Missing 1 optional field
    fName = Zariah
    lName =
    number = 101112131415
    email = zariah@gmail.com
    pronouns = she/her

Missing 2 optional fields
    fName = A'mari
    lName =
    number = 1112131415
    email =
    pronouns = he/him

Missing 3 optional fields
    fName = Karter
    lName =
    number = 1213141516
    email =
    pronouns =

Missing 1 required field
    fName = S'myrah
    lName = Akinseye
    number =
    email = smayrah@gmail.com
    pronouns = she/her

Missing 2 required fields
    fName =
    lName = Lee-Sumlin
    number =
    email = shardai@gmail.com
    pronouns = she/her

1 field incorrect
    fName = Shardai
    lName = Lee-Sum
    number = 
    email =
    pronouns =

2 fields incorrect
    fName =
    lName =
    number =
    email =
    pronouns =

All fields incorrect
    fName =
    lName =
    number =
    email =
    pronouns =
'''