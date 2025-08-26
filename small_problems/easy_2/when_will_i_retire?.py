'''
P: prompt user for age and retirement age, output retirment year
    and years of work left
E: 30, 70 -> 2064, 40
D: none
A: datetime.date.year and arithmetic
C: below
'''

from datetime import date

age = int(input('What is your age? '))
retirement_age = int(input('At what age would you like to retire? '))

current_year = date.today().year

years_left = retirement_age - age

print(f"\nIt's {current_year}. You will retire in {current_year + years_left}.")
print(f'You have only {years_left} years of work to go!')