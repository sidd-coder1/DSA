# # Tower of Hanoi
# import time 
# def towerofHonai(n, source, target, auxiliary):
#     if n==1:
#         print("Move disk 1 from source",source,"to target",target)
#         return
#     towerofHonai(n-1, source, auxiliary, target)
#     print("Move disk",n,"from source",source,"to target",target)
#     towerofHonai(n-1, auxiliary, target, source)
# n=int(input("Enter the number of disks: "))
# start_time = time.time() # it will store the current time in seconds since the epoch    
# towerofHonai(n, 'A', 'C', 'B') # it will call the function towerofHonai and pass the number of disks, source, target and auxiliary as arguments to the function
# end_time = time.time() # it will store the current time in seconds since the epoch  
# print("Time taken to solve the problem is:",end_time-start_time,"seconds") # it will print the time taken to solve the problem by subtracting the start time from the end time

import time
class Tower:
    def __init__(self):
        print("Welcome to the Tower of Hanoi Game!")
        print()
        print("Given Problem     A=[3,2,1]        B=[]        C=[]")
        print()
        print("Excpected Output   A=[]             B=[]        C=[3,2,1]")
        self.A=[]
        self.B=[]
        self.C=[]

    def tower(self,item):
            self.A.append(item)
            time.sleep(2)
            print("A=",self.A)
            print("Items in Tower A\n")
    def pass1(self):
            self.temp =self.A.pop(2)
            self.C.append(self.temp)
            time.sleep(2)
            print("A=",self.A   ,"   ",     "B=",self.B   ,"   ",     "C=",self.C)
            print("Pass One Completed========================\n")
       
    def pass2(self):
            self.temp =self.A.pop(1)
            self.B.append(self.temp)
            time.sleep(2)
            print("A=",self.A   ,"   ",     "B=",self.B   ,"   ",     "C=",self.C)
            print("Pass Two Completed========================\n")


    def pass3(self):
            self.temp =self.C.pop(0)
            self.B.append(self.temp)
            time.sleep(2)
            print("A=",self.A   ,"   ",     "B=",self.B   ,"   ",     "C=",self.C)
            print("Pass Three Completed========================\n")

    def pass4(self):
            self.temp =self.A.pop(0)
            self.C.append(self.temp)
            time.sleep(2)
            print("A=",self.A   ,"   ",     "B=",self.B   ,"   ",     "C=",self.C)
            print("Pass Four Completed========================\n")



    def pass5(self):
            self.temp =self.B.pop(1)
            self.A.append(self.temp)
            time.sleep(2)
            print("A=",self.A   ,"   ",     "B=",self.B   ,"   ",     "C=",self.C)
            print("Pass Five Completed========================\n")
         
    def pass6(self):
            self.temp =self.B.pop(0)
            self.C.append(self.temp)
            time.sleep(2)
            print("A=",self.A   ,"   ",     "B=",self.B   ,"   ",     "C=",self.C)
            print("Pass Six Completed========================\n")
    
    def pass7(self):
            self.temp =self.A.pop(0)
            self.C.append(self.temp)
            time.sleep(2)
            print("A=",self.A   ,"   ",     "B=",self.B   ,"   ",     "C=",self.C)  
            print("Pass Seven Completed========================\n")

obj=Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()

