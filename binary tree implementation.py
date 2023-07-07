#tree  creation and implementation

class Node:
    def __init__(self,data):
        self.data=data
        self.l_child=None
        self.r_child=None


class Tree_ds:
    def __init__(self):
        self.root=None

node_1=Node(100)
node_2=Node(200)
node_3=Node(300)

tree=Tree_ds()
tree.root=node_1

print(tree.root)
print(node_1.r_child)
print(node_1.l_child)
node_1.r_child=node_2
node_1.l_child=node_3

node_4=Node(150)
node_5=Node(500)
node_6=Node(250)
node_7=Node(700)

node_2.r_child=node_4
node_2.l_child=node_5

node_3.r_child=node_6
node_3.l_child=node_7

print("###################")
print(node_2.l_child)
print(node_2.r_child)
print(node_3.l_child)
print(node_3.r_child)
















    
