#-----------------------#CIRCULAR Linked list----------------------------------------------------------------------------------
class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
class CLL:
    def __init__(self):
        self.head = None
        self.Tail = None
        
    def display(self):
    
        if self.head is None:
            print('Empty Circular Linkedlist')
        temp = self.head
        while True:
            print(temp.data,"-->",end =" ")
            temp = temp.next
            if temp == self.head:
                break
        print()
            
L=CLL()
n=Node(10)
L.head = n
L.Tail = n
L.Tail.next = L.head

n1= Node(20)
L.Tail.next = n1
L.Tail = n1
L.Tail.next = L.head


n2 = Node(30)
L.Tail.next = n2
L.Tail = n2
L.Tail.next = L.head   
L.display()

        
        