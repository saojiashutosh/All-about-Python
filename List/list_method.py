a = [54, 23, 10, 90, -90]
b = [1, 2, 3, 4, 5]

print(a)

# insert element at the end
a.append(100)
a.append("Python")

print(a)

# insert element at the given index
a.insert(3, 999999)
a.insert(0, "hello")

print(a)

# delete element by index
a.pop(0)
a.pop(4)

print(a)

# delete element by value

a.remove(999999)
a.remove("Python")

print(a)

# remove all elements in list
a.clear()
print(a)
