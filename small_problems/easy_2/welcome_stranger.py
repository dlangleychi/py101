'''
P: take name list and dictionary with title and occupation,
    return greeting that uses full name and tile
E: ['A', 'Man'], {'title': Good, 'occupation': Boy} ->
    Hello, A Man! Nice to have a Good Boy around.
D: none
A: none
C: below
'''

def greetings(name_list, title_dict):
    return (
        f'Hello, {' '.join(name_list)}! Nice to have '
        f'a {title_dict['title']} {title_dict['occupation']} around.'
    )

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.