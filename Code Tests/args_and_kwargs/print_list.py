# TUTORIAL DE : https://realpython.com/python-kwargs-and-args/

# LIST
my_list = [1, 2, 3]
print(my_list)

# UNPACKED LIST
my_list = [1, 2, 3]
print(*my_list)

# UNPACKED CALL
def my_sum(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3]
my_sum(*my_list)

# WRONG UNPACKED CALL
def my_sum(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3, 4]
my_sum(*my_list)
