'''
P: function takes text and prints it in box
E: 'hello' ->

+-------+
|       |
| hello |
|       |
+-------+

D: none
A: none
C: below
'''

def print_in_box(text, box_width):
    if len(text) > box_width - 4:
        text = text[:box_width - 4]

    text_len = len(text)

    print(f'+{'-' * (text_len + 2)}+')
    print(f'| {' ' * text_len} |')
    print(f'| {text} |')
    print(f'| {' ' * text_len} |')
    print(f'+{'-' * (text_len + 2)}+')

print_in_box('To boldly go where no one has gone before.', 30)

def wrap_in_box(text, box_width):
    word_list = text.split()

    max_text_per_line = box_width - 4

    border = f'+{'-' * (box_width - 2)}+'
    empty_line = f'|{' ' * (box_width - 2)}|'

    print(border)
    print(empty_line)
    
    line_text = ''

    for word in word_list:
        if len(word) > max_text_per_line:
            return
        
        if len(word) + 1 + len(line_text) > max_text_per_line:
            print(f'| {line_text.center(max_text_per_line)} |')

            line_text = word

        elif line_text:
            line_text += ' ' + word

        else:
            line_text = word

    print(f'| {line_text.center(max_text_per_line)} |')

    print(empty_line)
    print(border)

print()
wrap_in_box('To boldly go where no one has gone before.', 30)
