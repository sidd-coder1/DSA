# inheritance in python
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new
# extending property from one class (called the child or subclass) to another class (called the parent or superclass).
# base class or parent class : The class that is being inherited from is called the base class or parent class.
#  It contains the common attributes and methods that can be shared by multiple child classes.
# derived class or child class : The class that inherits from the base class is called the derived class or child class.
#  It can have its own unique attributes and methods, in addition to the ones inherited from the base class.
#Types of inheritance in python:
#1. Single Inheritance: In single inheritance, a child class inherits from a single parent class.
#2. Multiple Inheritance: In multiple inheritance, a child class inherits from multiple parent classes.
#3. Multilevel Inheritance: In multilevel inheritance, a child class inherits from a parent class, which in turn inherits from another parent class.
#4. Hierarchical Inheritance: In hierarchical inheritance, multiple child classes inherit from a single parent class.
#5. Hybrid Inheritance: In hybrid inheritance, a child class inherits from multiple parent classes, which can be a combination of single, multiple, and multilevel inheritance.


# Single Inheritance Example

# class College:
#     def college_name(self):
#         print("College Name: YBIT College")
# class Student(College):
#     def student_info(self):
#         print("Student Name: Siddharth Singh")
#         print("Student Roll No: 20014")
# obj=Student()
# obj.college_name()
# obj.student_info()





# Multilevel Inheritance Example


# class College:
#     def college_name(self):
#         print("College Name: YBIT College")
# class Student(College):
#     def student_info(self):
#         print("Student Name: Siddharth Singh")
#         print("Student Branch: Computer Engineering")
# class Exam(Student):
#     def subject(self):
#         print("Subject1: C&SS")
#         print("Subject2: CC")
#         print("Subject3: MC")
# obj=Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()



# Multiple Inheritance Example
# class subMarks:
#     math=int(input("Enter marks for Math: "))
#     DE=int(input("Enter marks for DE: "))
#     c=int(input("Enter marks for C: "))
#     english=int(input("Enter marks for English: "))
# class PractMarks:
#     cprac=int(input("Enter marks for C Practical: "))
# class Result(subMarks,PractMarks):
#     def total(self):
#       if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cprac>=40:
#         print("passed")
#       else:
#         print("failed")
# obj=Result()
# obj.total()

