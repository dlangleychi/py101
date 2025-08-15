'''
P: text prompt for integer, text prompt for sum or product,
    print sum or product between 1 and integer
E:
 5, s -> 15
D: two variables
A: none
C:
'''

import math

number = int(input('Please enter an integer greater than 0: '))
op = input('Enter "s" to compute the sum, or "p" to compute the product. ')

print()

if op == 's':
    sum = int( number * (number + 1) / 2)
    print(f'The sum of the integers between 1 and {number} is {sum}.')

elif op == 'p':
    product = math.factorial(number)
    print(f'The product of the integers between 1 and {number} is {product}.')

else:
    print('Invalid operation.')