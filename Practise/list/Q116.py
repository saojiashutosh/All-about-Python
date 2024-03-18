# Write a Python code to find the second largest element in a list without sorting.

list1 = [5, 6, 7, 66, 3, 6, 9, 4, 57, 32, 5, 32]

greater = list1[0]
greater2 = list1[0]
for i in range(0, len(list1)):
    if greater <= list1[i]:
        greater = list1[i]

for i in range(0, len(list1)):
    if greater2 <= list1[i] < greater:
        greater2 = list1[i]

print("Second largest element:", greater2)
