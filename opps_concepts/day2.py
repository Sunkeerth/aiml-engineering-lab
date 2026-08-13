"""1. Encapsulation. 
    Encapsulation is hiding unnecessary implementation details from the user and 
    providing controlled access to the data.
    
    """

class Bank:
    def __init__(self,owner,acc_type,acc_pin):
        #1. Public / Default (No underscore)
        self.owner=owner
        
        # 2. Protected (Single underscore)
        # Signifies: "Internal use or subclasses only"
        self._acc_type=acc_type
        
        
        self.__acc_pin=acc_pin
        
account=Bank("sunkeerth","saving",2003)

# PUBLIC: Works fine
print(account.owner)

# PROTECTED: Technically works, but bad practice!
print(account._acc_type)

#  PRIVATE: Raises an AttributeError!
# print(account.__acc_pin)       # AttributeError: 'account' object has no attribute '__acc_pin'
# print(account.__acc_pin)

#  how doe sit works for the others way but we not need to practice .
# object._classname__private variable.
print(account._Bank__acc_pin)



""" 
 How It Works Internally: Name Mangling
When you use a double leading underscore (__pin), Python does not encrypt the data or make it physically impossible to read. 
Instead, the Python interpreter performs name mangling at bytecode compilation time.

The Internal Transformation
When Python sees an attribute named __pin inside a class named BankAccount, it automatically 
rewrites the attribute's internal name to:

_ClassName__attributeName → _BankAccount__pin

Why does Python do this? : 

Preventing Accidental Overrides: If a subclass also defines a variable named __pin, their names won't collide because 
    the mangled names will include their respective class names (_SubClass__pin vs. _BankAccount__pin).
Preventing Accidental Access: It stops developers from casually reaching into an object and changing sensitive state 
    (account.__pin = 0000 will fail).
The Candor Note: Because Python only renames the attribute, you can still technically access a private variable 
    from the outside if you use its mangled name:"""
    
# Controlled Access: The Pythonic Way (@property)
# To provide true controlled access (encapsulation) without letting users modify private variables directly, 
# Python uses the @property decorator to create getters and setters:

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private

    @property
    def balance(self):
        """Getter: Read-only access to balance."""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter: Controlled write access with validation."""
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount
bal=BankAccount(1000)
print(bal.balance)  # Accessing the balance using the getter
bal.balance = 1500  # Updating the balance using the setter
print(bal.balance)  # Accessing the updated balance
