'''
P: make rock paper scissors game
E: rock, paper -> loss
D: variables
A: while True play the game
C: below
'''

import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

WINNING_COMBINATIONS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'spock': ['rock', 'scissors'],
    'lizard': ['paper', 'spock'],
}

STARTING_SCORE = 0
WINNING_SCORE = 3

def prompt(message):
    print(f'==> {message}')

def interpret_choice(choice_input):
    for valid_choice in VALID_CHOICES:
        if choice_input and choice_input.lower() in valid_choice:
            return valid_choice
    return None

def return_winner(player, computer):
    if computer in WINNING_COMBINATIONS[player]:
        return 'player'
    if player != computer:
        return 'computer'
    return None

def display_winner(player, computer):
    round_winner = return_winner(player, computer)

    if round_winner == 'player':
        prompt('You win!')
    elif round_winner == 'computer':
        prompt('Computer wins!')
    else:
        prompt('It\'s a tie!')

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