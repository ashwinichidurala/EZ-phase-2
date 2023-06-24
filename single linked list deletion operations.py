#deleteing at begining,end,specific position in single linked list

#****delete at begining****
def delete_begining(self):
    temp=self.head
    self.head=temp.next
    temp.next=None
delete_begining()
sl.display()

  
#****delete at end****
def delete_end(self):
    prev=self.head
    temp=self.head.next
    while temp.next is not None:
        temp=temp.next
        prev=prev.next
    prev.next=None
    
sl.delete_end()
sl.display()
        

#****delete at specific position****    

def delete_specficpos(self,pos):
    prev=self.head
    temp=self.head.next
    for i in range(1,pos-1):
        temp=temp.next
        prev=prev.next
        prev.next=temp.next

sl.delete_specificpos(2)
sl.display()
        
    
