# global variable :  variables that is stored in the global memory and can be accessed from anywhere in the program.
# local variable : variables that is stored in the local memory and can be accessed only within the
""" global is stored in the stack memory and local is stored in the heap memory. """
x=99
def fu():
    y=282
    print(x)
    print(y)
print(x) # accessing global variable outside the function
fu()

#  recursion : a function that calls itself is called recursion
def fact(n):
    if n==1:
        return 1
    else:
        fact_res=fact(n-1)*n
        return fact_res
res=fact(5)
print(res)
