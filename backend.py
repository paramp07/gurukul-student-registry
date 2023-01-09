#import django
#import datetime
import json
import os
from os import path
from enum import Enum


#Classes = Enum('Classes',['BALGHANSHYAM','GHANSHYAM','HARIKRUSHNA','NEELKANTH'])
class ClassesRange(Enum):
    BALGHANSHYAM = (0,5)
    GHANSHYAM = (5,9)
    HARIKRUSHNA = (10,14)
    NEELKANTH = (15,18)
class Classes(Enum):
    BALGHANSHYAM = 'BALGHANSHYAM'
    GHANSHYAM = 'GHANSHYAM'
    HARIKRUSHNA = 'HARIKRUSHNA'
    NEELKANTH = 'NEELKANTH'
class dataStructure:
    Name = None
    BDate = None
    Age = None
    Class = None
    Email = None
    def new(self, name, bdate, age, class_, email):
        newData = {
            "Name":name,
            "BDate":bdate,
            "Age":age,
            "Class":class_,
            "Email":email
        }
        return newData

def checkClass(age):
    class_ = ''
    if age in range(ClassesRange.BALGHANSHYAM.value[0], ClassesRange.BALGHANSHYAM.value[1]):
        class_ = Classes.BALGHANSHYAM.value
    elif age in range(ClassesRange.GHANSHYAM.value[0], ClassesRange.GHANSHYAM.value[1]):
        class_ = Classes.GHANSHYAM.value
    elif age in range(ClassesRange.HARIKRUSHNA.value[0], ClassesRange.HARIKRUSHNA.value[1]):
        class_ = Classes.HARIKRUSHNA.value
    elif age in range(ClassesRange.NEELKANTH.value[0], ClassesRange.NEELKANTH.value[1]):
        class_ = Classes.NEELKANTH.value
    return class_


def calculate_age(birthday):
  while True:
    try:
      # Parse the birthday string into a datetime object
      bday = datetime.strptime(birthday, "%m-%d-%Y")

      # Get the current date
      today = datetime.now()

      # Calculate the age in years
      age = today.year - bday.year

      # Check if the birthday has not yet occurred this year
      if today.month < bday.month or (today.month == bday.month and today.day < bday.day):
        age -= 1

      break

    except ValueError:
      birthday = input("Please enter a valid birthday in the format MM-DD-YYYY: ")

  return age

name = input('name(string): ')
bdate = input('birthdate(MM-DD-YYYY): ')
age = calculate_age(bdate)
print("Your age is:", age)


#Error handling for age
# if age != int:
#     raise Exception('Please enter a valid age(whole number)')
# else:
#     age = int(age)

class_ = checkClass(age)
print("Your Class is:", class_)
email = input('email(email@somthing.com):   ')
joe = dataStructure().new(f'{name}',f'{bdate}',age,f'{class_}',f'{email}')


#JSON ---> Python stuff
fileName = str(os.path.abspath(path)) + "/dataBase.JSON"
listObj = []

#Check if file is there
if path.isfile(fileName) is False:
    raise Exception('File not found')
#Read the JSON File
with open(fileName) as fp:
    listObj = json.load(fp)
#Add new entry to python list
listObj.append(joe)
with open(fileName, 'w') as json_file:
    json.dump(listObj, json_file, indent=4, separators=(',',':'))
