
# 1

# {'prop1': 'hi there'}
# {'prop1': 'hi there'}

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

# print(first())
# print(second())

# WRONG second one returns None

# 2

# [1, 2]
# {'first': [1, 2]}

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

# print(num_list)
# print(dictionary)

# 3

'''
A)
one
two
three

B)
one
two
three

C)
two
three
one

'''

def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

# 4

def is_an_ip_number(word):
    return 0 <= int(word) <= 255

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    
    if len(dot_separated_words) != 4:
        return False
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

# print(is_dot_separated_ip_address('45.10.11.255') == True)
# print(is_dot_separated_ip_address('45.10.11.256') == False)
# print(is_dot_separated_ip_address('10.11.255') == False)
# print(is_dot_separated_ip_address('45.10.11.255.63') == False)

# 5

# NameError: name 'greeting' is not defined

if False:
    greeting = "hello world"

print(greeting)