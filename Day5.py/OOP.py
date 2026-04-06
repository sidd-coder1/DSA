# Python object-oriented programming (OOP) is a programming paradigm that uses objects and classes to structure code. 
# It allows for the creation of reusable and modular code, making it easier to manage and maintain. 
# In OOP, objects are instances of classes, which can have attributes (data) and methods (functions) that operate on that data. 
# This approach promotes encapsulation, inheritance, and polymorphism, which are key principles of OOP.

# what is class and object in python
# A class in Python is a blueprint for creating objects.
# It defines a set of attributes and methods that the objects created from the class will have.  
# An object, on the other hand, is an instance of a class.
# It is a specific realization of the class, with its own unique set of attribute values.
# Example of a class and object in Python
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         return "Woof!"
# # Creating an object of the Dog class
# my_dog = Dog("Buddy", 3)
# print(my_dog.name)  # Output: Buddy
# print(my_dog.age)   # Output: 3
# print(my_dog.bark())  # Output: Woof!

# class Student:
#     roll_no=0

#     def studentData(self):
#         print("Student information:")

# obj=Student()
# print(obj.roll_no)
# obj.studentData()

# class Demo:
#     def __init__(self):
#         print("This is a constructor")
    
#     def msg(self):
#         print("hello bachooo")
# obj=Demo()
# # print(obj)
# # obj2=Demo()
# # print(obj2)
# obj.msg()

# class Hod:
#     def __init__(self):
#         self.name="Siddharth Singh" #2 bytes
#         self.age=20 #4 bytes
#         self.empid=20014 #4 bytes
#     def info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Employee ID:", self.empid)
# obj=Hod() #10 bytes
# obj.info()

# class Hod:
#     def __init__(self,name,age,empid):
#         self.name=name 
#         self.age=age 
#         self.empid=empid
#     def show(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Employee ID:", self.empid)
# obj=Hod("Siddharth Singh",20,20014)
# obj.show()

# variables
# instance variable: A variable that is defined within a class and is associated with an instance of the class.
# Each instance of the class can have its own unique value for the instance variable.

# class EK:
#     def __init__(self):
#         self.a=10
# obj=EK()
# obj1=EK()
# obj2=EK()
# print(obj.a) #10
# print(obj1.a) #10   
# print(obj2.a) #10

# obj2.a=20
# print()
# print(obj.a)
# print(obj1.a)
# print(obj2.a)



# class Student:
#     def __init__(self):
#         self.name = "Siddharth Singh"
#         self.age = 20

#     def getdata(self):
#        self.s_mb= 1234567890
# obj=Student()
# obj.getdata()
# del obj.s_mb
# obj.s_branch="COE"
# print(obj.__dict__)


# static variable: 
# A variable that is shared among all instances of a class.  
# It is defined within the class but outside of any instance methods. 

# class New:
#     a=10 #static variable
#     def __init__(self):
#         self.name="Siddharth Singh"
# obj=New()
# obj1=New()
# obj2=New()
# print(obj.a) #10
# print(obj1.a) #10
# print(obj2.a) #10

# New.a=20
# print(obj.a) 
# print(obj1.a) 
# print(obj2.a)

