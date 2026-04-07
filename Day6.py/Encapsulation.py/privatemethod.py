class Rbi:
    def publicpolicy(self):
        print("check the public policy of the rbi")
    def __privatepolicy(self):
        print("There is a private policy of the rbi which is not accessible for the public")
class Sbi(Rbi):
    def __init__(self): # first we will call constructor of child class
        Rbi.__init__(self) # calling the parent class constructor
    def callingpublicpolicy(self):
        print("\n Inside the child class we are calling the public method of the parent class")
        self.publicpolicy() # calling the public method of the parent class
    def callingprivatepolicy(self):
        print("\n Inside the child class we are calling the private method of the parent class")
        self.__privatepolicy() # this will give an error because we cannot access the private method in the child class
    
# obj=Sbi()
# obj.callingpublicpolicy()
# obj.callingprivatepolicy() # this will give an error because we cannot access the private method in the child class
# obj.publicpolicy() # this will work because we can access the public method in the child class
# obj.__privatepolicy() # this will give an error because we cannot access the private method in the child class
obj1=Rbi()
obj1.publicpolicy() # this will work because we can access the public method in the parent class
# obj1.__privatepolicy() # this will give an error because we cannot access the private method in the parent class
 
