

'''
Looks like a good answer.  It is clear, easy to understand,
and stylistically good.
'''

def yes_no_response(question):
    while True:
        print(question)
        answer = input()

        if answer == 'y' or answer == 'yes':
            print('Here we go again!')
            return
        elif answer == 'n' or answer == 'no':
            print('Okay. See you later.')
            return
        else:
            print('You goofed! That is not a valid answer.')

yes_no_response("Do you want to continue? (y/n)")
yes_no_response("Are you absolutely sure? (yes/no)")
print("All done.")