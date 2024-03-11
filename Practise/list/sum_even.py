my_list = [51, 85, 1748, 52, 44, 100, 200]


x = len(my_list)

sum = 0
for i in range(0, x):
    if my_list[i] % 2 == 0:
        sum += my_list[i]

print(sum)
