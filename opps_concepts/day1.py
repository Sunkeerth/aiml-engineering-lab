class bug:
    specific = 192.20 # class attributes and instance variable 
    def __init__(self,a1,a2):
        self.a1=a1 # instance attributes
        self.a2=a2 
bug1=bug(11,12)
# setattr(bug1,100,200)
print("bug2 using setattr : ",bug1)
print(bug1.__dict__,"instance variable ")
print(bug1.a1)
print(bug1.a2)

""" can the 1 fun can sent as argument to another function """

def alpha(sel):
    print("inside the alpha()")
    sel()

def beta():
    print("inside the beta ()")

alpha(beta)

""" 
output :

    inside the alpha()
    inside the beta ()"""

""" can function is be passed as ouput from another function ."""

def suma(lst):
    print(sum(lst))
def product(pr):
    p=1
    for i in pr:
        p=p*i
    print(p)

def sol(chooice):
    if chooice=='suma':
        return suma
    else:
        return product

hel=sol('suma')
hel1=sol('product')
lst=[102,1830,1930]
hel(lst)
hel1(lst)


# __init__ is an intilization

# creating an instance variable 
#  1 normal creation 
#  setattr() after creating an object.

#  all the instance variable is stored in the dictionary " __dict__"

