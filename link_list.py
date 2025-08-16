#------------------------------Creating the link list---------------------------------------------------------------------

# class Node:
#     def __init__(self,data):
#         self.data= data
#         self.next = None
        
# class Single_LL:
#     def __init__(self):
#         self.head = None
# #------------INSERTING   --------------------------------------------------------------------------------------------------

#     def insert_starting(self,data):
#         nb =Node(data)
#         nb.next = self.head
#         self.head = nb
        
#     def insert_end(self,data):
#         ne = Node(data)
#         temp = self.head
#         while temp.next is not None:
#             temp = temp.next
#         temp.next = ne
            
            
#     def insert_position(self,pos,data):
#         np = Node(data)
#         temp = self.head
#         for i in range(pos-1):
#             temp = temp.next
#         np.data = data
#         np.next = temp.next
#         temp.next = np
             
#     def display(self):
#         if self.head is None:
#             print("Linked List is empty")
#         else:
#             temp = self.head
#             while temp != None:
#                 print(temp.data,"->",end=" ")
#                 temp = temp.next 
# l = Single_LL()
# n = Node(10)
# l.head = n
# n1=Node(20)
# l.head.next = n1
# n2 = Node(30)
# n1.next = n2
# n3 = Node(40) 
# n2.next = n3
# n4 = Node(50)
# n3.next = n4 
# l.insert_starting(5)
# l.insert_end(7)
# l.insert_position(4,35)
# l.display()
    
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Single_LL():
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("IT is not a Linked list")
        else:
            temp = self.head  
            while temp is not None:
                print(temp.data , '->',end=" ")
                temp = temp.next
    def insert_first(self,data):
        nb = Node(data)
        #temp = self.head
        nb.next = self.head
        self.head = nb
    def insert_middle(self,data,pos):
        nm = Node(data)
        temp = self.head
        for i in range (pos-1):
            temp = temp.next
        nm.next = temp.next
        temp.next = nm
    def insert_end(self,data):
        Ne = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Ne
                
                
            
        
            
    
        
l = Single_LL()
n = Node(43)
l.head = n
n1 = Node(56)
l.head.next = n1
n2 = Node(89)
n1.next = n2
n3 = Node(39)
n2.next = n3
l.insert_first(1)
l.insert_middle(55,3)
l.insert_end(12)
l.display()



                    

