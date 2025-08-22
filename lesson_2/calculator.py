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

LANGUAGE = 'en'

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message, lang='en'):
    return MESSAGES[lang][message]

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt(messages('welcome', LANGUAGE))

while True:
    prompt(messages('first', LANGUAGE))
    number1 = input()

    while invalid_number(number1):
        prompt(messages('invalid_number', LANGUAGE))
        number1 = input()

    prompt(messages('second', LANGUAGE))
    number2 = input()

    while invalid_number(number2):
        prompt(messages('invalid_number', LANGUAGE))
        number2 = input()

    prompt(messages('operation', LANGUAGE))
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(messages('invalid_operation', LANGUAGE))
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    prompt(f'The result is: {output}')

    prompt(messages('another?', LANGUAGE))
    answer = input()

    if answer and answer[0].lower() != 'y':
        break
