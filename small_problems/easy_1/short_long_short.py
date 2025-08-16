'''
P: write function, compares length of strings, return short + long + short
E: 'a', 'bc' -> 'abca'
D: none
A: none
C: below
'''

def short_long_short(string1, string2):
    if len(string1) > len(string2):
        string1, string2 = string2, string1
    return string1 + string2 + string1

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")