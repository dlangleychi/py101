'''
P: make mortgage loan calculator that takes:
loan amount (dollars), annual percentage rate (%/year),
loan duration (years)
and print monthly payment (dollars)
E:  100,000, 6, 10 -> $1,110.21
D: variables
A: formula, m = p * (j / (1 - (1 + j) ** (-n)))
C: below
'''

import json

def invalid_float(float_str):
    try:
        float(float_str)
    except ValueError:
        return True
    return float(float_str) <= 0

def get_input_variable(message):
    print(message)
    variable_value_str = input()

    while invalid_float(variable_value_str):
        print(MESSAGES['invalid_input'])
        variable_value_str = input()

    return float(variable_value_str.strip())

with open ('mortgage_loan_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

loan_amount = get_input_variable(MESSAGES['loan_amount'])
apr = get_input_variable(MESSAGES['apr'])
loan_duration = get_input_variable(MESSAGES['loan_duration'])

monthly_interest = 0.01 * apr/12
month_duration = round(loan_duration * 12)

monthly_payment = loan_amount * \
    (monthly_interest / (1 - (1 + monthly_interest) ** (-month_duration)))

print(MESSAGES['result'].format(payment = monthly_payment))