""" Decorators : 
    In simplest terms, a decorator is a function that takes another function, adds some new functionality to it, and returns it.
Think of it like putting a case on your phone. The phone (your function) still does exactly what it did before, but the case (the decorator) adds extra features like drop protection or a kickstand without you having to alter the phone itself.
Here is a complete, copy-pasteable guide to Python decorators, organized from basic to advanced. You can drop this entire block of code directly into VS Code to run it and keep it as a reference.

The Prerequisites: Functions are Objects :
To understand decorators, you only need to know two rules in Python:
Functions can be passed as arguments to other functions.
Functions can be defined inside other functions.

"""

from textwrap import wrap
import time

from sympy import fu

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        
        res=func(*args,**kwargs)
        end=time .time()
        print(f"{func.__name__} {start-end}")
        return res
    return wrapper
@timer
def examp(n):
    time.sleep(n)
    
examp(2)

def outer(ref):
    def inner(a,b):
        if b==0:
            print("provide non zero element")
        else:
            print("inside the else : ")
            ref(a,b)
    return inner
@outer
def dive(a,b):
    print(a/b)

dive(10,2)
    

    