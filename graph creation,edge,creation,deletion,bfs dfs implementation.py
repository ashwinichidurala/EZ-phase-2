def add_node(v):
    if v in graph:
        print(f"the given {v} is already in the graph")
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not preaent")
    if v2 not in graph:
        print(v2,"is not present")
    else:
        #list1=[v2,cost]
        #list2=[v1,cost]
        graph[v1].append(v2)
        graph[v2].append(v1)

def del_node(v):
    if v not in graph:
        print(f"the given node {v} is not present")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)
def del_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present")
    if v2  not in graph:
        print(v2,"is not present")
    else:
        if v1 in graph[v2]:
            graph[v2].remove(v1)
        if v2 in graph[v1]:
            graph[v1].remove(v2)

#depth for search
def DFS(node,graph):
    visited=set()
    if node not in graph:
        print("Node is not present in graph")
        return
    stack=[]
    stack.append(node)
    while stack:
        current=stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)
            
    
    
#breadth first search
def BFS(node,graph):
    visited=set()
    queue=[]
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        visited.add(m)
        for n in graph[m]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    
        

graph={}
print(graph)
add_node("a")
print(graph)
add_node("b")
add_node("c")
add_node("d")
add_node("e")
add_node("f")
print(graph)

add_edge("a","b")
add_edge("a","d")
add_edge("a","e")
add_edge("d","c")
print(graph)
#del_node("a")
print(graph)
#del_edge("d","c")
print(graph)
print("DEPTH FIRST SEARCH")
DFS("a",graph)
print("BREADTH FIRST SEARCH")
BFS("a",graph)
