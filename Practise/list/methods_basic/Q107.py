#  Ask the user for a number. Then, from a list of numbers, remove all
# the numbers that can be divided by the number the user entered. (Do on
# your own).

size = int(input("Enter size of list: "))
a = []

for i in range(size):
    num = int(input("Enter number: "))
    a.append(num)

print(a)

n = int(input("Enter a number to divide with = "))

i = 0
while i < len(a):
    if a[i] % n == 0:
        a.pop(i)
    else:
        i += 1
print(a)
