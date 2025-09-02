'''
P: take an int year and return century as string with correct ending
E: 2000 -> '20th', 2001 -> '21st'
D: none
A: century = (year - 1) // 100 + 1 , seperate suffix function
C: below
'''

def century_number(year):
    return ((year - 1) // 100) + 1

def ordinal_suffix(num):
    if 11 <= (num % 100) <= 13:
        return 'th'
    if num % 10 == 1:
        return 'st'
    if num % 10 == 2:
        return 'nd'
    if num % 10 == 3:
        return 'rd'
    return 'th'

def century(int_year):
    int_century = century_number(int_year)
    return f'{int_century}{ordinal_suffix(int_century)}'

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True