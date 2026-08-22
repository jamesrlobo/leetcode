# 520. Detect Capital
# https://leetcode.com/problems/detect-capital/description/
# Beats: 100.00%
def detectCapitalUse(word):
    camelcase = True
    all_caps = True
    n = len(word)
    capitals = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    smallcase =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if word[0] in smallcase:
        for i in range(1, n):
            if word[i] not in smallcase:
                return False
    else:
        for i in range(1, n):
            if word[i] not in capitals:
                all_caps = False
            if word[i] not in smallcase:
                camelcase = False
    if camelcase == True or all_caps == True:
        return True
    return False


word = "USA"
word = "FlaG"
print(detectCapitalUse(word))
