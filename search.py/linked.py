
if __name__ =="__main__":
    object=LinkedList()

    while True:
        print("1. Add Node LinkedList")
        print("2. Add node in begining of LinkedList")
        print("3. Add node in end of LinkedList")
        print("4. Add node in between of LinkedList")
        print("5. Display LinkedList")
        print("6. Exit LinkedList")



        ch=int(input("Enter your choice: "))
        if ch==1:
            val=int(input("Enter the value of node: "))
            object.addNode(val) # a method is used to add a node to the linked list
            print("Node added to the linked list")
        elif ch==2:
            val=int(input("Enter the value of node: "))
            object.addNodeBegining(val) # a method is used to add a node to the begining of the linked list
            print("Node added to the begining of the linked list")
        elif ch==3:
            val=int(input("Enter the value of node: "))
            object.addNodeEnd(val) # a method is used to add a node to the end of the linked list
            print("Node added to the end of the linked list")
        elif ch==4:
            val=int(input("Enter the value of node: "))
            pos=int(input("Enter the position of node: "))
            object.addNodeBetween(val,pos) # a method is used to add a node to the between of the linked list
            print("Node added to the between of the linked list")
        elif ch==5:
            object.displayLinkedList() # a method is used to display the linked list
        elif ch==6:
            print("Exiting LinkedList...")
            break
        else:
            print("Invalid choice")

class Node:
    def __init__(self, data):
        self.data = data  #instance variable to store the data of the node
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def addNode(self, value):
        node=Node(value) # a method is used to create a new node with the given value
        if self.head is None: # a method is used to check if the linked list is empty or not
            self.head=node # if the linked list is empty, then the head and tail will point to the new node
            self.tail=node
        else:
            self.tail.next=node # if the linked list is not empty, then the next of the tail will point to the new node and the tail will point to the new node
            self.tail=node
    def displayLinkedList(self):
        current=self.head # a method is used to create a variable current that will point to the head of the linked list
        while current is not None: # a method is used to traverse the linked list until the current is not None
            print("|", current.data, "|", end=" ") # a method is used to print the data of the current node
            current=current.next # a method is used to move the current to the next node of the linked list
            print() # a method is used to print a new line after printing the linked list
    
    
