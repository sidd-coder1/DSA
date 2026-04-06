# class Father:
#     def __init__(self):
#         print("Breakfast is ready and I am having breakfast already where are you child?")
# class Son(Father):
#     def __init__(self):
#         print("Not today father,I am not intreseted in your filthy breakfast")
    
# obj=Son()
# above example is constructor overriding because we have defined the same method name in the child class as in the parent class.

class Father:
    def __init__(self):
        print("Breakfast is ready and I am having breakfast already where are you child?")
class Son(Father):
    def __init__(self):
        print("Not today father,I am not intreseted in your filthy breakfast")
        super().__init__() # using super() to call the parent class constructor in child class
    
obj=Son()