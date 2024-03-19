# Write a Python function that accepts a string and counts the number of upper and lower case letters.
def case(a):
    upper = [chr(i) for i in range(65, 91)]
    upper_count = 0
    lower_count = 0
    for i in a:
        if i in upper:
            upper_count += 1
        else:
            lower_count += 1
    print(f"Upper Count : {upper_count} , Lower Count : {lower_count}")


a = str(input("Enter a String = "))
case(a)
