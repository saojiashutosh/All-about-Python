# # Make a list of your own. And remove all the duplicates element from
# # that list.

my_list = [5, 1, "code", 5, 10, 20, 5, 1, 1]
result = []

for num in my_list:
    if num not in result:
        result.append(num)

print(result)
