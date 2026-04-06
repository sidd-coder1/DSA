# what is polymorphism in python?
# Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. 
# It enables a single interface to represent different types of objects, allowing for flexibility and code reusability.
# In Python, polymorphism can be achieved through method overriding and method overloading.

# class Principal:
#     def role(self):
#         print("The principal is responsible for the overall management of the school.")
# class Dean:
#     def role(self):
#         print("The dean is responsible for the academic affairs of the school.")
# class Hod:
#     def role(self):
#         print("The head of department is responsible for the Teacher and students of the department.")
# class Faculty:
#     def role(self):
#         print("faculty is responsible for commpleting the syllabus successfully")
# def func(obj):
#     obj.role()
# campus=[Principal(), Dean(), Hod(), Faculty()]
# for obj in campus:
#     func(obj)

# Python does not support method overloading and constructor overloading like other programming languages.
# Function overloading is the ability to define multiple functions with the same name but different parameters.
# Constructor overloading is the ability to define multiple constructors with different parameters in a class.
 



# class Arithmetic:
#         def add(self, a,):
#             print(a)
#         def add(self, a, b):
#             print(a+b)
#         def add(self,a,b,c):
#             print(a+b+c)
# obj=Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)
#  That's why python does not support method overloading .


# class Arithmetic:
#     def add(self,a=None,b=None,c=None ):
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=None and b!=None:  
#             print(a+b)
#         elif a!=None:
#             print(a)
#         else:
#             print("Please provide valid arguments.")
# obj=Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)



# class Arithmetic:
#     def __init__(self,a):
#         print("There is no argument")
#     def __init__(self,a,b):
#         print("There are two arguments")
#     def __init__(self,a,b,c):
#         print("There are three arguments")
# obj=Arithmetic()
# obj=Arithmetic(10)
# obj=Arithmetic(2,4) 
# this code will give an error because python does not support constructor overloading. The last defined constructor will overwrite the previous ones.



