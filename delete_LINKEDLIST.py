class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Single_LL():
    def __init__(self):
        self.head = None
        
    def display(self):
        if self.head is None:
            print("IT is a Empty LL")
        temp = self.head
        while temp is not None:
            print(temp.data,"->",end=" ")
            temp = temp.next
            
    def delete_first(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        
    def delete_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
        
    def delete_position(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            prev = prev.next
            temp = temp.next
        prev.next = temp.next
        
        
l = Single_LL()
n = Node(23)
l.head = n
n1 = Node(45)
l.head.next = n1
n2 = Node(60)
n1.next = n2
n3 = Node(90)
n2.next = n3
n4 = Node(65)
n3.next = n4
#l.delete_first()
#l.delete_end()
l.delete_position(3)
l.display()
            
                