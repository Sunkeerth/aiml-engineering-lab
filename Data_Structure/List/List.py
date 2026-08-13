""" list uses an  array to store the values and it is a mutable data structure. it can store any type of data and
 it can be changed after creation. it is a ordered collection of items and it allows duplicate values. it is defined 
 by using square brackets [] and the items are separated by commas. 

Amortization where the list will create an array of fixed size and when the list is full it will create a new 
array of double the size and copy the old array to the new array. this is called amortization.


"""
# Operation of list in python: 1. Concation ,2 replication 
lst=[12,"sunkeerth",99.0,True]
lst1=[12,34,56]
print(lst+lst1) # it will print the concatenation of the two lists
print(lst*3) # it will print the replication of the list 3 times

for i in lst:
    print(i) # it will print the elements of the list one by one

for j in range(0,len(lst)):
    print(lst[j]) # it will print the elements of the list one by one using index

lst.append(100) # it will add the element 100 to the end of the list
l1=[67,6489,738]
lst.append(l1)
lst.insert(2,200) # it will add the element 200 at index 2
# print(lst) # it will print the updated list
li=[10,20,30]
lst.extend(li) # extends the list by appending at the last .
print(lst)

#  Modification : 
li[1:3]=[136,7379,739,]
print(li)

#  remove() 
li.remove(li[2])# removes the first occurrence of the specified value from the list. if the value is not present, it raises a ValueError.
print(li)

print(li.pop(1)) # removes the element at the specified index and returns it. if the index is not specified, it removes and returns the last element.
    
""" 
| **Operation**          | **Best Case**                                                    | **Worst Case**                                                                     |
| ---------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **`append(x)`**        | **O(1)** – Space is available, so the element is added directly. | **O(n)** – The list is full and must be resized (copied to a larger memory block). |
| **`extend(iterable)`** | **O(k)** – Enough space exists to add `k` elements.              | **O(n + k)** – The list must be resized and all existing elements copied.          |
| **`insert(i, x)`**     | **O(1)** – Inserting at the end (`i = len(lst)`).                | **O(n)** – Inserting at the beginning; all elements shift right.                   |
| **`pop()`**            | **O(1)** – Removes the last element.                             | **O(1)** – Always removes the last element.                                        |
| **`pop(i)`**           | **O(1)** – Removing the last element.                            | **O(n)** – Removing the first element; all remaining elements shift left.          |
| **`remove(x)`**        | **O(1)** – The element is the first item.                        | **O(n)** – The element is the last item or not present.                            |
| **`index(x)`**         | **O(1)** – The element is the first item.                        | **O(n)** – The element is the last item or not present.                            |
| **`count(x)`**         | **O(n)** – Must check every element.                             | **O(n)** – Must check every element.                                               |
| **`sort()`**           | **O(n log n)** – Average/best performance of Timsort.            | **O(n log n)** – Maximum expected time for Timsort.                                |
| **`reverse()`**        | **O(n)** – Swaps all elements.                                   | **O(n)** – Swaps all elements.                                                     |
| **`len(lst)`**         | **O(1)** – Length is already stored.                             | **O(1)** – Always constant time.                                                   |
| **`lst[i]`**           | **O(1)** – Direct indexing.                                      | **O(1)** – Direct indexing.                                                        |
| **`lst[i] = x`**       | **O(1)** – Direct update.                                        | **O(1)** – Direct update.                                                          |
| **`del lst[i]`**       | **O(1)** – Deleting the last element.                            | **O(n)** – Deleting the first element; all remaining elements shift left.          |
"""

""" # Python List Methods – Complete Explanation

A Python list is a dynamic array. Elements are stored in contiguous memory, and each element has an index starting from 0.

Example:

lst = [10, 20, 30, 40, 50]

Index:   0    1    2    3    4
        +----+----+----+----+----+
Value:  |10  |20  |30  |40  |50  |
        +----+----+----+----+----+


===============================================================================
1. append(x)
===============================================================================

Purpose:
- Adds ONE element to the END (last position) of the list.

Syntax:
lst.append(x)

Example:

lst = [10, 20, 30]

lst.append(40)

Output:
[10, 20, 30, 40]

Before:

10 20 30

After:

10 20 30 40
          ↑
      Added here

Where does it add?
✔ Last position only

Returns:
None

Time Complexity:
Best Case : O(1)
Worst Case: O(n) (if list needs resizing)


===============================================================================
2. extend(iterable)
===============================================================================

Purpose:
- Adds MULTIPLE elements to the END of the list.

Syntax:
lst.extend(iterable)

Example:

lst = [10, 20]

lst.extend([30, 40, 50])

Output:

[10, 20, 30, 40, 50]

Before:

10 20

After:

10 20 30 40 50
      ↑
Added at end

Where does it add?
✔ Last position only

Returns:
None

Time Complexity:
Best Case : O(k)
Worst Case: O(n + k)

(k = number of inserted elements)


===============================================================================
3. insert(index, value)
===============================================================================

Purpose:
- Inserts an element at ANY POSITION.

Syntax:
lst.insert(index, value)

Example 1

lst = [10,20,30]

lst.insert(0,5)

Output

[5,10,20,30]

Before

10 20 30

After

5 10 20 30
↑
Inserted at beginning


Example 2

lst.insert(2,15)

Output

[5,10,15,20,30]

5 10 15 20 30
     ↑
Inserted in middle


Example 3

lst.insert(len(lst),40)

Output

5 10 15 20 30 40
               ↑
Inserted at end

Where does it add?

✔ Beginning
✔ Middle
✔ End

Returns:
None

Time Complexity:

Best Case : O(1) (insert at end)

Worst Case: O(n) (insert at beginning)


===============================================================================
4. pop()
===============================================================================

Purpose:
- Removes the LAST element.

Syntax:
lst.pop()

Example

lst=[10,20,30]

x=lst.pop()

Output

List:
[10,20]

Removed Value:
30

Before

10 20 30
      ↑

After

10 20

Where does it remove?

✔ Last only

Returns:
Removed element

Time Complexity:

O(1)


===============================================================================
5. pop(index)
===============================================================================

Purpose:
- Removes an element at a GIVEN INDEX.

Syntax

lst.pop(index)

Example

lst=[10,20,30,40]

lst.pop(1)

Output

[10,30,40]

Before

10 20 30 40
   ↑

After

10 30 40

Everything shifts left.

Removing first element

lst.pop(0)

10 20 30 40

↓

20 30 40

Removing last element

lst.pop(len(lst)-1)

Same as

lst.pop()

Where can it remove?

✔ Beginning

✔ Middle

✔ End

Returns:
Removed element

Time Complexity

Best Case : O(1)

Worst Case: O(n)


===============================================================================
6. remove(value)
===============================================================================

Purpose:
- Removes the FIRST OCCURRENCE of a VALUE.

Syntax

lst.remove(value)

Example

lst=[10,20,30,20]

lst.remove(20)

Output

[10,30,20]

Only FIRST 20 removed.

Before

10 20 30 20
   ↑

Removed

If value doesn't exist

ValueError

Where can it remove?

✔ First matching value

Returns

None

Time Complexity

Best Case : O(1)

Worst Case: O(n)


===============================================================================
7. index(value)
===============================================================================

Purpose:
- Finds the INDEX of the FIRST OCCURRENCE.

Syntax

lst.index(value)

Example

lst=[10,20,30,20]

print(lst.index(20))

Output

1

Index

0 1 2 3

10 20 30 20
   ↑

Returns

Index number

If value not found

ValueError

Time Complexity

Best Case : O(1)

Worst Case: O(n)


===============================================================================
8. count(value)
===============================================================================

Purpose:
- Counts how many times a VALUE appears.

Syntax

lst.count(value)

Example

lst=[10,20,20,30,20]

print(lst.count(20))

Output

3

Python checks EVERY ELEMENT.

Returns

Count

Time Complexity

Best Case : O(n)

Worst Case: O(n)


===============================================================================
9. sort()
===============================================================================

Purpose:
- Sorts elements in ASCENDING ORDER.

Syntax

lst.sort()

Example

lst=[40,10,30,20]

lst.sort()

Output

[10,20,30,40]

Before

40 10 30 20

After

10 20 30 40

Descending

lst.sort(reverse=True)

Output

40 30 20 10

Returns

None

Time Complexity

Best Case : O(n log n)

Worst Case: O(n log n)


===============================================================================
10. reverse()
===============================================================================

Purpose:
- Reverses the ENTIRE LIST.

Syntax

lst.reverse()

Example

lst=[10,20,30,40]

lst.reverse()

Output

[40,30,20,10]

Before

10 20 30 40

After

40 30 20 10

Note

reverse() DOES NOT SORT.

Returns

None

Time Complexity

O(n)


===============================================================================
11. len(lst)
===============================================================================

Purpose:
- Returns NUMBER OF ELEMENTS.

Syntax

len(lst)

Example

lst=[10,20,30]

print(len(lst))

Output

3

Returns

Length

Time Complexity

O(1)


===============================================================================
12. lst[index]
===============================================================================

Purpose:
- Accesses an element using INDEX.

Syntax

lst[index]

Example

lst=[10,20,30]

print(lst[1])

Output

20

Index

0 1 2

10 20 30
   ↑

Returns

Element

Time Complexity

O(1)


===============================================================================
13. lst[index] = value
===============================================================================

Purpose:
- Updates an EXISTING ELEMENT.

Syntax

lst[index]=value

Example

lst=[10,20,30]

lst[1]=100

Output

[10,100,30]

Before

10 20 30
   ↑

After

10 100 30

Returns

None

Time Complexity

O(1)


===============================================================================
14. del lst[index]
===============================================================================

Purpose:
- Deletes an element at an INDEX.

Syntax

del lst[index]

Example

lst=[10,20,30]

del lst[1]

Output

[10,30]

Before

10 20 30
   ↑

After

10 30

Everything shifts left.

Deleting last element

del lst[-1]

10 20 30

↓

10 20

Where can it delete?

✔ Beginning

✔ Middle

✔ End

Returns

None

Time Complexity

Best Case : O(1) (last element)

Worst Case: O(n) (first element)


===============================================================================
QUICK SUMMARY
===============================================================================

append(x)
→ Add ONE element at END.

extend(iterable)
→ Add MULTIPLE elements at END.

insert(index, value)
→ Insert at BEGINNING, MIDDLE, or END.

pop()
→ Remove LAST element.

pop(index)
→ Remove element at SPECIFIC INDEX.

remove(value)
→ Remove FIRST MATCHING VALUE.

index(value)
→ Return INDEX of FIRST MATCHING VALUE.

count(value)
→ Count OCCURRENCES of a VALUE.

sort()
→ Sort ENTIRE LIST.

reverse()
→ Reverse ENTIRE LIST.

len(lst)
→ Return NUMBER OF ELEMENTS.

lst[index]
→ ACCESS an element.

lst[index] = value
→ UPDATE an element.

del lst[index]
→ DELETE an element.

===============================================================================
EASY MEMORY TRICK
===============================================================================

ADD
-----
append()          → End
extend()          → End (multiple)
insert()          → Anywhere

REMOVE
--------
pop()             → Last
pop(index)        → Anywhere by index
remove(value)     → First matching value

SEARCH
--------
index(value)      → First occurrence index
count(value)      → Count occurrences

REORDER
---------
sort()            → Arrange in ascending/descending order
reverse()         → Reverse order

ACCESS
--------
lst[index]        → Read value
lst[index]=value  → Update value

DELETE
--------
del lst[index]    → Delete by index

SIZE
------
len(lst)          → Number of elements"""