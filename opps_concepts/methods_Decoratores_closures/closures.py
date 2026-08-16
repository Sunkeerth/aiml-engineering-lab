""" 
Closures : its an concepts that when an outer fuction is deleted and the inner function is still present through the variables in 
 outer got deleted the inner function will still have the access to those varibale .
     
     Beaciuse of the values in the memory will be present .

"""

def outer():
    c=101010
    def inner():
        print(c, " inner ")
    return inner
res=outer()
# res()  # output : 101010  inner 
del outer
# res()  # ater the deleting an the 

