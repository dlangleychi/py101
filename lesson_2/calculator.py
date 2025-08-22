# X Ask the user for the first number.
# X Ask the user for the second number.
# X Ask the user for an operation to perform.
# X Perform the operation on the two numbers.
# X Print the result to the terminal.

'''
P: above
E: 1, 2, add -> 3
D: none
A: none
C: below
'''

import json

with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

while True:
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt(data['invalid_num'])
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt(data['invalid_num'])
        number2 = input()

    prompt("""What operation would you like to perform?
    1) Add 2) Subtract 3) Multiply 4) Divide""")
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt("You must choose 1, 2, 3, or 4.")
        operation = input()

    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)

    prompt(f'The result is: {output}')

    prompt("Would you like to perform another operation? (y/n) ")
    answer = input()

    if answer and answer[0].lower() != 'y':
        break



