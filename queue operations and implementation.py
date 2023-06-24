#Queue implementation

queue=[]
def enqueue_element():
    if len(queue)==n:
        print("queue is full")
    else:
        
        element=input("enter the element for queue")
        queue.append(element)
        print(queue)

def dequeue_element():
    if not queue:
        print("queue is empty,add any element")
    else:
        e=queue.pop(0)
        print(e,"removed")
        print(queue)

n=int(input("enter the size of queue"))
while True:
    print("select the operation 1.enqeue 2.dequeue 3.exit")
    choice=int(input())
    if choice==1:
        enqueue_element()
    elif choice==2:
        dequeue_element()
    elif choice==3:
        break
    else:
        print("ENTER THE CORRECT OPERATION!")
    
        
