# Strings way of writing the string in python
# 1. Single quotes, 2. Double quotes, 3. Triple quotes, 4. Raw string, 5. Unicode string

s="Hello World "
print(s[0]) # accessing the first character of the string
print(s[0:5]) # accessing the first 5 characters of the string

#  checking the addres of string in python
print(id(s))

#  internally string uses an dictionary to store the string and its address is stored in the dictionary. so if we create a new string with the same value as the previous string then it will not create a new string in the memory but it will point to the same address of the previous string.
# example:
s1="Hello World "
print(id(s1)) # it will print the same address as s because both the strings have
    # the same value.

# String scilicing :
h1="Hello World"
print(h1[0:7]) # it will print the first 7 characters of the string
print(h1[-1:-13:-2]) # it will print the string in reverse order

""" String Comparaction :
1. == : it checks the value of the string
2. is : it checks the address of the string
3. id() : it returns the address of the string
4. len() : it returns the length of the string
5. in : it checks if the string is present in the string or not
6. not in : it checks if the string is not present in the string or not
7. upper() : it converts the string to uppercase
8. lower() : it converts the string to lowercase
9. title() : it converts the first character of each word to uppercase

"""
st="sunkeerth"
st1="sanketha"
st2="sunkeerth"
print(st==st1," == ") # it will return False because the value of the strings are different
print(st==st2," == ") # it will return True because the value of the strings are same
print(st is st1," is ") # it will return False because the address of the strings are different
print(st is st2," is ") # it will return True because the address of the strings are same
print(id(st)," id ") # it will return the address of the string
print(id(st1)," id ") # it will return the address of the string
print(len(st)," len ") # it will return the length of the string
print(len(st1)," len ") # it will return the length of the string
print(len(st2)," len ") # it will return the length of the string
print("sun" in st," in ") # it will return True because the string "sun" is present in the string "sunkeerth"
print("keerth" not in st1," not in ") # it will return True because the string "keerth" is not present in the string "sanketha"
print(st.upper()," upper ") # it will return the string in uppercase
print(st1.lower()," lower ") # it will return the string in lowercase
print(st2.title()," title ") # it will return the string with the first character of each word in uppercase