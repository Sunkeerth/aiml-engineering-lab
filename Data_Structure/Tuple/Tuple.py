""" Tuple is immutable data structure in python. It is used to store multiple items in a single variable. 
Tuple is one of 4 built-in data types in Python used to store collections of data, the other
 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is 
 ordered and unchangeable. In Python tuples are written with round brackets."""

""" Tuple is immutable data structure in python .iy use an static so it will not grow or shrinkin size. 
it is defined by using round brackets () and the items are separated by commas. it can store any type of data and
 it allows duplicate values. it is an ordered collection of items. 
"""
tu=(12,"sunkeerth",99.0,True)
print(tu)

print(tu[len(tu):0:-1])
#  tuple does'nt have append and extend method because it is immutable data structure. but we can convert the tuple 
# to list and then we can use the append and extend method to add the values to the tuple.

