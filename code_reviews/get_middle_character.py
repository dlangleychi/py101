
'''
Problem with even lenght case: logic is correct, but string indices 
must be ints, and assignment is superfluous
corrected version:
    return string[l//2 - 1] + string[l//2]
Also, condition for even length is bad stylistically, needs spaces, 
and don't need assignment, should read:
    if len(string) % 2 == 0:
'''

def center_of(string):
  l = len(string)
  if l%2==0:
      middle_chars = string[(l/2) - 1] + string[l/2]
      return middle_chars
  else:
    return string[l//2]

# These examples should all print True
print(center_of('I love Python!!!') == "Py")
print(center_of('Launch School') == " ")
print(center_of('Launchschool') == "hs")
print(center_of('Launch') == "un")
print(center_of('Launch School is #1') == "h")
print(center_of('x') == "x")