class Phonebook:
  def __init__(self, fName, number, lName="" , email="", pronouns=""):
    self.fName = fName
    self.number = number
    self.lName = lName
    self.email = email
    self.pronouns = pronouns

  def getfName(self):
    return self.fName

  def setfName(self , fName):
    self.fName = fName

  def getlName(self):
    return self.fName

  def setlName(self , lName):
    self.lName = lName

  def getNumber(self):
    return self.number

  def setNumber(self , number):
    self.number = number

  def getEmail(self):
    return self.email

  def setEmail(self , email):
    self.email = email

  def getPronouns(self):
    return self.pronouns

  def setPronouns(self , pronouns):
    self.pronouns = pronouns

  def displayContacts(self):
    with open("myPhonebook.txt") as myPhonebook:
      contacts = myPhonebook.readlines()
      for line in range (len(contacts)):
        print("Name:", contacts[line][0], contacts[line][2])
        print("Number:", contacts[line][1])
        print("Email:", contacts[line][3])
        print("Pronouns:", contacts[line][4])
