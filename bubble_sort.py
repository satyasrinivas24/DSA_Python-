#--------------Bubble sort--------------------------------------------------------------------------------------------
# comparing with beside terms if there smaller number there need to swap otherwise leave like that

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
                        
arr = [6,2,5,1,6,3]
sorted_arr = bubble_sort(arr)
print(sorted_arr)


#-------------------------------------Selection Sort --------------------------------------------------------------------------------
# first take in a array first element and compare with the all element in the array if it is smaller than other elemnts swap first to that elemnt


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i+1,n):
            if arr[j]< arr[min_index]:
                arr[min_index],arr[j]=arr[j],arr[min_index]
    return arr   
arr = [12,25,11,34,50,22]
sorted_arr = selection_sort(arr)
print(sorted_arr)

#-----------------------Interstion Sort --------------------------------------------------------------------------------------------------------
# first check arry if arr[0]and arr[1] compare if this correct leave if not change the index of array then check like to all the indexes 


def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):

    
    
    
arr = [22,56,10,5,42,67,32]
sorted_arr = insertion_sort(arr)
print(sorted_arr)