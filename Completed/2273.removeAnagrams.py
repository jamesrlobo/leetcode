# 2273. Find Resultant Array After Removing Anagrams
# Beats: 33.02%
def removeAnagrams(words):
    def check(a, b):
        if set(a) == set(b):
            for x in a:
                if a.count(x) != b.count(x):
                    return False
        else:
            return False
        return True
    i = 1
    while i < len(words):
        print(words[i-1], words[i])
        if check(words[i-1], words[i]) == True:
            words.pop(i)
        else:
            i+=1
        # print(words)
    return words


words = ["abba","baba","bbaa","cd","cd"]
words = ["a","b","c","d","e"]
print(removeAnagrams(words))
