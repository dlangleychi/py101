

'''
Code works, but could be more simple and more clear.
Change 'line' variable to 'number_stars'
New code would be
for number_stars in range(1, height + 1):
    print(' ' * (height - number_stars) + '*' * number_stars)
'''

def triangle(height):
    line = 1
    while line <= height:
        spaces = ''
        for _ in range(height - line):
            spaces += ' '

        stars = ''
        for _ in range(line):
            stars += '*'

        print(spaces + stars)
        line += 1

triangle(5)
triangle(9)