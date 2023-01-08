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
    if age in range(ClassesRange().BALGHANSHYAM):
        class_ = Classes().BALGHANSHYAM
    elif age in range(ClassesRange().GHANSHYAM):
        class_ = Classes().GHANSHYAM
    elif age in range(ClassesRange().HARIKRUSHNA):
        class_ = Classes().HARIKRUSHNA
    elif age in range(ClassesRange().NEELKANTH):
        class_ = Classes().NEELKANTH
    return class_

name = input('name(string): ')
bdate = input('birthdate(MM-DD-YYYY): ')
age = input('age(whole number):  ')
#Error handling for age
if age != int:
    raise Exception('Please enter a valid age(whole number)')
else:
    age = int(age)
class_ = checkClass(age)
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
