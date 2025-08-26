'''
P: print random age between 20 and 100
E: Teddy is 45 years old!
D: none
A: random.randint()
C: below
'''

import random

LOWER_LIMIT = 20
UPPER_LIMIT = 100

name_input = input('Please provide a name: ')

name = name_input.strip().title() if name_input.strip() else 'Teddy'

print(f'{name} is {random.randint(LOWER_LIMIT, UPPER_LIMIT)} years old!')