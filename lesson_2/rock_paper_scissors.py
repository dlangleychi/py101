'''
P: make rock paper scissors game
E: rock, paper -> loss
D: variables
A: while True play the game
C: below
'''

import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

WINNING_SCORE = 3
STARTING_SCORE = 0

def prompt(message):
    print(f'==> {message}')

def interpret_choice(choice_input):
    for valid_choice in VALID_CHOICES:
        if choice_input in valid_choice:
            return valid_choice
    return None

def display_winner(player, computer):
    if ((player == 'rock' and computer in ['scissors', 'lizard']) or
        (player == 'paper' and computer in ['rock', 'spock']) or
        (player == 'scissors' and computer in ['paper', 'lizard']) or
        (player == 'spock' and computer in ['rock', 'scissors']) or
        (player == 'lizard' and computer in ['paper', 'spock'])):
        prompt('You win!')
    elif ((player == 'rock' and computer in ['paper', 'spock']) or
        (player == 'paper' and computer in ['scissors', 'lizard']) or
        (player == 'scissors' and computer in ['rock', 'spock']) or
        (player == 'spock' and computer in ['paper', 'lizard']) or
        (player == 'lizard' and computer in ['rock', 'scissors'])):
        prompt('Computer wins!')
    else:
        prompt('It\'s a tie!')

def return_winner(player, computer):
    if ((player == 'rock' and computer in ['scissors', 'lizard']) or
        (player == 'paper' and computer in ['rock', 'spock']) or
        (player == 'scissors' and computer in ['paper', 'lizard']) or
        (player == 'spock' and computer in ['rock', 'scissors']) or
        (player == 'lizard' and computer in ['paper', 'spock'])):
        return 'player'
    if ((player == 'rock' and computer in ['paper', 'spock']) or
        (player == 'paper' and computer in ['scissors', 'lizard']) or
        (player == 'scissors' and computer in ['rock', 'spock']) or
        (player == 'spock' and computer in ['paper', 'lizard']) or
        (player == 'lizard' and computer in ['rock', 'scissors'])):
        return 'computer'
    return None

while True:
    player_score = STARTING_SCORE
    computer_score = STARTING_SCORE

    while True:
        prompt(f'Score is player: {player_score}, computer: {computer_score}')

        if player_score == WINNING_SCORE:
            prompt("Player wins the game!")
            break
        if computer_score == WINNING_SCORE:
            prompt("Computer wins the game!")
            break

        prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
        choice = interpret_choice(input())

        while choice not in VALID_CHOICES:
            prompt("That's not a valid choice")
            choice = interpret_choice(input())

        computer_choice = random.choice(VALID_CHOICES)

        prompt(f'You chose {choice}, computer chose {computer_choice}')

        winner = return_winner(choice, computer_choice)

        if winner == 'player':
            player_score += 1
        elif winner == 'computer':
            computer_score += 1

        display_winner(choice, computer_choice)

    prompt('Do you want to play again (y/n)?')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        break
