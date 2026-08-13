#  prime numbers
n=int(input("Enter a number: " ))
def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            # print(i)
            return False
    return True
# print(prime(n))
# res=prime(n)
# print(res," **")

for j in range(2,n+1):
    if prime(j):

        print(j)

# Print Prime Numbers from 2 to N

# count=0
# l=2
# while count<n:
#     if prime(l):
#         print(l)
#         count+=1
#     l+=1
# print("Total prime numbers from 2 to",n,"is:",count)

# """ given 2 integer x and n print all th emultiples of n till x"""

# n1=int(input("Enter the first number: ")  )
# x2=int(input("Enter the second number: ")  )
# l2=1
# for i in range(1,x2+1):
#     if i%n1==0:
#         print(i)

# """given 3 integer a,b,n printy common multiple of a and b till n"""

# a=int(input("Enter the first number: ")  )
# b=int(input("Enter the second number: ")  )
# n=int(input("Enter the number till u need : ")  )

# for i in range(1,n+1):
#     if i%a==0 and i%b==0:
#         print(i)

# """ given a,b,n print all first n common multiples of a and b"""
# count=1
# i=1
# while count<=n:
#     if i%a==0 and i%b==0:
#         print(i)
#         count+=1
#     i+=1