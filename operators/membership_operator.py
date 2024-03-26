# there are two operator in this
# 1. in : checks that element is in the sequence (eg,list,tuple ,etc)
# 2. not in : check that element is not in that sequence


a = [59, 68, 100, 5, "Ashutosh", True, 55.556, "Code"]

num = int(input("Enter a number = "))

if num in a:
    print("yes")
else:
    print("no")


if num not in a:
    print("yes")
else:
    print("no")
