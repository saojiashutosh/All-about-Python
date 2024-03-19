# Ask ‘n’ from user. Create a list of first n elements but in reverse order using slicing

my_list = [23, 54, 78, 43, 12, 34, 89]
n = int(input("enter number of elements to print = "))

result = my_list[n - 1 :: -1]

print(result)
