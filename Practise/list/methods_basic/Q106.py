# Remove all the even numbers from the list.

size = int(input("Enter size of list: "))
a = []

for i in range(size):
    num = int(input("Enter number: "))
    a.append(num)

print(a)

i = 0
while i < len(a):
    if a[i] % 2 == 0:
        a.pop(i)
    else:
        i += 1

print(a)
