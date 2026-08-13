""" given an array of integer of the largest present in arrat"""
# Input the number of elements
n = int(input("Enter number of elements: "))

""" hen you ask a user for an array of numbers (like 5 12 7), you chain these methods 
together to get clean, usable data.input() gets the raw data: "  5 12 7  ".strip() 
cleans the outer edges: "5 12 7".split() cuts it into a list of text numbers: ['5', '12', '7']✅ 
Summary Checklist.strip() = Cleans the outer edges..split() = Chops text into a list.Would you like to see 
how to change specific split characters (like splitting by commas instead of spaces), 
or should we look at how map(int, ...) converts that final list into real numbers?"""
# arr=list(map(int(input("").strip().split())))
# Input the array elements separated by spaces
arr = list(map(int, input("Enter the array elements separated by space: ").strip().split()))

# Find and print the largest element
print("Largest element:", max(arr))

# ===================================================================================

# Sort the array in ascending order
arr.sort()

# Access the last element using slicing/negative indexing
largest = arr[-1]

print("Largest element:", largest)

# =================================================================

# smallest number in array 

sma=min(arr)
print("smallest number " , sma)

# ====

sm=arr[0]
print(sm)

# ====================================================================

ar=arr[0]
maxl=0
for i in range(0,n):
    if arr[i]>maxl:
        maxl=arr[i]
        print(" max ")

print(" max number : ",maxl)
