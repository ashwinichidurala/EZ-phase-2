#double linked list
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class Dll:
    def __init__(self):
     self.head=None
     class Dll:
         def __init__(self):
             self.head=None


        

node_1=Node("ashwini")
print(node_1.data)
print(node_1.next)
print(node_1.prev)
dl=Dll()
dl.head=node_1
print(dl.head)
print(dl.head.data)

node_2=Node("shashanka")
node_1.next=node_2
node_2.prev=node_1
print(node_2)
print(node_2.next)
print(node_2.prev)


node_3=Node("pranavi")
print(node_3.data)
print(node_3.next)
print(node_3.prev)
node_2.next=node_3
node_3.prev=node_2
print(node_3.data)
print(node_3.next)
print(node_3.prev)

node_4=Node("nandhini")
print(node_4.data)
print(node_4.next)
print(node_4.prev)
node_3.next=node_4
node_4.prev=node_3

print(node_4.data)
print(node_4.next)
print(node_4.prev)

class Dll:
    def __init__(self):
     self.head=None
    def __init__(self):
        self.head=None
    def insert_begining(self,data):
        new_node=Node(data)
        temp=self.head
        temp.prev=new_node
        new_node.next=temp
        self.head=new_node

        
    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.previous=temp
            
        

    def display(self):
        if self.head is None:
            print("double linked list is empty!")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end="")
                temp=temp.next



dl=Dll()
dl.display()
print()
dl.insert_end("samyu")
dl.display()
        





               












