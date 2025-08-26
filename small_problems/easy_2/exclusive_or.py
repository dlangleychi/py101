'''
P: write exclusive or function taking bool and other data types
E: 1,0 -> True, 1,1 -> False
D: none
A: none
C: below
'''

def xor(arg1, arg2):
    return bool(arg1) ^ bool(arg2)

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)