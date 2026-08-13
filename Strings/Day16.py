"""Strings are immutable collection of characters
Strings functions : """

# ord() : it returns the asci valuecode code point for a given character.
s1="sunkeerth"
s2='sanketha'
print(ord('a'))

# chr() : it returns the character that represents the specified unicode code point.
print(chr(97),"chr fun") # it will return 'a' because the unicode code point for 'a' is 97
print(chr(ord(s1[0])),"chr fun") # it will return 's' because the unicode code point for 's' is 115

# upper() : it converts the string to uppercase
print(s1.upper(),"upper fun") # it will return 'SUNKEERTH' because

# lower() : it converts the string to lowercase
print(s2.lower(),"lower fun") # it will return 'sanketha' because

# join() : it joins the elements of an iterable (e.g. list, tuple) into a single string, with a specified separator.
lst=["sunkeerth","sanketha","suneerth"]
print("".join(lst),"join fun") # it will return 'sunkeerth sanketha

# .startswith() : it checks if the string starts with the specified prefix
print(s1.startswith("sun"),"startswith fun") # it will return True because the string

# endswith() : it checks if the string ends with the specified suffix
print(s2.endswith("tha"),"endswith fun") # it will return True because the

# .isnumeric() : it checks if all the characters in the string are numeric
print(s1.isnumeric(),"isnumeric fun") # it will return False because the string "sunkeerth" contains non-numeric characters

# .isalpha() : it checks if all the characters in the string are alphabetic
print(s2.isalpha(),"isalpha fun") # it will return True because the string "

# .isalnum() : it checks if all the characters in the string are alphanumeric
s3="sunkeerth123"
print(s3.isalnum(),"isalnum fun") # it will return True because the string

# .isspace() : it checks if all the characters in the string are whitespace
s4="   "
print(s4.isspace(),"isspace fun") # it will return True because the string

# .maketrans() : it returns a translation table that can be used with the translate() method to replace specified characters in a string with other characters.
s5="sunkeerth"
translation_table = str.maketrans("sunkeerth", "SUNKERTH")
print(s5.translate(translation_table),"maketrans fun") # it will return 'S







