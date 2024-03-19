# Write a Python code to find the occurrence of each element in a list and print the element with the highest occurrence.

my_list = [5, 1, 10, 20, 5, 1, 1]

result = []

for num in my_list:
    if num not in result:
        result.append(num)

highest_occ_element = 0
highest_occurance = 0

for num in result:
    count = my_list.count(num)
    print(f"{num} occurs {count} times")
    if count > highest_occurance:
        highest_occurance = count
        highest_occ_element = num

print(f"Highest occurance element {highest_occ_element}")
print(f"highest occurance is {highest_occurance}")
