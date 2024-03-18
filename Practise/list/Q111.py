#  Make a list. Then ask a number from user. If number exists in that list
# then print the position of the element else print -1.

my_list = [5, 1, 5, 10, 20, 5, 1, 1]

num = int(input("Enter value = "))

if num in my_list:
    for i in range(0, len(my_list)):
        if num == my_list[i]:
            print("OUTPUT = ", i)
else:
    print("OUTPUT = -1")
