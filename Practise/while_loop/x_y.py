# Ask to numbers x and y from the user. If x<y then print all the
# numbers from x to y, but if y<x then print all the numbers from y to x

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if x < y:
    while x <= y:
        print(x)
        x += 1
elif y < x:
    while y <= x:
        print(y)
        y += 1
else:
    print("x and y are equal:", x)
