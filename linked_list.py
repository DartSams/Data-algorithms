# class linkedListNode:
#     def __init__(self,value):
#         self.value=value
#         self.nextNode=None

# node1=linkedListNode(3)
# node2=linkedListNode(7)
# node3=linkedListNode(10)

# node1.nextNode=node2 #3->7
# node2.nextNode=node3 #7->10


# currentNode=node1
# while True:
#     print(currentNode.value)
#     if currentNode.nextNode is None:
#         break
#     else:
#         currentNode=currentNode.nextNode

# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.nextNode=None
    

# class linkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None

#     def push(self,value):
#         node=Node(value)
#         if self.head is None:
#             self.head=Node(value)
        
        
#         currentNode=self.head
#         while True:
#             if currentNode.nextNode is None:
#                 currentNode.nextNode=node
#                 break
#             else:
#                 currentNode=currentNode.nextNode

# ll=linkedList()
# ll.push(3)
# # ll.push(7)
# # ll.push(10)
# print(ll)



# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.nextNode=None


# class ssl:
#     def __init__(self):
#         self.head=None

#     def push(self,value):
#         node=Node(value)
#         if self.head is None:
#             self.head=node

#         # last = self.head
#         # while (last.nextNode):
#         #     last = last.nextNode
 
#         # # 6. Change the next of last node
#         # last.nextNode =  node

#         # if self.head is not None:
#         #     current=self.head
#         #     while current.nextNode:
#         #         current=current.nextNode
            
#         #     current.nextNode=node

#         if self.head.value and self.head.nextNode is None:
#             current=self.head
#             while current.nextNode:
#                 current=current.nextNode
            
#             current.nextNode=node

        
#     def traverse(self):
#         current=self.head
#         # while current:
#         #     print(current.value)
#         #     current=current.nextNode
#         print(self.head.value)
#         print(self.head.nextNode)
            

# # s=ssl()
# # s.push(1)
# # s.push(2)
# # s.push(3)
# # s.traverse()



# class Node2:

#     def __init__(self, data=None, next_node=None):
#         self.data = data
#         self.next_node = next_node

#     def get_data(self):
#         return self.data

#     def get_next(self):
#         return self.next_node

#     def set_next(self, new_next):
#         self.next_node = new_next

# class ll:
#     def __init__(self):
#         self.head=None

#     def add(self,value):
#         node=Node2(value)
#         node.set_next(self.head)
#         self.head=node.data
#         print(f"{node.get_data()} - {node.get_next()}")

#     # def traverse(self):
#         # print(Node2.get_data())
#         # current=self.head
#         # while current:
#         #     print(current.value)
#         #     current=current.nextNode
#         # print(self.head.data)
#         # print(self.head.nextNode)


# a=ll()
# a.add(2)
# a.add(3)
# a.add(4)
# a.traverse()



# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.nextNode=None

#     def get_data(self):
#         return self.value

#     def set_next(self,new_next):
#         self.nextNode=new_next

# class sll:
#     def __init__(self):
#         self.head=None

#     def add_at_beginning(self,value):
#         node=Node(value)
#         # node.nextNode=self.head
#         # self.head=node

#         if self.head is None:
#             self.head=node


#     def add_after(self,value):
#         current=self.head
#         while current.nextNode:
#             current=current.nextNode
        
#         current.nextNode=Node(value)

            

#     def traverse(self):
#         # print(self.head.value)
#         # print(self.head.nextNode.value)

#         if self.head is None:
#             print("List has no element")
#             return
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.value , " ")
#                 n = n.nextNode
 

# s=sll()
# s.add_at_beginning(2)
# s.add_after(3)
# s.add_after(4)
# s.add_after(5)
# s.traverse()




class Node:
    def __init__(self,value,previousNode=None,nextNode=None):
        self.previousNode=previousNode
        self.value=value
        self.nextNode=nextNode

class sll:
    def __init__(self):
        self.head=None
        self.taile=None

    def insert(self,value):
        node=Node(value,None,self.head)
        self.head=node

    def add(self,value):
        current=self.head
        while current.nextNode:
            previous=current.previousNode
            current=current.nextNode

        current.nextNode=Node(value,current.previousNode)

    def remove(self,place):
        num=0
        current=self.head
        while current.value:
            if num == place-1:
                current.nextNode=current.nextNode.nextNode
                break
            current=current.nextNode
            num+=1

    def traverse(self):
        current=self.head
        while current.value:
            print(current.value)
            
            if current.nextNode is None:
                print("End onf linked list")
                break
            else:
                current=current.nextNode
x=[1,2,3,4,5,6,9,7]


lst=sll()
lst.insert(x[0])
for i in x:
    lst.add(i)
lst.traverse()