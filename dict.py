# sample input:{c:3,"B":2,"A":1}
# output: Ascending by key {"A":1,"B":2,"C":3}
# Descending by value {"C":3,"B":2,"A":1}

class Dict:
    def __init__(self):
        self.dic={}
    def add(self,key,value):
        self.dic[key]=value
    def ascending_by_key(self):
        for i in sorted(self.dic.keys()):
            print(i,":",self.dic[i])
    def descending_by_value(self):
        for i in sorted(self.dic.items(),key=lambda x:x[1],reverse=True):
            print(i[0],":",i[1])
d=Dict()
d.add("C",3)
d.add("B",2)
d.add("A",1)
print("Ascending by key")
d.ascending_by_key()
print("Descending by value")
d.descending_by_value()

