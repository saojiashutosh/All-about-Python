my_list = [51, 85, 91.66, 52, 44, 100, 200]

x = len(my_list)

count = 0
for i in range(0, x):
    if my_list[i] % 2 == 0 and my_list[i] % 5 == 0:
        count += 1

print(count)
