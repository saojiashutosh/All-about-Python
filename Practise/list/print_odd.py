my_list = [51, 74, 85, 52, 91, 44]
x = len(my_list)
for i in range(0, x):
    if my_list[i] % 2 != 0:
        print(my_list[i], end=" ")
