""" it cn store any kind of datypes
 it has methods like : 
 1. add()
 2. pop()
 3. append()
 4. remove() it will give an error if lement is not prent in the set.
 5 .discard()
 6 ..update()"""

se={12,23,23,849.293,"sunkeerth"}
# TypeError: unhashable type: 'list'
print(se.add("hii")," add ")
print(se)
print(se.pop()," pop ")
print(se)
print(se.remove(23), " remove ")
print(se.discard(23),"discard")
print(se)

print(se.update({"yeelo"}))

""" set operations :
     
    1. union :
        where the eelements will be same repated will repet only once .
        syntax : ,union()
        """
se={12,12,13,14}
se1={123,14,13,535}
print(se|se1)

# intersection : comment elemets from set 1 and set2 common  elemets are the given by the intersection.
print(se.intersection(se1))

# Difference is where elements from set1 - set2 where elemets from set2 is removed from set1 and set1 is returned

print(se.difference(se1))
