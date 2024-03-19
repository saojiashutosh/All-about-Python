# Implement a python program to get the last 'n' elements from a list using slicing.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Enter a number of elements to print = "))
x = 10 - n
result = my_list[x:10]
print(result)
