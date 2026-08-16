"""
Instance methods :an instance method is a method that uses self to access or modify the data of a particular object.
static method : a method can be called without any object for the class using  the class name directlly .
class method : 


"""
class student:
    def __init__(self,name,clas):
        self.name=name
        self.clas=clas
    def disply(self):
        print(self.name," name of stundent ")
        print(self.clas," class the student ")

def main():
    obj=student("sunkeerth","job")
    obj.disply()

if __name__=="__main__":
    main()
    
""" static methods ."""

class sunkeerth:
    def __init__(self,comp):
        self.comp=comp
    @staticmethod
    def dob():
        print("08/06/2026")

def main():
    obj=sunkeerth("cybernetick")
    # obj.dob()
    sunkeerth.dob() # static method 

if __name__=="__main__":
    main()
    
    
""" class methods : 
    its an method in py where a method that works with the class itself rather than a particular object.
    
    use of the class methods : 
    1.access or modify the class varibales.
    2.call without creating an object.
    3.create an alernative consrttors"""

class mother:
    name="channabasama"
    age=49
    
    @classmethod
    def display(self):
        # self.age=age
        print(self.name,self.age)

mother.display()


    