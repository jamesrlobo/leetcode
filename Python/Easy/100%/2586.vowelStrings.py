# 2586. Count the Number of Vowel Strings in Range
# Beats: 100.00%
def vowelStrings(words, left, right):
    v = ['a', 'e', 'i', 'o', 'u']
    output = 0
    for i in range(left,right+1):
        if words[i][0] in v and words[i][-1] in v:
            output +=1
    return output


words = ["are","amy","u"]
left = 0
right = 2

# words = ["hey","aeo","mu","ooo","artro"]
# left = 1
# right = 4
print(vowelStrings(words, left, right))
