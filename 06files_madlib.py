#! Python3
# A Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
from pathlib import Path
import re


fil = Path.cwd() / input('What file do you want to change the words? \n')
text = open(fil)
textContent = text.read()
text.close()
text = open(fil, 'w')
print('This is the text: \n')
print(textContent)
adjRe = re.compile(input('Enter an adjective: '))
nounRe = re.compile(input('Enter a noun: '))
verbRe = re.compile(input('Enter a verb: '))
noun2Re = re.compile(input('Enter a noun: '))

textContent = adjRe.sub('ADJECTIVE', textContent)
textContent = nounRe.sub('NOUN', textContent)
textContent = verbRe.sub('VERB', textContent)
textContent = noun2Re.sub('NOUN', textContent)

print(textContent)
text.write(textContent)
text.close()