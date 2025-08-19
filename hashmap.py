#------------------------------------------HASHMAP-----------------------------------------------------------------------------
# arr = [1,5,8,0,1,8,1,5,1]
# n = len(arr)
# dict = {}
# for i in range(n):
#     val = arr[i]
#     if val not in dict:
#         dict[val]=1
#     else:
#         dict[val] = dict[val]+1 
# print(dict)
        
        
#------------------------------------factorial-----------------------------------------------------------------------------

# def factorial(n):
#     if(n==1):
#         return 1
#     else:
#         fact = factorial(n-1)*n
#         return fact
    
# s = factorial(5)
# print(s)

#----------------------Sum of natural numbers------------------------------------------------------------------------------------
# if n vale 1 is return 1 if not upto n-1 for n = 5 (n-1) need to be add 1+2+3+4 = 10 next return the sum +n sum = 10 add n to itt
# def sum_of_natural_numbers(n):
#     if n==1:
#         return 1
#     else:
#         sum = sum_of_natural_numbers(n-1)
#         return n+sum
# s = sum_of_natural_numbers(6)
# print(s)

#------------------------------------------Fibonicci-------------------------------------------------------------------------------------
# if n = 0 or n= 1 return should 1 or fib(4) last two number should add to get the fib(4)

#
# def fibonicci(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     last = fibonicci(n-1)
#     last_second = fibonicci(n-2)
#     res = last + last_second 
#     return res
# s = fibonicci(4)
# print(s)

