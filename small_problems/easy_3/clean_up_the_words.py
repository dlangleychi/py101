'''
P: replace nonalphbetic characters with single space
E: "---what's my +*& line?" -> " what s my line "
D: none
A: python regex subs one or more non alphbetic -> one space
C: below
'''

import re

def clean_up(string):
    return re.sub(r'([^a-zA-Z])+', r' ', string)

def clean_up(string):
    result_list = []
    for char in string:
        if char.isalpha():
            result_list.append(char)
        elif not result_list or result_list[-1] != ' ':
            result_list.append(' ')
    return ''.join(result_list)

print(clean_up("---what's my +*& line?") == " what s my line ")
# True