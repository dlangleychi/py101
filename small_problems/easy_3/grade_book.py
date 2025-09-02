'''
P: average three scores and return letter grade
E: 95, 90, 93 -> 'A'
D: none
A: average then if else
C: below
'''

def get_grade(score1, score2, score3):
    average_score = (score1 + score2 + score3) / 3

    if average_score >= 90:
        return 'A'
    if average_score >= 80:
        return 'B'
    if average_score >= 70:
        return 'C'
    if average_score >= 60:
        return 'D'
    return 'F'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True