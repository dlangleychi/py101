# 1

numbers = [1, 2, 3, 4]

while numbers:
    numbers.pop()

# print(numbers)

numbers = [1, 2, 3, 4]

numbers.clear()

# print(numbers)

numbers = [1, 2, 3, 4]

numbers[:] = []

# print(numbers)

# 2 [1, 2, 3, 4, 5]

# print([1, 2, 3] + [4, 5])

# 3 hello there

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
# print(str1)

# 4 [{"first": 42}, {"second": "value2"}, 3, 4, 5]

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
# print(my_list1)

# 5 

def is_color_valid(color):
    return color == 'blue' or color == 'green'

def is_color_valid(color):
    return color in ['blue', 'green']

print(is_color_valid('blue'))
print(is_color_valid('green'))
print(is_color_valid('red'))
