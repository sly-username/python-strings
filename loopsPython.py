s = 'azcbobobegghakl'
stringsList = []
letters = ''

for i in range(len(s)-1):
    if s[i+1] >= s[i]:
        letters = letters + s[i]
        stringsList.append(letters)

    elif s[i+1] < s[i] and s[i] > s[i-1]:
        letters = letters + s[i]
        stringsList.append(letters)

    else:
        letters = ''

print(stringsList)