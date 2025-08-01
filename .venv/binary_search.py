def binary_search(arr,trg):
    n = len(arr)-1
    start = 0
    end = n
    while(start <= end):
        mid = (start+end)//2
        if arr[mid]== trg:
            return mid
        elif arr[mid]<trg:
            start = mid + 1
        elif arr[mid]>trg:
            end = mid -1
    
    return -1
                
arr = [10,23,35,45,50,70,85]
trg = 50
res = binary_search(arr,trg)
print(res)