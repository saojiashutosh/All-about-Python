# Write a Python function to reverse a string using slicing and return it.
def reverse(a):
    x = len(a)
    result = a[x::-1]
    print(result)


a = "HelloWorld"
reverse(a)
