# 1

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

# print(numbers[::-1])
# print(list(reversed(numbers)))
# print(numbers)

# 2

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

# print(number1 in numbers)
# print(number2 in numbers)

# 3

# print(10 <= 42 <= 100)
# print(10 <= 100 <= 100)
# print(10 <= 101 <= 100)

# print(42 in range(10, 101))
# print(100 in range(10, 101))
# print(101 in range(10, 101))

# 4

numbers = [1, 2, 3, 4, 5]

# del numbers[2]
# print(numbers)

# 5

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

# print(isinstance(numbers, list))
# print(isinstance(table, list))

# 6

title = "Flintstone Family Members"

# print(title.center(40))

# 7

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

# print(statement1.count('t'))
# print(statement2.count('t'))

# 8

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

# print('Spot' in ages)

# 9

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update(additional_ages)

print(ages)