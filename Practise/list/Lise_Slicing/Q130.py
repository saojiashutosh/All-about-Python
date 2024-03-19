#  Ask start and end index from the user. Create a list from start index to end index using slicing.

my_list = [23, 54, 78, 43, 12, 34, 89]

start = int(input("Enter start index = "))
end = int(input("Enter end index = "))

result = my_list[start : end + 1]

print(result)
