""" Array is sequential collection elements of same type """
# 1. elment of even index is even and element of odd index is odd
arr=[2,3,4,5,6,7,8,9]
for i in range(len(arr)):
    if i%2==0 and arr[i]%2==0:
        print("Element of even index is even:",arr[i])
    elif i%2!=0 and arr[i]%2!=0:
        print("Element of odd index is odd:",arr[i])
