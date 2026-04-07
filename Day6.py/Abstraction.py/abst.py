from abc import ABC, abstractmethod
class Help4code(ABC):
    @abstractmethod
    def training(self):
        pass
    @abstractmethod
    def placement(self):
        pass

class Maruti(Help4code):
    def training(self):
        print("Maruti will provide training in java ,c ,c++")
    def placement(self):
        print("Maruti will provide placement in java  ")
class Om(Help4code):
    def training(self):
        print("Om will provide training in python ,Django")
    def placement(self):
        print("Om will provide placement in python")
        
class Mahesh(Help4code):
    def training(self):
        print("Mahesh will provide training in Machine Learning")
    def placement(self):
        print("Mahesh will provide placement in Machine Learning")
        


obj=Maruti()
obj.training()
obj.placement()
obj1=Om()
obj1.training()
obj1.placement()
obj2=Mahesh()
obj2.training()
obj2.placement()

