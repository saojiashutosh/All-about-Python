#  Generate a list of at least 10 numbers. Then, create two separate
# lists called 'odd' and 'even.' Put all the odd numbers from the original list
# into the 'odd' list, and all the even numbers into the 'even' list.

my_list = [3, 8, 12, 17, 22, 30, 35, 41, 48, 50]

odd = []
even = []

for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        even.append(my_list[i])
    else:
        odd.append(my_list[i])

print("odd =", odd)
print("even =", even)
