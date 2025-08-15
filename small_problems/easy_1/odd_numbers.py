'''
P: print all odd numbers 1 to 99, each on seperate line
E: 1 \n 2 \n ,,,
D: none
A: loop
C: 
'''

for i in range(1, 100, 2):
    print(i)

# bonus: check

# further exploration

def print_odds(start, end):
    if start % 2 == 0:
        start += 1
    for num in range(start, end + 1, 2):
        print(num)

print()
print_odds(44, 57)