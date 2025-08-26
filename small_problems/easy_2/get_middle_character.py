'''
P: take string, return middle character if odd or two if even lenght
E: 'cat' -> 'a', 'boys' -> 'oy'
D: none
A: branch on length
C: below
'''

def center_of(str_):
    len_ = len(str_)

    if len_ % 2:
        return str_[len_ // 2]
    start_index = (len_ // 2) - 1
    return str_[start_index: start_index + 2]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True