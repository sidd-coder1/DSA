class BSTNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insertNode(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data=nodeValue
    elif nodeValue < rootNode.data:
        if rootNode.left is None:
            rootNode.left=BSTNode(nodeValue)
        else:
            insertNode(rootNode.left,nodeValue)
    else:
        if rootNode.right is None:
            rootNode.right=BSTNode(nodeValue)
        else:
            insertNode(rootNode.right,nodeValue)
def preorderTraversal(rootNode):
    if rootNode is not None:
        print(rootNode.data)
        preorderTraversal(rootNode.left)
        preorderTraversal(rootNode.right)
    else:
        return
def inorderTraversal(rootNode):
    if rootNode is not None:
        inorderTraversal(rootNode.left)
        print(rootNode.data)
        inorderTraversal(rootNode.right)
    else:
        return

def postorderTraversal(rootNode):
    if rootNode is not None:
        postorderTraversal(rootNode.left)
        postorderTraversal(rootNode.right)
        print(rootNode.data)
    else:
        return
def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    queue = []
    queue.append(rootNode)
    while len(queue) > 0:
        currentNode = queue.pop(0)
        print(currentNode.data)
        if currentNode.left is not None:
            queue.append(currentNode.left)
        if currentNode.right is not None:
            queue.append(currentNode.right)




obj=BSTNode(None)
insertNode(obj,70)
insertNode(obj,50)
insertNode(obj,90)
insertNode(obj,30)
insertNode(obj,60)
insertNode(obj,80)
insertNode(obj,100)
insertNode(obj,20)
insertNode(obj,40)
print("Preorder Traversal:")
preorderTraversal(obj)
print("Inorder Traversal:")
inorderTraversal(obj)
print("Postorder Traversal:")
postorderTraversal(obj)
print("Level Order Traversal:")
levelOrderTraversal(obj)
