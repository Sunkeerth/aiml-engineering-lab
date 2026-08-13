# lambda is single line function syntax : 
# lambda arguments : expression

"""res=lambda a,b:a+b
hi=res(10,20)
print(hi)"""

res=(lambda a,b:a+b)(10,20)
print(res)



# filter function is used to filter the data based on some condition
#  synatax = filter(function, iterable )

lst=[1,2,3,4,5,6,7,8,9]
def evn_odd(n):
    if n%2==0:
        return True
    else:
        return False
    
res1=list(filter(evn_odd,lst))
print(res1)

""" Reduce is the function which is used to perform some operation on the iterable and return a single value
syantax =reduce(functipon,itetrable)"""
from functools import reduce

def fil(x,y):
    return x+y
reduce_res=reduce(fil,lst)
print(reduce_res)

""" map is the function that applys an fun to each of element of the iterable and returns a new iterable with the results
syntax=map(function,iterable )"""

def map_fun(x):
    return x*x
map_res=list(map(map_fun,lst))
print(map_res,"map function")

# optimized way to write the above code using lambda function
map_r=list(map(lambda x:x*x,lst))
print(map_r)






