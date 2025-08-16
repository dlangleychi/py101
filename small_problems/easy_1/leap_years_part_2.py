'''
P: write a function that determines is a year is a leap year
    use Julian calendar before 1752, and Gregorian calendar afterwards
E: 1300 -> True, 1900 -> False
D: none
A: branching on year < 1752
C: below
'''

SWICH_YEAR = 1752

def is_leap_year(year):
    if year < SWICH_YEAR:
        return year % 4 == 0
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)