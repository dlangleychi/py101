
# 1

# str_ = 'The Flintstones Rock!'

# for padding in range(1,11):
#     print(f'{'-' * padding}{str_}')


# 2

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

# print(factors(12))
# print(factors(-12))

# bonus: to see if divisor evenly divides number 
# = if divisor is a factor of number

# 3

# in the first implementation new_element is appended to buffer
# buffer is mutated
# in teh second implementation a new buffer list is created each time
# an element is added

# 4

# 0.9 , True WRONG

# print(0.3 + 0.6)
# print(0.3 + 0.6 == 0.9)

import math

# print(0.3 + 0.6)
# print(math.isclose(0.3 + 0.6, 0.9))

# 5

# Value Error, WRONG, False

nan_value = float("nan")

# print(nan_value == float("nan"))

# print(math.isnan(nan_value))

# 6

# output: 34

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

# print(answer - 8)

# 7

# yes , dictionaries are mutable, when passes a reference is passed not
# a value

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)

# print(munsters)

# 8

def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"
    
# print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# prints rock WRONG paper

# 9

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

# print(bar(foo()))

# returns False

# 10

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# True