class Node:
    def __init__(self,value):
        self.value=value
        self.nextNode=None
        self.index=0



class sll:
    def __init__(self):
        self.size=0
        self.head=None
        self.tail=None

    def insert1(self,value):
        self.head=Node(value)
        self.size+=1

    def append1(self,value):
        num=1
        curr=self.head
        while curr.nextNode:
            curr=curr.nextNode
            num+=1
        
        if curr.nextNode == None:
            tail=curr.nextNode=Node(value)
            curr.nextNode.index=num
            self.tail=tail
            self.size+=1
        
    def pop1(self,index):
        curr=self.head

        if index == self.head.index:
            self.head=curr.nextNode
            return
        
        elif index > self.tail.index:
            print("Index non existant")

        elif index == self.tail.index:
            curr=self.head
            while curr:
                curr=curr.nextNode

                if curr.nextNode.nextNode.index == index:
                    print("end")
                    curr.nextNode.nexNode = None
                    break
        while curr:
            if curr.index == index-1:
                print(f"Removing=Index:{curr.index},Value:{curr.value},Next:{curr.nextNode.value}")
                curr.nextNode=curr.nextNode.nextNode

            curr=curr.nextNode

    def get_size(self):
        curr=self.head
        self.size=0
        while curr:
            self.size+=1
            curr=curr.nextNode
        print(f"size:{self.size}")
        return self.size


    def traverse(self):
        curr=self.head
        while curr:
            if curr.nextNode:
                print(f"Index:{curr.index},Value:{curr.value},Next:{curr.nextNode.value}")
            elif curr.nextNode == None:
                print(f"Index:{curr.index},Value:{curr.value},Next:{curr.nextNode}")
            curr=curr.nextNode
        print("End of linked list")

a=sll()
a.insert1(1)
a.append1(3)
a.append1(5)
a.append1(25)
# a.traverse()
a.pop1(3)
a.traverse()