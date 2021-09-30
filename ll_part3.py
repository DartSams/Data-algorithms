class Node:
    def __init__(self,value):
        self.value=value
        self.nextNode=None
        self.index=0



class sll:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert1(self,value):
        self.head=Node(value)

    def append1(self,value):
        curr=self.head
        while curr.nextNode:
            curr=curr.nextNode
        
        if curr.nextNode == None:
            tail=curr.nextNode=Node(value)
            curr.nextNode.index+=1
            self.tail=tail


    def get_size(self):
        curr=self.head
        num=0
        while curr:
            num+=1
            curr=curr.nextNode
        print(f"size:{num}")


    def traverse(self):
        curr=self.head
        while curr:
            if curr.nextNode:
                print(f"Index:{curr.index},Value:{curr.value},Next:{curr.nextNode.value}")
            elif curr.nextNode == None:
                print(f"Index:{curr.index},Value:{curr.value},Next:{curr.nextNode}")
            curr=curr.nextNode
        print("End of linked list")
        print(f"tail:{self.tail.value}")

a=sll()
a.insert1(1)
a.append1(3)
a.append1(25)
a.traverse()
a.get_size()
