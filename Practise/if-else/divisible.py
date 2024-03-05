# Write a program that takes two numbers as input and checks if the
# first number is divisible by the second.

x = int(input("Enter first number = "))
y = int(input("Enter second number = "))

if(x%y==0):
    print("First number is divisible by second number")
else:
    print("First number is not divisible by second number")