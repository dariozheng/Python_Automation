#! python3
# Regex_Strip.py is like the strip() function, with the added benefit of being able to replace the stripped word

import pyperclip, re

def RegexStrip(text, whatstrip):
    substitute = input('What word do you want to put at the place of the stripped word? ')
    stripRegex = re.compile(whatstrip, re.IGNORECASE)
    return stripRegex.sub(substitute, text)

text = pyperclip.paste()
whatstrip = input('Enter the Regex pattern to strip: ')
strippedtext = RegexStrip(text, whatstrip)
pyperclip.copy(strippedtext)