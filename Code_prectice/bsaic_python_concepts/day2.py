#  given 2 integer values n1,n2 print common factor of n1 anf n2 
n1=int(input("Enter first integer: ")  )
n2=int(input("Enter second integer: ")  )
print("Common factors of", n1, "and", n2, "are:")
for i in range(1, n1+1):
    if n1%i==0 and n2%i==0:
        print(i," ")

#  given 2 integer values n1,n2 print common factor of n1 anf n2 in reverse oder start from n1 to 1

print("Common factors of", n1, "and", n2, "are:")
for i in range(n1, 0, -1):
    if n1%i==0 and n2%i==0:
        print(i," ")


#  HCF highest common factor of n1 and n2 or gratest common divisor of n1 and n2

for i in range(n1,0,-1):
    if n1%i==0 and n2%i==0:
        print("HCF of", n1, "and", n2, "is:", i)
        break
    
#  more effiecient way to find HCF of n1 and n2 is using Euclidean algorithm
ma=max(n1,n2)
mi=min(n1,n2)
while mi!=0:
    re=ma%mi
    ma=mi
    mi=re
print("HCF of most effiecient way ", n1, "and", n2, "is:", ma)

#  LCM (Least Common Multiple) of n1 and n2
lcm=(n1*n2)//ma
print("LCM of", n1, "and", n2, "is:", lcm)
