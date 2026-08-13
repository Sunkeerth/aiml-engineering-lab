""" String Formating : it way of inserting an value in the plceholder whate the formate will plce the values.
    syntax ==> string.formate(*args).
    
    
    """
st="sunkeerth {} {}".format("hii"," = hello")
# print(st)
""" we can also chage way of representing :
    1.{>} right alignment
    2.{<} left 
    3.{^} center"""

st1="{0:*>10}".format("123")
st2="{0:*<10}".format("123")
print(st1)
print(st2)

""" String replication :"""
su="sunkeerth"
print(su*2)

# f liternal 

print(f"{su}")
# raw string 
suu="sun\keerth"
sun=r"fhg\g"
print(suu)
print(sun)