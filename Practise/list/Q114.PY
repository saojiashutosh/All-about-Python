# Write a Python code to find the occurrence of each element in a list and print the element with the highest occurrence.

my_list = [5, 1, 5, 10, 20, 5, 1, 1]


element_count = {}


for element in my_list:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

max_occurrence_element = None
max_occurrence = 0

for element, count in element_count.items():
    if count > max_occurrence:
        max_occurrence = count
        max_occurrence_element = element

print("Occurrences of each element:", element_count)
print("Element with the highest occurrence:", max_occurrence_element)
print("Highest occurrence count:", max_occurrence)
