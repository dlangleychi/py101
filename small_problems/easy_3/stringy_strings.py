'''
P: return string of alternating 1's and 0's with length 
of integer input
E: 1 -> '1', 2 -> '10', 3 -> '101'
D: none
A: '10' * quotient n/2 + '1' if odd
C: below
'''

def stringy(pos_int):
    return '10' * (pos_int // 2) + '1' * (pos_int % 2)

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True