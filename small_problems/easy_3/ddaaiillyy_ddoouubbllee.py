'''
P: function collapses string removing consecutive duplicate characters
E: 'aaabbb' -> 'ab', '' -> ''
D: none
A: loop through characters only recording if its not a duplicate
C: below
'''

def crunch(string):
    result = ''
    for i, char in enumerate(string):
        if i == 0 or string[i] != string[i - 1]:
            result += char
    return result

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')