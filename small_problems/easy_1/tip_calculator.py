'''
P: make text prompt tip calculator
E: 200, 20 -> 40, 240
D: two floats
A: none
C:
'''

bill_amount = float(input('What is the bill? '))
tip_percentage = float(input('What is the tip percentage? '))

tip = bill_amount * tip_percentage/100

print(f'\nThe tip is ${tip:.2f}')
print(f'The total is ${bill_amount + tip:.2f}')