class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node_1=("ashu")

node_2=Node(10)
node_3=Node(20)
node_4=Node(40)
node_5=Node(50)
node_6=Node(80)



class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("empty circulur linked list")
        else:
            temp=self.head
            while temp.next !=sef.head:
                print(temp.data)
                temp=temp.next
                print(temp.data,"-->",end)
                print(temp.next.data)
    def insert_begining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head

    def insert_end(self,data):

        new_node=Node(data)
        if self.head  is None:
            self.=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.tail
            self.tail=new_node
            self.tail.next=self.head

    def  delete_begining(self):
        
                
            
            
print(node_1)
print(node_2)
print(node_3)
print(node_4)
print(node_5)
print(node_6)
            
        
cl=CLL()
cl.head=node_1
cl.tail.next=node_1
cl.tail=cl.head



print(node_1.next)
print(cl.tail.next)
print(node_2.next)

cl.display()



#find the length of the circulur linked list
def len_cll():
    



