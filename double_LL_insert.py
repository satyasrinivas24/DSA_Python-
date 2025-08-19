#----------------------------------Double LL INsert-------------------------------------------------------------------------------

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class dll:
    def __init__(self):
        self.head=None
        
    def display(self):
        if self.head is None:
            print("It is Empty Linkedlist")
        temp = self.head
        while temp is not None:
            print(temp.data,'->',end = " ")
            temp = temp.next
            
    # def insert_first(self,data):
    #     nf = Node(data)
    #     temp = self.head
    #     temp.prev = nf
    #     nf.next = temp
    #     self.head = nf
    def insert_first(self,data):
        n = Node(42)
        temp = self.head
        temp.prev = n
        n.next = temp
        self.head = n
        
    def insert_end(self,data):
        n = Node(data)
        temp =self.head
        while temp.next is not None:
            temp = temp.next
            
        temp.next = n
        n.prev = temp
        
    def insert_position(self,pos,data):
        n = Node(data)
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        n.prev = temp
        n.next=temp.next
        temp.next = n
        
        
        
        
l = dll()
n = Node(10)
l.head = n
n1 = Node(20)
l.head.next = n1
n2 = Node(30)
n1.next = n2
n3 =Node(40)
n2.next = n3
#l.insert_first(5)
# l.insert_end(59)
l.insert_position(3,77)
l.display()       