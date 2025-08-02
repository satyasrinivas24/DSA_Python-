#--------------Bubble sort--------------------------------------------------------------------------------------------
# comparing with beside terms if there smaller number there need to swap otherwise leave like that

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
                        
# arr = [6,2,5,1,6,3]
# sorted_arr = bubble_sort(arr)
# print(sorted_arr)


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
arr = [2,5,8,9,45]
sorted_arr = selection_sort(arr)
print(sorted_arr)