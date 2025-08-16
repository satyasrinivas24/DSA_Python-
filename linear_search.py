#--------------------LINEAR SEARCH-----------------------------------------------------------------------
#first we need to see thr trg and in the array we want to go step by step position where is my trg if trg is there we wab=nt to upload the index of that value 
# def linear_search(arr,trg):
#     n = len(arr)
#     for i in range(n):
#         if(arr[i]==trg):
#          return i
#     return -1

# arr = [45,78,897,67,23,99]
# trg = 99
# res = linear_search(arr,trg)
# print(res)


#------------------BINARY SEARCH----------------------------------------------------------------------------------
# First if start < end then create the mid to create the mid formula is start + end //2 if yours trg is < than the mid start will be mid+1 or mid is > than trg then the end is mid -1 or -1
# def binary_search(arr,trg):
#     n = len(arr)-1
#     start = 0
#     end = n
#     while(start <= end):
#         mid = (start+end)//2
#         if arr[mid]== trg:
#             return mid
#         elif arr[mid]<trg:
#             start = mid + 1
#         elif arr[mid]>trg:
#             end = mid -1
    
#     return -1
                
# arr = [10,23,35,45,50,70,85]
# trg = 9
# res = binary_search(arr,trg)
# print(res)

"editor.quickSuggestions": false
