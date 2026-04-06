# method overriding
# for overriding a method in a subclass, you need to define the same method name in the subclass as in the parent class.
 

class RBI:
    def home_loan(self):
        print("RBI Home Loan Interest Rate: 7.5%")
    def car_loan(self):
        print("RBI Car Loan Interest Rate: 8.5%")
class SBI(RBI):
    def home_loan(self):
        print("SBI Home Loan Interest Rate: 6.5%")
    def car_loan(self):
        print("SBI Car Loan Interest Rate: 8.0%")
        super().home_loan()  # using super() to call the parent class method in child class
        super().car_loan()   # using super() to call the parent class method in child class
obj=SBI()
obj.home_loan()
obj.car_loan()
