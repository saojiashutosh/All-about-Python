# Take 10 integer inputs from user and store them in a list. Now, copy
# all the elements in another list but in reverse order.

num = int(input("Enter the size of list: "))
my_list = []
print("Enter your list elements: ")
for i in range(0, num):
    my_list.append(input())

print("Original list:", my_list)

another_list = []
for i in range(num - 1, -1, -1):
    another_list.append(my_list[i])

print("Reversed list:", another_list)
