import sys
class Queue:
    def __init__(self,queueSize):
        self.queuelist=[]  # creating an empty list to implement queue
        self.queueSize = queueSize # a variable is used to store the size of the queue
    def isFull(self):
        if len(self.queuelist)==self.queueSize: # a method is used to check if the queue is full or not
            return True
        else:
            return False
    def enqueue(self, value):
        if self.isFull():
            print("Queue is full")
        else:
            self.queuelist.append(value) # a method is used to add an element to the end of the list
    def displayQueue(self):
        print(self.queuelist) # a method is used to display the elements of the queue
    def isEmpty(self):
        if self.queuelist==[]: # a method is used to check if the queue is empty or not
            return True
        else:
            return False
    def dequeue(self):
        if self.isEmpty(): # a method is used to check if the queue is empty or not
            print("Queue is empty")
        else:
            return self.queuelist.pop(0) # a method is used to remove the first element from the list and return it
        
    def createQueue(self):
        # after deleting the queue, we can create a new queue by initializing the queuelist as an empty list and setting the queueSize to 0
        self.queuelist=[]  # creating an empty list to implement queue  
        self.queueSize = [size] # a variable is used to store the size of the queue
        print("=====================================================")
        print("New Queue Created")
        print("=====================================================")
        size1 =int(input("Enter the size of the queue: "))
        self.queueSize = size1 # a variable is used to store the size of the queue      

    def deleteQueue(self):
        self.queuelist=None # a method is used to delete the queue by making the list empty'
        print("=====================================================")
        print("Queue Deleted")
        print("=====================================================")
        print("Do you want to create a new queue? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            self.createQueue()
    def peekQueue(self):
        if self.isEmpty(): # a method is used to check if the queue is empty or not
            print("Queue is empty")
        else:
            return self.queuelist[0] # a method is used to peek at the top element of the queue
    def exitQueue(self):
        print("Exiting Queue...")


size =int(input("Enter the size of the queue: "))
Queueobj=Queue(size) # it will create an object of the queue class and pass the size of the queue as an argument to the constructor of the queue class


while True:
    print("1. Enqueue Element in Queue")
    print("2. Display Queue")
    print("3. Check if Queue is Empty")
    print("4. Dequeue Element from Queue")
    print("5. Delete Queue")
    print("6. Create Queue")
    print("7. Peek Element from Queue")
    print("8. Exit Queue")
    choice=int(input("Enter your choice: "))    
    if choice==1:
     val1=int(input("Enter the value of queue : "))
     Queueobj.enqueue(val1)      # a method is used to add an element to the end of the list
    elif choice==2:
        Queueobj.displayQueue() # a method is used to display the elements of the queue
    elif choice==3:
        print(Queueobj.isEmpty()) # a method is used to check if the queue is empty or not
    elif choice==4:
        print(Queueobj.dequeue()) # a method is used to remove the first element from the list and return it
    elif choice==5:
        Queueobj.deleteQueue() # a method is used to delete the queue by making the list empty
    elif choice==6:
        Queueobj.createQueue() # a method is used to create a new queue
    elif choice==7:
        print(Queueobj.peekQueue()) # a method is used to peek at the top element of the queue
    elif choice==8:
        Queueobj.exitQueue() # a method is used to exit the queue
        sys.exit()      # a method is used to exit the program
    else:
        print("Invalid choice")

    





    