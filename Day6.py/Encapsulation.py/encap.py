
# Private method used to restrict the access of the method in the class and it can only be accessed within the class and not outside the class.
class Base:
    def __init__(self):
        print("Parent class constructor is called")
        self.a="siddharth"#public variable
        self.__c="Maruti" #private variable
class Derived(Base):
    def __init__(self):
        Base.__init__(self) # calling the parent class constructor
        # print("Calling a private variable in child class ")
        # print(self.a)
        # print(self.__c) # this will give an error because we cannot access the private variable in the child class
# obj=Derived()
# print(obj.a) # this will work because we can access the public variable in the child class
# print(obj.__c) # this will give an error because we cannot access the private variable in the child class

obj1=Base()
print(obj1.a) # this will work because we can access the public variable in the parent class
print(obj1.__c) # this will give an error because we cannot access the private variable in the parent class

