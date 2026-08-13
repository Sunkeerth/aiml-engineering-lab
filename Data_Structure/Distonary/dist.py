""" The dictionary (dict) is one of the most important data structures in Python. It is used almost everywhere in Python, 
AI/ML, web development, databases, APIs, and automation. 

    A dictionary stores data as key-value pairs, making the data meaningful and easy to understand.
    A dictionary provides very fast lookup (average O(1)), so finding a value by its key is much faster than searching through a list or tuple.
    A dictionary uses unique keys, which prevents duplicate identifiers and keeps data organized.
    A dictionary is mutable, so you can easily add, update, or remove items after it is created.
    A dictionary can store different data types (strings, numbers, lists, tuples, other dictionaries, etc.) in a single object.
    A dictionary is ideal for representing real-world objects, such as students, employees, products, and configurations.
    A dictionary supports nested dictionaries, making it suitable for storing complex and hierarchical data.
    A dictionary is widely used in JSON, APIs, databases, AI/ML, and web applications, making it one of the most important Python data structures.
    Comparison with Other Data Structures
    Compared to a list: A dictionary is better for searching by name (key), while a list is better for ordered data accessed by index.
    Compared to a tuple: A dictionary is mutable and stores labeled data, while a tuple is immutable and stores fixed ordered data.
    Compared to a set: A dictionary stores both keys and values, while a set stores only unique values.
    Compared to variables: A dictionary groups related information into a single object instead of creating many separate variables.
"""
""" Dictionary Hash Function (Short Sentence Format)
A dictionary stores data as key-value pairs.
Python uses the hash() function on the key, not the value.
The hash value determines the memory location where the value is stored.
When a key is searched, Python computes its hash and directly accesses the value.
Python does not search every element like a list, making dictionaries much faster.
Dictionary lookup, insertion, and deletion have an average time complexity of O(1).
Keys must be unique and hashable because they are used for indexing.
Values can be duplicated and can be of any data type. """

d={2:23,1:3}
print(d[2])

d[1]="sunkeerth"
print(d)

d.update({3:"ello"})
print(d)

""" 
built in methods :

1.pop()
2.popitem() pops last item
3.del d[index] delete an elmet using the index
4.clear() clears the element from the dicitonary
5. append()
6."""