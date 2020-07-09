# Get word from user
# Break down word
    # If Check for the first 2 letters or vowel
    # else add first letter + "ay"
# Print out word


def checkVowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    firstLetter = word[0].lower()
    for i in range(len(vowels)):
        if(firstLetter == vowels[i]):
            return True                 # if the first letter contains a vowel return true
    # else return false
    return False

def checkPre(word):
    prefix = ["bl", "br", "ch", "cl", "cr", "dr", "fl", "fr", "gl", "gr", "kl", "ph", "pl", "pr", "sh", "sl", "sp", "sr", "st", "th", "tr", "wh", "wr"]
    pre = (word[0] + word[1]).lower()
    for i in range(len(prefix)):
        if(pre == prefix[i]):
            return True                 # if the first letter contains a prefix return true
    # else return false
    return False

def breakWordPrefix(word):
    pre = word[0] + word[1]
    word = word.strip(pre)
    word = word + pre + "ay"
    return word

def breakWordVowels(word):
    word = word + "yay"
    return word

def breakWordNormal(word):
    s = list(word)
    firstLetter = s[0]
    s[0] = ''
    word = ''.join(s)
    word = word + firstLetter + 'ay'
    return word

def breakWord(word):
    if checkPre(word) == True:              #if check prefix
        word = breakWordPrefix(word)
    elif checkVowels(word) == True:           #elif check vowels
        word = breakWordVowels(word)
    else:
        word = breakWordNormal(word)
    return word

def pigLatin(englishWord):
    word = breakWord(englishWord)
    print(word)
    return word
