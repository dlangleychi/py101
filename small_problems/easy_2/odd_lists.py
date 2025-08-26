'''
P: function takes list and returns even indexed elements in list
E: [0, 1, 2] -> [0, 2]
D: none
A: list slicing
C: below
'''

def oddities(ls):
    return ls[::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

def evens(ls):
    return ls[1::2]

print(evens([2, 3, 4, 5, 6]) == [3, 5])  # True
print(evens([1, 2, 3, 4]) == [2, 4])        # True
print(evens(["abc", "def"]) == ['def'])     # True
print(evens([123]) == [])                # True
print(evens([]) == [])                      # True
