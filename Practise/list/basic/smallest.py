my_list = [51, 85, 1748, 52, 44, 100, 200]

x = len(my_list)
small = my_list[0]
for i in range(0, x):
    if small > my_list[i]:
        small = my_list[i]

print(small)
