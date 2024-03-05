# Write a program that takes three numbers as input and determines
# the largest one using nested if-else statements. Make sure all 3 numbers
# entered by user are different.

x = int(input("Enter 1st number = "))
y = int(input("Enter 2nd number = "))
z = int(input("Enter 3rd number = "))

if(x>y):
    if(x>z):
        print("1st number is greater")
elif(y>z):
    print("2nd number is greater")
else:
    if(z>x):
        print("3rd number is greater")        
    