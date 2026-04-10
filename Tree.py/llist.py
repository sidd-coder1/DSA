class Tree:
    def __init__(self,data):
        self.data=data    #instance variable,it creates separate memory for each instance of the class
        self.children=[]
    def add_child(self,child):
        self.children.append(child)
    def __str__(self,level=0):
        ret=" "*level+str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret

rootNode=Tree("Drinks")
hot=Tree("Hot")
cold=Tree("Cold")
tea=Tree("Tea")
coffee=Tree("Coffee")
Nonalcholic=Tree("Non-Alcoholic")
alcholic=Tree("Alcoholic")


rootNode.add_child(hot)
rootNode.add_child(cold)
hot.add_child(tea)
hot.add_child(coffee)
cold.add_child(Nonalcholic)
cold.add_child(alcholic)
print(rootNode)

 