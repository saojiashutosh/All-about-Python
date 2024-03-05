# Create a program that calculates the price of a movie ticket based on
# the age of the customer. If the customer is under 12, the ticket costs $5; if
# # they are between 12 and 65, the ticket costs $10; otherwise, it's $7.

age = int(input("Enter the age of the customer = "))

if(age < 12):
    print(" the ticket costs $5")
elif (12 < age < 65 ):
    print("the ticket costs $10")
else:
    print("the ticket costs $7")