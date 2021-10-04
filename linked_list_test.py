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

    def add1(self,value):
        if self.head==None:
            self.head=Node(value)
        else:
            curr=self.head
            num=1
            while curr.nextNode:
                num+=1
                curr=curr.nextNode

            if curr.nextNode == None:
                self.tail=curr.nextNode=Node(value)
                self.size+=1
                # curr.nextNode.index+=num

        self.set_reverse_node() 
        
    def append1(self,value):
        curr=self.head
        num=1
        while curr.nextNode:
            num+=1
            curr=curr.nextNode

        if curr.nextNode == None:
            self.tail=curr.nextNode=Node(value)
            self.size+=1
            curr.nextNode.index+=num

        self.set_reverse_node()

    def set_reverse_node(self):
        curr=self.head
        while curr.nextNode:
            curr.nextNode.prevNode=curr
            curr=curr.nextNode

    def remove_element(self,index):
        curr=self.head
        num=0            
        while curr:
            num+=1
            curr=curr.nextNode
        
            if num == index and index != self.tail.index:
                print(f"Removing Node=Prev:{curr.prevNode.value},Index:{curr.index},Value:{curr.value},Next:{curr.nextNode.value}")
                curr.prevNode.nextNode=curr.nextNode


            if index == self.head.index:
                print(f"Removing Node=Prev:{self.head.prevNode},Index:{self.head.index},Value:{self.head.value},Next:{self.head.nextNode.value}")
                self.head=self.head.nextNode
                

            if index == self.tail.index:
                print("tail")
                print(self.tail.prevNode.value)
                print(f"Removing Node=Prev:{self.tail.prevNode.value},Index:{self.tail.index},Value:{self.tail.value},Next:{self.tail.nextNode}")
                self.tail.prevNode.nextNode=None
                break

            if index > self.size:
                print("Index Doesnt exist")
                break

    def reset_index(self):
        curr=self.head
        num=1
        while curr:
            curr.index+=num
            num+=1
            curr=curr.nextNode
        
    def insert_after(self,index,value):
        curr=self.head
        num=0
        before=self.select(index-1)
        after=self.select(index+1)
        # print(after)
        new_node=before.nextNode=Node(value)
        new_node.nextNode=after 
        new_node.prevNode=before
        after.prevNode=new_node

        # print(before.prevNode.value)
        # print(before.value)
        # print(before.nextNode.value)
        # print("")
        # print(new_node.prevNode.value)
        # print(new_node.value)
        # print(new_node.nextNode.value)
        # print("")
        # print(after.prevNode.value)
        # print(after.value)
        # print(after.nextNode.value)

        curr=self.head
        reset_num=1
        while curr:
            curr.index=0
            reset_num+=1
            curr=curr.nextNode

        self.reset_index()


    def select(self,index):
        curr=self.head
        while curr:
            if curr.index == index:
                break
            curr=curr.nextNode
        return curr

    def traverse(self):
        # self.reset_index()
        curr=self.head
        while curr:
            if curr.nextNode:
                print(f"Index:{curr.index},Value:{curr.value},Next:{curr.nextNode.value}")
                # print(f"Index:{curr.index},Previouse:{curr.prevNode},Value:{curr.value},Next:{curr.nextNode.value}")
                
            else:
                print(f"Index:{curr.index},Value:{curr.value},Next:{curr.nextNode}")
                # print(f"Index:{curr.index},Previouse:{curr.prevNode},Value:{curr.value},Next:{curr.nextNode}")

            curr=curr.nextNode

    def traverse_reverse(self):
        print("Reversing Linked List ")
        
        curr=self.tail
        while curr:
            if curr.prevNode:
                print(f"Index:{curr.index},Prev:{curr.prevNode.value},Value:{curr.value}")
            else:
                print(f"Index:{curr.index},Prev:{curr.prevNode},Value:{curr.value}")
            curr=curr.prevNode

a=dll()
a.add1(1)
for i in range(2,11):
    a.append1(i)

# a.remove_element(0)
# print(a.select(2).value)
a.insert_after(3,19)
a.traverse()
# print(a.select(6).value)
print("")
a.traverse_reverse()