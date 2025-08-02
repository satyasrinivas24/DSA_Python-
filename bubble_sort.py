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