#  Calculate factorial of a number entered by user.

i = int(input("Enter a number = "))
j=1
fact=1
while(j<=i):
    fact=fact*j
    j+=1
print(fact)     