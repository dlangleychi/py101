

'''
Code doesn't work because x, itself, is omitted.
Solve with:
    for y in range(1, x + 1)
'nums = ...' is superfluous, we could just iterate through the range.
The two conditionals could be just one with an or statement:
    if y % 3 == 0 or y % 5 == 0
'''


def multisum(x):
    result = 0
    nums = list(range(1, x))
    for y in nums:
        if y % 3 == 0:
            result += y
        elif y % 5 == 0:
            result += y
    return result


# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)