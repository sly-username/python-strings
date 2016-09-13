s = 'azcbobobegghakl'
prevLetter = ''
currentString = s[0]
longestString = ''

for position, letter in enumerate(s):
    if prevLetter <= letter:
        currentString += letter
    else: 
        if len(currentString) > len(longestString):
            longestString = currentString
        currentString = letter
    prevLetter = letter

if len(currentString) > len(longestString):
    longestString = currentString

print('Longest substring in alphabetical order is:', longestString)
