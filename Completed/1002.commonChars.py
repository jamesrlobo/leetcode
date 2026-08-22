# 1002. Find Common Characters
def commonChars(words):
    output = []
    d = {}
    for i in words[0]:
        d[i] = words[0].count(i)
    print(d)
    for word in words[1:]:
        for ch in d:
            print(word, ch, word.count(ch))
            if ch in word:
                if word.count(ch) < d[ch]:
                    d[ch] = word.count(ch)
            elif ch not in word:
                d[ch] = 0
            print(d)
    for item in d:
        if d[item] > 0:
            for i in range(d[item]):
                output.append(item)
    return output

words = ["bcaddcdd","cbcdccdd","ddccbdda","dacbbdad","dababdcb","bccbdaad","dbccbabd","accdddda"]
# words = ["dadaabaa","bdaaabcc","abccddbb","bbaacdba","ababbbab","ccddbbba","bbdabbda","bdabaacb"]
# words = ["cool","lock","cook"]
# words = ["bella","label","roller"]
# words = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
print(commonChars(words))
