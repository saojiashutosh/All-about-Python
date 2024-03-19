# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def distinct(my_list):
    unique_list = []
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)


my_list = [10, 20, 20, 20, 10, 10, 50]
distinct(my_list)
