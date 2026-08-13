""" Set is an unordered collection. We cannot access elements using an index. 
It can store any type of data, but it does not allow duplicate elements."""

""" A set is an unordered collection of unique elements.
 It does not allow duplicate values and does not support indexing like a list.
Internally, a set uses a hash table to store its elements.

How does a hash table work?

When you insert a value into a set, Python applies a hash function to that value.

A hash function takes the value and converts it into a hash code. Using this hash code, 
it calculates the index (bucket) where the element should be stored. 

How it stores :
        Hash Index = (Sum of digits) % 11
        95
        ↓
    9 + 5 = 14
        ↓
    14 % 11 = 3
"""

""" What is a Collision?

A collision happens when two different values produce the same index. 
    Both 95 and 59 map to index 3.
    This creates a collision.
    
Collision Resolution (Separate Chaining)

One common way to solve collisions is Separate Chaining.

In separate chaining, each index points to a linked list (chain). If another element gets the same index,
 it is added to the linked list instead of replacing the existing value. 

 Hash Table

Index
-----
0
1
2
3 ----> 95 ----> 59 ----> NULL
4
5
6
7
8
9
10""" 

""" Why does a set allow only immutable data types?

A set uses a hash function to store elements in a hash table.

When you insert an element into a set:

The hash function calculates a hash value for that element.
The hash value determines the index (bucket) where the element is stored.
Later, Python uses the same hash value to find the element quickly.

For this to work, the hash value must never change.

Immutable objects

An immutable object cannot be changed after it is created.
Since its value never changes, its hash value also remains the same.
Therefore, immutable objects can be stored safely in a set.

Insert value

        "Python"
            │
            ▼
     Hash Function
            │
            ▼
     Hash Value = 2568
            │
            ▼
      Index = 2568 % 11 = 5
            │
            ▼
       Hash Table
       +---------+
Index 5│ Python  │
       +---------+
       
       """

se={12,13,15,"fdhndj",90.0}

print(se)
# print(se[len(se):0:-2])
#  error : File "/home/sunkeerth/Documents/Daily_practice/Python_pra/Data_Structure/set/set.py", line 95, in <module>
#       ^^^^^^^^^^^
# TypeError: 'set' object is not subscriptable

