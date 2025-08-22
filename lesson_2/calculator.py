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
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt("For Spanish please enter 2.")
language_choice = input()

if language_choice == '2':
    LANGUAGE = 'ESP'
else:
    LANGUAGE = 'ENG'

prompt(MESSAGES[LANGUAGE]['welcome'])

while True:
    prompt(MESSAGES[LANGUAGE]['first'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES[LANGUAGE]['invalid_number'])
        number1 = input()

    prompt(MESSAGES[LANGUAGE]['second'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES[LANGUAGE]['invalid_number'])
        number2 = input()

    prompt(MESSAGES[LANGUAGE]['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(MESSAGES[LANGUAGE]['invalid_operation'])
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

    prompt(MESSAGES[LANGUAGE]['another?'])
    answer = input()

    if answer and answer[0].lower() != 'y':
        break
