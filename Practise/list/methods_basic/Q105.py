# Create a list and prompt the user for an 'old number' followed by a
# 'new number.' If the 'old number' exists in the list, replace it with the 'new
# number' provided by the user

size = int(input("Enter size of list = "))
a = []

for i in range(0, size):
    m = int(input("Enter number = "))
    a.append(m)

print(a)

old = int(input("Enter any old number = "))
nn = int(input("Enter the new number = "))

for i in range(0, size):
    if a[i] == old:
        a[i] = nn

print(a)
