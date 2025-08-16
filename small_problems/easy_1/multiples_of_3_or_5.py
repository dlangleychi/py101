'''
P: return sum of numbers between 1 and input inclusive 
    that are multiples of 3 or 5
E: 3 -> 3, 10 -> 33
D: none
A: loop, add if it meets criteria
C: below
'''

def multisum(num):
    result = 0
    for i in range(1, num+1):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)