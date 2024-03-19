# Write a program to find the average of all the numbers present in the list.

num = int(input("Enter the size of list: "))
my_list = []
print("Enter your list elements: ")
for i in range(0, num):
    my_list.append(input())

sum = 0

for i in range(0, num):
    sum += int(my_list[i])

avg = sum / num
print("Average of all elements = ", avg)
