# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.nextNode=None

# class sll:
#     def __init__(self):
#         self.head=None
#         self.taile=None

#     def insert(self,value):
#         node=Node(value)
#         self.head=node

#     def add(self,value):
#         current=self.head
#         while current.nextNode:
#             current=current.nextNode

#         current.nextNode=Node(value)

#     def remove(self,place):
#         num=0
#         current=self.head
#         while current.value:
#             if num == place-1:
#                 current.nextNode=current.nextNode.nextNode
#                 break
#             current=current.nextNode
#             num+=1

#     def traverse(self):
#         current=self.head
#         while current.value:
#             print(current.value)
            
#             if current.nextNode is None:
#                 print("End onf linked list")
#                 break
#             else:
#                 current=current.nextNode


# a=sll()
# a.insert(1)
# a.add(2)
# a.add(3)
# a.add(4)
# a.traverse()

class Node:
    def __init__(self,value):
        self.value=value
        self.nextNode=None

class sll:
    def __init__(self):
        self.head=None

    def push(self,value):
        self.head=Node(value)

    def add_after(self,value):
        current=self.head
        while current.nextNode:
            current=current.nextNode

        current.nextNode=Node(value)

    def traverse(self):
        current=self.head
        while current:
            print(current.value)
            current=current.nextNode
s=sll()
s.push(1)
s.add_after(2)
s.add_after(3)
s.add_after(4)
s.traverse()