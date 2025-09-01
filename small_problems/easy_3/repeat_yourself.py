'''
P: function prints string integer number of times
E: 'a', 1 -> a
D: None
A: loop
C: below
'''

def repeat(string, number_times):
    for _ in range(number_times):
        print(string)

repeat('Hello', 3)