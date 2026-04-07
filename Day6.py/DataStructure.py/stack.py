# what is role of data structure in software development?
# Data structures play a crucial role in software development as they provide a way to organize and store data efficiently. 
#  They allow developers to manage and manipulate data effectively, which is essential for creating efficient algorithms and applications.

 
# stack 
# WITHOUT size limit
import sys
class Stack:
    def __init__(self):
        self.stacklist=[]  # creating an empty list to implement stack
    def push(self, value):
        self.stacklist.append(value) # a method is used to add an element to the end of the list
    def displayStack(self):
        print(self.stacklist) # a method is used to display the elements of the stack
    def isEmpty(self):
        if self.stacklist==[]: # a method is used to check if the stack is empty or not
            return True
        else:
            return False
    def popStack(self):
        if self.isEmpty(): # a method is used to check if the stack is empty or not
            print("Stack is empty")
        else:
            return self.stacklist.pop() # a method is used to remove the last element from the list and return it
    def deleteStack(self):
        self.stacklist=None # a method is used to delete the stack by making the list empty'
    def peekStack(self):
        if self.isEmpty(): # a method is used to check if the stack is empty or not
            print("Stack is empty")
        else:
            return self.stacklist[-1] # a method is used to peek at the top element of the stack
    def exitStack(self):
        print("Exiting Stack...")

Stackobj=Stack()


while True:
    print("1. Push Element in Stack")
    print("2. Display Stack")
    print("3. Check if Stack is Empty")
    print("4. Pop Element from Stack")
    print("5. Delete Stack")
    print("6. Peek Element from Stack")
    print("7. Exit Stack")
    choice=int(input("Enter your choice: "))    
    if choice==1:
     val1=int(input("Enter the size of the stack: "))
     Stackobj.push(val1)      # a method is used to add an element to the end of the list
    elif choice==2:
        Stackobj.displayStack() # a method is used to display the elements of the stack
    elif choice==3:
        print(Stackobj.isEmpty()) # a method is used to check if the stack is empty or not
    elif choice==4:
        print(Stackobj.popStack()) # a method is used to remove the last element from the list and return it
    elif choice==5:
        Stackobj.deleteStack() # a method is used to delete the stack by making the list empty
    elif choice==6:
        print(Stackobj.peekStack()) # a method is used to peek at the top element of the stack
    elif choice==7:
        Stackobj.exitStack() # a method is used to exit the stack
        sys.exit()      # a method is used to exit the program
    else:
        print("Invalid choice")