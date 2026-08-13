""" given an array of integer value k. print the number of occurence of k """
n=int(input(" enter the num : "))
arr=list(map(int,input(" enter th earr elemets : ").strip().split()))
# k=int(input(" enter th ek value : "))
# count=0
# for i in range(0,len(arr)):
#     if k == arr[i]:
#         count+=1
# +=========================================

# for i in arr:
#     if k == i:
#         count+=1

# ==============================

# print(arr.count(k)," count of the k value present in arr ")

# print(count)

# ==============================================================================
# for i in range(0,n):
#     if k ==arr[i]:
#         print(i)

# =======================================================
# given an array of integers print the max and min numbers sum of n-1 elemets present in the array

sum=0
for i in arr:
    sum+=i
# print(sum)
arr1=list()
for j in range(0,n):
    arr1=sum-j
print(arr1)

