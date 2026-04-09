class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __inti__(self):
        self.head=None

linkedlist=LinkedList()
# linkedlist1=LinkedList()
# linkedlist2=LinkedList()
linkedlist.head=Node(5)
second =Node(10)
third  =Node(15)
# print(linkedlist.head.data)
# print(linkedlist1.head.data)
# print(linkedlist2.head.data) 

 
# linking the nodes
linkedlist.head.next=second
second.next=third
# print(linkedlist.head.next.data) # it will print the data of the next node which is linked to the head node of the linked list
# print(linkedlist1.head.next.data) # it will print the data of the next node
# print(linkedlist2.head.next) # it will print None because the next node of the last node is None

# displaying the linked list

while linkedlist.head is not None:
    print("|", linkedlist.head.data, "|", linkedlist.head.next,end=" ") # it will print the data of the current node
    linkedlist.head=linkedlist.head.next # it will move the head to the next node of the linked list 



