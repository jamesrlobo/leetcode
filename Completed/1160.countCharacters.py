# 1160. Find Words That Can Be Formed by Characters
# Beats: 98.95%
def countCharacters(words, chars):
    output = 0
    d = {}
    for i in set(chars):
        d[i] = chars.count(i)
    for word in words:
        for ch in word:
            if ch not in d:
                break
            if word.count(ch) > d[ch]:
                break
        else:
            output += int(len(word))
    return output


# words = ["cat","bt","hat","tree"]
# chars = "atach"
words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(countCharacters(words, chars))
