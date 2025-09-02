'''
P: return number times 2 unless double number in which case return input
E: 37 -> 74, 44 -> 44
D: none
A: is_double helper, branch
C: below
'''

def is_double(num):
    str_num = str(num)
    n = len(str_num)

    return str_num[:n//2] == str_num[n//2:]

def twice(num):
    return num if is_double(num) else num * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True