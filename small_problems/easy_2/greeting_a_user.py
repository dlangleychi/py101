'''
P: prompt name, reply, with uppercase if name ends in '!'
E: Bob! -> HELLO BOB! ...
D: none
A: branch
C: below
'''

name_input = input('What is your name? ')

name = name_input.strip()

if name_input and name_input[-1] == '!':
    print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {name}.')
