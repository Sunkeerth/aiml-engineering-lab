""" given an array of inegers print the largest element in array 
 n i/p and arr = i/p"""

n=int(input(" enter a n "))
arr=list(map(int,input("enter the values of arr :").strip().split()))

#  easy 
# print(max(arr))
# hard 
# ma=arr[0]
# for i in range(1,n):
#     if arr[i]>ma:
#         ma=arr[i]
#         continue
# print(ma)

""" given an array of integer print the result of the array with product of n-1 present an eelement 
 i/p = n=5 and arr = 3,4,2,1,4 and o/p = 40,24,60,120,30 .
 
 create product like 3*4*2*1*4 =120/arr[i]"""

# pr=1
# for i in arr:
#     pr=pr*arr[i]
# # print(pr)
# a1=[]
# for i in range(0,n):
#     a1.append(pr//arr[i])

# print(a1)
    
""" given an array of integers print the second largest no in in array 
input :
n=7
arr=[3 5 4 7 6 10 8]   o/p : 8 . no sorting is allowed ."""

# if arr[0]>arr[1]:
#     p=arr[0]
#     print(p)
# else:
#     vp=arr[1]
# p=0
# vp=0

# for i in range(2,n):
#     if arr[i]>p:
#         vp=p
#         p=arr[i]
#     elif arr[i]>vp:
#         vp=arr[i]

# print(vp)

""" given the sorted array int values that occurrence of each element in the array .
input :
n=8
arr=[2 2 2 3 4 4 23]     output : 
                            2 -3 times 
                            3 -1 time 
                            4 - 3 times
                            23 -2 time """
                            
                        #  it will work in sorted arry in ascending order 
                        
                            
count=1
for i in range(0,n-1):
    if arr[i]==arr[i+1]:
        count+=1
    else:
        print(arr[i],"-- times  ", count)
        count=1
        
""" given a sorted array of integer print all the elemets of array without repeating 
    input :                         output : 2 3 4 23
    n=8         
    arr=[2 2 2 3 4 4 4 23 ] """

for i in range(0,n-1):
    if arr[i]!=arr[i+1]:
        print(arr[i])
print(arr[n-1])
        
    
    

    
 
 