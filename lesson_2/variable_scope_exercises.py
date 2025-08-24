# # 1 -> 5

# num = 5

# def my_func():
#     print(num)

# my_func()

# # 2 -> 5

# num = 5

# def my_func():
#     num = 10

# my_func()
# print(num)

# # 3 -> 10

# num = 5

# def my_func():
#     global num
#     num = 10

# my_func()
# print(num)

# # 4 -> Hello World

# def outer():
#     outer_var = 'Hello'

#     def inner():
#         inner_var = 'World'
#         print(outer_var, inner_var)

#     inner()

# outer()

# 5 -> NameError

# def my_func():
#     num = 10

# my_func()
# print(num)

# 6 -> Inner 1: 25 (newline) Inner 2: 15

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()