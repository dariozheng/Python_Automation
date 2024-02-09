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

def check(day, month, year, groups):
    month = int(month)
    day = int(day)
    year = int(year)
    if month in [4,6,9,11]: 
        if day <= 30:
            matches.append(groups[0])
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  
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
    check(day, month, year, groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else: 
    print('No Date is found')
