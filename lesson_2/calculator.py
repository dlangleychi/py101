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

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def do_calculation():
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
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

    prompt("""Would you like to perform another calculation?
    yes or no""")
    answer = input()

    while answer not in ['yes', 'no']:
        prompt("Please answer yes or no.")
        answer = input()

    if answer == 'yes':
        do_calculation()

prompt('Welcome to Calculator!')

do_calculation()




