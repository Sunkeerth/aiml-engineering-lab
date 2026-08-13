"""pop(1) it delete an ele at index value and return the value of that index.
    syntax ==> list.pop(index)"""
    
""" del is key word we can delete an using sliceing froward and reverse"""
li=[1,2,2,2,3,4,5,6,7,8]

del li[::2]
print(li)# 2 4 6 8
li.remove(2)
print(li)

""" creating copy of the list : """
# 1
li1=li[::]
print(li1)

""" list built in functions : 
 1. max(),2. min(),3.range(),4.len(),5.enumerate(),6.any()
 7.eval(),8.sum(),9.sorted(),10.all().11.reversed()
 
 | Built-in Function | What it does (Short)                                              |
| ----------------- | ----------------------------------------------------------------- |
| `max()`           | Returns the **largest** element in an iterable.                   |
| `min()`           | Returns the **smallest** element in an iterable.                  |
| `range()`         | Generates a **sequence of numbers** (commonly used in loops).     |
| `len()`           | Returns the **number of elements** in an object.                  |
| `enumerate()`     | Returns **index and value** together while iterating.             |
| `any()`           | Returns `True` if **at least one** element is truthy.             |
| `eval()`          | **Evaluates and executes** a Python expression given as a string. |
| `sum()`           | Returns the **sum of all numeric elements**.                      |
| `sorted()`        | Returns a **new sorted list** without modifying the original.     |
| `all()`           | Returns `True` if **every** element is truthy.                    |
| `reversed()`      | Returns an **iterator** that accesses elements in reverse order.  |

 """
print(max(li))
print(min(li))
print(range(10))
print(len(li))
print(enumerate(li))
print(any(li))
print(eval("2+3"))
print(sum(li))
print(sorted(li))
print(all(li))

# pgm insert an elemet at an right index
# n=int(input(""))
li=[12,12,1,3,1,3,1,3]
i=int(input("enter the ele to insert : "))
d=1000

for j in range(0,len(li)):
    if j==i:
        li.insert(i,d)
print(li)
