# Full Binary Tree
# Each node has either 0 or 2 children.
# No node has only one child.


# complete binary tree
# All levels are completely filled except possibly the last level, which is filled from left to right.
# last level are filled from left to right


# perfect binary tree
# All internal nodes have exactly two children and all leaf nodes are at the same level.
# all leaf nodes are at the same level and every parent has two children

# create a binary tree

# class Tree:
#     def __init__(self,data): 
#         self.data=data
#         self.children=[]
#     def add_child(self,child):
#         self.children.append(child)

# root=Tree("Maharashtra")
# Mumbai=Tree("Mumbai")
# Pune=Tree("Pune")
# Dharavi=Tree("Dharavi")
# chincholi=Tree("Chincholi")

# root.add_child(Mumbai)
# root.add_child(Pune)
# Mumbai.add_child(Dharavi)
# Pune.add_child(chincholi)
# print(root)  # Output: Maharashtra

# root.add_child(Tree("Mumbai"))
# root.add_child(Tree("Pune"))
# root.children[0].add_child(Tree("Bombay"))
# root.children[0].add_child(Tree("Thane"))
# print(root.data)  # Output: Maharashtra
# print(root.children[0].data)  # Output: Mumbai
# print(root.children[1].data)  # Output: Pune
# print(root.children[0].children[0].data)  # Output: Bombay
# print(root.children[0].children[1].data)  # Output: Thane




class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if self.root is None:
            self.root=Node(value)
        else:
            self.insertNode(self.root,value)
    def insertNode(self,rootNode,value):
        if value < rootNode.data: 
            if rootNode.left is None:
                rootNode.left = Node(value)
            else:
                self.insertNode(rootNode.left,value)
        else:
            if rootNode.right is None:
                rootNode.right=Node(value)
            else: 
                self.insertNode(rootNode.right,value)




btobj=BinaryTree()
btobj.insert(50)
btobj.insert(30)
btobj.insert(70)
print(btobj.root.data)  # Output: 50
print(btobj.root.left.data)  # Output: 30
print(btobj.root.right.data)  # Output: 70  