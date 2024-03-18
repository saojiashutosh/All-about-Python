# Generate a list of list using list comprehension where format should
# be [[1, ”ODD”], [2, “EVEN”], [3, ”ODD”]]

my_list = [[i, "EVEN"] if i % 2 == 0 else [i, "ODD"] for i in range(1, 6)]
print(my_list)
