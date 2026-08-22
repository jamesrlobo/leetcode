# 3136. Valid Word
def isValid(word):
    vowel, consonant = 0, 0
    if len(word) < 3:
        return False
    for i in range(len(word)):
        if word[i].isalnum():
            if word[i].isalpha() and word[i].upper() not in ['A','E','I','O','U']:
                consonant += 1
            elif word[i].isalpha() and word[i].upper() in ['A','E','I','O','U']:
                vowel += 1
            continue
        else:
            return False
    if (vowel == 0) or (consonant == 0):
        return False
    return True


# word = "234Adas"
# word = "b3"
word = "a3e"
print(isValid(word))
