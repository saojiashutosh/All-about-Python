# Ask a number from user. Print the multiplication table of that number.

x = int(input("Enter a number = "))
for i in range(1,11):
    print(x," * ",i," = ",x*i)
    