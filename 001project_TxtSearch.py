#! python3
# This is a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results is printed to the screen.

from pathlib import Path
import re, os

homeDir = Path.home()
print('\nFolders: \n')
for files in os.listdir(homeDir):
    print('- '+files, end='\n')

folder = input('What is the folder? \nPlease input a folder from the home directory:\n')
path = Path(homeDir/folder)

lineRegex = re.compile(input('What line do you want to find?:\n'))
numberFiles = 0

for file in path.glob('*.txt'):
    with open(file) as f:
        for lineNumber, line in enumerate(f, 1):
            if lineRegex.search(line):
                print(f'File: {file.name}, Line: {lineNumber}, Match: {line.strip()}')
        numberFiles += 1

print(f'\nWe have found {numberFiles} txt files. \n')
