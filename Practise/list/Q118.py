# Write a program to find and print all prime numbers within a given list.

num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Prime numbers within the list:")
for num in num_list:
    if num > 1:
        prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)
