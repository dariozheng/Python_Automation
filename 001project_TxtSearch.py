#! python3
# This is a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results is printed to the screen and saved in a txt.

from pathlib import Path
import re, os

#save the result in a txt file in the home dir
def saveOnFile():
    listOfLines = open(Path(homeDir/'listOfLines.txt'), 'a')
    listOfLines.write(f'File: {file.name}, Line: {lineNumber}, Match: {line.strip()} \n')
    listOfLines.close()
#print the folder in the home directory 
def homeDir():
    print('\nFolders: \n')
    for files in os.listdir(Path.home()):
        print('- '+files, end='\n')
    return Path.home()
#choose a folder among those in the homedir
def chooseFolder():
    folder = ''
    while folder == '':
        folder = input('What is the folder? \nPlease input a folder from the home directory:\n')
    return Path(homeDir/folder)

homeDir = homeDir()
path = chooseFolder()

lineRegex = re.compile(input('What line do you want to find?:\n'))
numberFiles = 0

for file in path.glob('*.txt'):
    with open(file) as f:
        for lineNumber, line in enumerate(f, 1):
            if lineRegex.search(line):
                print(f'File: {file.name}, Line: {lineNumber}, Match: {line.strip()}')
                saveOnFile()
        numberFiles += 1
    f.close()

print(f'\nWe have found {numberFiles} txt files. \n')
