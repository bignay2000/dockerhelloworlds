import time
import os
import platform

class Student:
    def __init__(self, name):
        self.name = name
        self.attend = 0
        self.grades = []
        print("Hi My name is {0}".format(self.name))
    def addGrade(self, grade):
        self.grades.append(grade)
    def attendDay(self):
        self.attend += 1
        print("Attend Days is " + str(self.attend))

def strings():
    mystring = "This is cool"
    print(mystring)
    print("lower case:")
    print(mystring.lower())

def fruits():
    fruits = ["apples", "orange", "lemon"]
    print(fruits)
    print(fruits[0:1])


def dictionary():
    print("Dictionary Literal")
    address = {'bob': '1234 Main', 'Jim': 1234}
    print (address)
    inventory = {}
    inventory['bob'] = "1234 Main"
    inventory['Jim'] = 1234
    print(inventory)
    print("Keys:")
    print(list(inventory.keys()))
    print("Values:")
    print(list(inventory.values()))
    print("Remove Jim from dictionary")
    del inventory['Jim']
    print(inventory)


def whoareyou():
    yourname = input("Enter your Name: ")
    yourage = int(input("Enter your Age: "))
    print("Welcome " + yourname + "!")
    print("age: " + str(yourage))


def ryan(a=10, b=10):
    result = a * b
    return result


def equaltotwo(x):
    if x == 2:
        print("x equals 2")
    elif x > 9:
        print("x is greater than 9")
    else:
        print("x does not equal 2")


def whileloop(x):
    while x < 5:
        x = x + 1
        print(x)


def forloop():
    for x in range(1,5):
        x = x + 1
        print(x)


def tired(a):
    print("Sleeping " + str(a))
    time.sleep(a)
    print("Done Sleeping " + str(a))


def computer():
    print("OS is " + os.name)
    print("platform System is " + platform.system() + " " + str(platform.architecture()))


print("Helloworld")
computer()
# whoareyou()
print(ryan())
fruits()
equaltotwo(3)
equaltotwo(10)
whileloop(0)
forloop()
dictionary()
strings()


#tired(int(os.environ.get('PYTHON3_SLEEP')))

# class
# student1 = Student("Ryan")
# student1.attendDay()
# student1.attendDay()
