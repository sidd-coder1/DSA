from abc import ABC, abstractmethod
class IRCTC(ABC):
    @abstractmethod
    def booking(self):
        pass

class MakeMyTrip(IRCTC):
    def booking(self):
        print("======================================================================")
        print("=============WELCOME TO MAKE MY TRIP TRAVEL AGENCY================================")
        Source=input("Enter the source station: ")
        Destination=input("Enter the destination station: ")  
        Date=input("Enter the date of journey: ")
        print("Your ticket has been booked from",Source,"to",Destination,"on",Date)
        print("======================================================================")
class GOIbibo(IRCTC):
    def booking(self):
        print("======================================================================")
        print("=============WELCOME TO GOIBIBO TRAVEL AGENCY================================")
        Source=input("Enter the source station:")
        Destination=input("Enter the destination station:")  
        Date=input("Enter the date of journey:")
        print("Your ticket has been booked from",Source,"to",Destination,"on",Date)
        print("======================================================================")

class Yatra(IRCTC):
    def booking(self):
        print("======================================================================")
        print("=============WELCOME TO YATRA TRAVEL AGENCY================================")
        Source=input("Enter the source station: ")
        Destination=input("Enter the destination station: ")  
        Date=input("Enter the date of journey: ")
        print("Your ticket has been booked from",Source,"to",Destination,"on",Date)
        print("======================================================================")

obj=MakeMyTrip()
obj.booking()
obj1=GOIbibo()
obj1.booking()
obj2=Yatra()
obj2.booking()