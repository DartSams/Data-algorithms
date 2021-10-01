class Node:
    def __init__(self,value):
        self.value=value
        self.prevNode=None
        self.nextNode=None
        self.index=0



class dll:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def insert1(self,value):
        self.head=Node(value)
        self.size+=1
        # self.head.prevNode=self.tail.value

    def append1(self,value):
        curr=self.head
        num=1
        while curr.nextNode:
            num+=1
            # self.size+=1
            curr.nextNode.prevNode=curr.value

            curr=curr.nextNode

        if curr.nextNode == None:
            self.tail=curr.nextNode=Node(value)
            curr.nextNode.index=num
            self.size+=1

    def traverse(self):
        curr=self.head
        curr.prevNode=self.tail.value
        print("")
        while curr:
            if curr.nextNode:
                curr.nextNode.prevNode=curr.value
                print(f"Index:{curr.index},Previouse:{curr.prevNode},Value:{curr.value},Next:{curr.nextNode.value}")
            elif curr.nextNode == None:
                curr.nextNode=self.head.value
                print(f"Index:{curr.index},Previouse:{curr.prevNode},Value:{curr.value},Next:{curr.nextNode}")
                break
            curr=curr.nextNode
        print("End of linked list\n")

    def traverse_reverse(self):

        curr=self.head
        curr.prevNode=self.tail.value
        print("")
        while curr:
            if curr.nextNode:
                curr.nextNode.prevNode=curr
            elif curr.nextNode == None:
                curr.nextNode=self.head
                break
            curr=curr.nextNode
            
        curr=self.tail
        for i in range(self.size):
            print(curr.value)
            curr=curr.prevNode
        

import random
a=dll()
a.insert1(1)
# for i in range(5):
#     a.append1(random.randint(0,100))
a.append1(2)
a.append1(3)
a.append1(4)
a.append1(5)
a.traverse()
# a.traverse_reverse()