'''
P: given positive int draw right triangle with n lenght adj sides
E: 5 ->
    *
   **
  ***
 ****
*****
D: none
A: loop
C: below
'''

def triangle(n):
    for i in range(1, n + 1):
        print(('*' * i).rjust(n))

triangle(5)

print()

triangle(9)