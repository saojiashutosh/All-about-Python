# Ask a number from user. Print all the numbers from 1 to that number
number = int(input("Enter a number: "))

if number < 1:
    print("Please enter a positive number.")
else:
    for i in range(1, number + 1):
        print(i)
