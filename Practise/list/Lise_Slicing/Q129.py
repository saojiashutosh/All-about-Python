# Ask ‘n’ from user. Create a list of last n elements but in reverse order using slicing.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = int(input("Enter number of elements to print = "))

x = 10 - n - 1
result = my_list[10:x:-1]

print(result)
