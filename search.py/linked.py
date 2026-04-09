import sys
if __name__ =="__main__":
 class  Node:
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
            self.tail=node # the tail will point to the new node
    def addNodeBegining(self, value):
        node=Node(value) # a method is used to create a new node with the given value
        if self.head is None: # a method is used to check if the linked list is empty or not
            self.head=node # if the linked list is empty, then the head and tail will point to the new node
            self.tail=node
        else:
            node.next=self.head # if the linked list is not empty, then the next of the new node will point to the head and the head will point to the new node
            self.head=node # the head will point to the new node
    def addNodeEnd(self, value):
        node=Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def addNodeBetween(self, value, pos):
        node=Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
        elif pos==0:
            node.next=self.head
            self.head=node
        else:
            temp=self.head
            for _ in range(pos-1):
                temp=temp.next
            node.next=temp.next
            temp.next=node
    def searchNode(self, value):
        current=self.head # a method is used to create a variable current that will point to the head of the linked list
        while current is not None: # a method is used to traverse the linked list until the current is not None
            if current.data==value: # a method is used to check if the data of the current node is equal to the value we are searching for
                return True # if the value is found, then it will return True
            current=current.next # a method is used to move the current to the next node of the linked list
        return False # if the value is not found, then it will return False
    
    def deleteLinkedList(self,index):
       node =Node(index)
       if node is None:
           print("Linked List is empty")
       elif index==0:
           self.head=self.head.next
           if self.head is None:
               self.tail=None
       else:
           temp=self.head
           for _ in range(index-1):
               temp=temp.next
           if temp.next is self.tail:
               self.tail=temp
           temp.next=temp.next.next
    def displayLinkedList(self): 
        current=self.head # a method is used to create a variable current that will point to the head of the linked list
        while current is not None: # a method is used to traverse the linked list until the current is not None
            print("|", current.data, "|",current.next,"|", end="  ") # a method is used to print the data of the current node
            current=current.next # a method is used to move the current to the next node of the linked list
            print() # a method is used to print a new line after printing the linked list
    
object=LinkedList() # it will create an object of the linked list class and pass the size of the linked list as an argument to the constructor of the linked list class


while True:
        print("1. Add Node LinkedList")
        print("2. Add node in begining of LinkedList")
        print("3. Add node in end of LinkedList")
        print("4. Add node in between of LinkedList")
        print("5. Display LinkedList")
        print("6. Delete LinkedList")
        print("7. Search Node in LinkedList")
        print("8. Exit LinkedList")



        ch=int(input("Enter your choice: "))
        if ch==1:
            val=int(input("Enter the value of node: "))
            object.addNode(val) # a method is used to add a node to the linked list
            print("********************************************************")
            print("Node added to the linked list")
            print("********************************************************")
        elif ch==2:
            val=int(input("Enter the value of node: "))
            object.addNodeBegining(val) # a method is used to add a node to the begining of the linked list
            print("********************************************************")
            print("Node added to the begining of the linked list")
            print("********************************************************")
        elif ch==3:
            val=int(input("Enter the value of node: "))
            object.addNodeEnd(val) # a method is used to add a node to the end of the linked list
            print("********************************************************")
            print("Node added to the end of the linked list")
            print("********************************************************")
        elif ch==4:
            val=int(input("Enter the value of node: "))
            pos=int(input("Enter the position of node: "))
            object.addNodeBetween(val,pos) # a method is used to add a node to the between of the linked list
            print("********************************************************")
            print("Node added to the between of the linked list")
            print("********************************************************")
        elif ch==5:
            object.displayLinkedList() # a method is used to display the linked list
        elif ch==6:
            index=int(input("Enter the index of node to delete: "))
            object.deleteLinkedList(index)
            print("********************************************************")
            print("Node deleted from the linked list")
            print("********************************************************")
        elif ch==7:
            val=int(input("Enter the value of node to search: "))
            if object.searchNode(val):
                print("********************************************************")
                print("Node found in the linked list")
                print("********************************************************")
            else:
                print("********************************************************")
                print("Node not found in the linked list")
                print("********************************************************")
        elif ch==8:
            print("Exiting LinkedList...")
            sys.exit()
        else:
            print("Invalid choice")

