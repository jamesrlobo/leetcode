# 3042. Count Prefix and Suffix Pairs I
# Beats: 28.99%
def countPrefixSuffixPairs(words):
    count = 0
    for i in range(len(words)):
        for j in range(len(words)):
            if i < j and len(words[i]) <= len(words[j]):
                if (words[i] == words[j][:len(words[i])]) and (words[i] == words[j][-len(words[i]):]):
                    print(words[i], words[j])
                    count += 1
    return count



# words = ["a","aba","ababa","aa"]
# words = ["pa","papa","ma","mama"]
# words = ["abab","ab"]
words = ["bb","bb"]
print(countPrefixSuffixPairs(words))
