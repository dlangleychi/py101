'''
P: prompt user for length and width in meters, 
    print area in square meters and square feet
E: 1, 2 -> 2 and 2 * 10.7639 ** 2
D: two floats (and one conversion constant)
A: none
C:
'''

SQR_FEET_PER_SQR_METER = 10.7639

length = float(input('What is length in meters? '))
width = float(input('What is width in meters? '))

units = None

while units is None:
    units = input('What units of output? ')

    if units not in ['meters', 'feet']:
        print()
        print('Please select meters or feet.')
        units = None

area = length * width
if units == 'feet':
    area *= SQR_FEET_PER_SQR_METER

print(f'The room\'s area is {area:.2f} square {units}.')
