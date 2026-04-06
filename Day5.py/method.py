# instance method: A method that is defined within a class and is associated with an instance of the class. 
#  It can access and modify the instance variables of the class.   

# class Student:
#     def __init__(self,name,roll_no,mobile_no):
#         self.name=name #instance variable
#         self.roll_no=roll_no #instance variable
#         self.mobile_no=mobile_no #instance variable

#     def display(self):
#         print("Name:",self.name,"Roll No:",self.roll_no,"Mobile No:",self.mobile_no) #instance method

# obj = Student("Siddharth Singh",20014,1234567890)
# obj.display()      

#------------------------------------------- static method: -------------------------------------------
# A method that is defined within a class but is not associated with any instance of the class. 
# It can be called on the class itself, rather than on an instance of the class.


class Student:
    @staticmethod  #decorator
    def get_personal_details(firstname,lastname):
        print("your personal details =",firstname,lastname)

    @staticmethod
    def contact_detail(mobile_no, roll_no):
        print("your contact details =",mobile_no,roll_no)

Student.get_personal_details("Siddharth","Singh")
Student.contact_detail(9822485616, "ce46")
    

