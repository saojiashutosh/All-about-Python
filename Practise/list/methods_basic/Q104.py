# Write a program that prompts the user to specify the length of a list
# and then requests numbers to populate that list.

n = int(input("Enter size of list = "))
a = []
for i in range(0, n):
    m = int(input("Enter number = "))
    a.append(m)

print(a)
