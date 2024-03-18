# Write a program that has two lists and make a new list that contains only the common elements between them without duplicates.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

list3 = []

for i in range(0, len(list1)):
    for j in range(0, len(list2)):
        if list2[j] == list1[i]:
            list3.append(list2[j])

print(list3)
