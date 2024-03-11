my_list = [51, 85, 1748, 52, 44, 100, 200]

x = len(my_list)
large = my_list[0]
for i in range(0, x):
    if large < my_list[i]:
        large = my_list[i]

print(large)
