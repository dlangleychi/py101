'''
P: write function that return next to last word in string
E: 'hit a ball' -> 'a'
D: none
A: none
C: below
'''

def penultimate(sentence_string):
    return sentence_string.split()[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

def middle_word(sentence_string):
    word_list = sentence_string.split()

    word_count = len(word_list)
    if word_count == 0:
        return ''
    
    middle_index = (word_count - 1) // 2
    
    return word_list[middle_index]

print(middle_word('') == '')
print(middle_word('a') == 'a')
print(middle_word('a big dog') == 'big')
print(middle_word('a big red dog') == 'big')
