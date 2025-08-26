'''
P: prompt for two floating points, print list of arithmetic operations
E: 3, 5 -> 3 + 5 = 8 ...
D: none
A: none
C: below
'''

def prompt(message):
    print(f'==> {message}')

prompt('Enter the first number:')
num1 = float(input().strip())

prompt('Enter the second number:')
num2 = float(input().strip())

prompt(f'{num1} + {num2} = {num1 + num2}')
prompt(f'{num1} - {num2} = {num1 - num2}')
prompt(f'{num1} * {num2} = {num1 * num2}')
prompt(f'{num1} / {num2} = {num1 / num2}')
prompt(f'{num1} // {num2} = {num1 // num2}')
prompt(f'{num1} % {num2} = {num1 % num2}')
prompt(f'{num1} ** {num2} = {num1 ** num2}')