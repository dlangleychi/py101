'''
P: using multipy function make function that returns square of argument
E: 2 -> 4, -3 -> 9
D: none
A: none
C: below
'''

def multiply(num1, num2):
    return num1 * num2

def square(num):
    return multiply(num, num)

def power_to_n(num, n):
    result = 1
    for _ in range(n):
        result = multiply(result, num)
    return result

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

print(power_to_n(2, 3) == 8)
print(power_to_n(-2, 3) == -8)