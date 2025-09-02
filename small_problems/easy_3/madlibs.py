'''
P: create simple madlib program
E: dog, walk, blue, quickly ->
Do you walk your blue dog quickly? That's hilarious!
The blue dog walks quickly over the lazy dog.
The dog quickly walks up to Joe's blue turtle.
D: four variables:
A: none
C: below
'''

noun = input('Enter a noun: ').strip()
verb = input('Enter a verb: ').strip()
adjective = input('Enter an adjective: ').strip()
adverb = input('Enter an adverb: ').strip()

print(f'''
Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!
The {adjective} {noun} {verb}s {adverb} over the lazy {noun}.
The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.
''')