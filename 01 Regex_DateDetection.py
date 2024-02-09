#! python3
# Regex_DateDetection.py - Detects dates in the DD/MM/YYYY format on the clipboard.
import pyperclip, re

text = pyperclip.paste()

dateRegex = re.compile(r'''(
    (\d{2})
    \/
    (\d{2})
    \/
    (\d{4})
    )''', re.VERBOSE)

def check(day, month, year):
    month = int(month)
    day = int(day)
    year = int(year)
    if month in [4,7,9,11]: 
        if day <= 30:
            matches.append(groups[0])
    elif month == 2:
        if year % 4 == 0 | year % 100 == 0 and not year % 400 == 0: # Find the leap year 
            if day <= 29:
                matches.append(groups[0])
        else:
            if day <= 28:
                matches.append(groups[0])
    else:
        if day <= 31:
            matches.append(groups[0])

matches = []

for groups in dateRegex.findall(text):
    month, day, year = groups[2], groups[1], groups[3]
    check(day, month, year)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else: 
    print('No Date is found')
