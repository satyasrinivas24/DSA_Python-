class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class double_LL:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("It is Empty linklist")
        temp = self.head
        while temp is not None:
            print(temp.data,"->",end=" ")
            temp = temp.next
    def delete_first(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None
        
    def delete_end(self):
        temp = self.head.next
        before = self.head
        while temp.next is not None:
            temp = temp.next
            before = before.next
        before.next = None
        temp.prev = None
        
    def delete_position(self,pos):
        temp = self.head.next
        before = self.head
        for i in range(1,pos-1):
            temp = temp.next
            before = before .next
        before.next = temp.next
        temp.next.prev = before
            
            
        
    
    
l = double_LL()
n = Node(10)
l.head = n
n1 = Node(20)
l.head.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
l.delete_position(2)
l.display() 
        