# Write a Python function that takes start_number and end_number as a parameter. Now print all the prime numbers between start_number to end_number.
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


start = int(input("Enter a Start Number = "))
end = int(input("Enter a End Number = "))
prime_no = []
for i in range(start, end + 1):
    is_prime(i)
    if is_prime(i):
        prime_no.append(i)

print(prime_no)
