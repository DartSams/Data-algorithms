class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None



class Tree:
    def __init__(self):
        self.root=None

    def add(self,current,value):
        if self.root == None:
            self.root=Node(value)


        else:
            if value < current.value:
                if current.left == None:
                    current.left=Node(value)
                elif current.left != None:
                    self.add(current.left,value)

            elif value > current.value:
                if current.right == None:
                    current.right=Node(value)
                elif current.right != None:
                    self.add(current.right,value)


    def visit(self,current):
        print(current.value)

    def inorder(self,current):
        if current:
            self.inorder(current.left)
            self.visit(current)
            self.inorder(current.right)

    def preorder(self,current):
        if current:
            self.visit(current)
            self.preorder(current.left)
            self.preorder(current.right)

    def postorder(self,current):
        if current:
            self.postorder(current.left)
            self.postorder(current.right)
            self.visit(current)



lst=[7,8,3,5,2,4,1,2]
a=Tree()
for i in lst:
    a.add(a.root,i)

# a.inorder(a.root)
a.preorder(a.root) #pre=[7,3,2,1,5,4,8]



##Intro
# class bst:
#     def __init__(self,value):
#         self.value=value
#         self.left=None
#         self.right=None

# def inorder(node):
#     # print(node.left)
#     if node:
#         inorder(node.left)
#         print(node.value)
#         inorder(node.right)


# root=bst(50)
# root.left=bst(43)
# root.right=bst(34)

# inorder(root)