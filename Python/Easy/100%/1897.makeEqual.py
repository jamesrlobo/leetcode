# 1897. Redistribute Characters to Make All Strings Equal
# Beats: 100.00%
def makeEqual(words):
    final = ""
    for word in words:
        final += word
    for i in set(final):
        if final.count(i)%len(words) != 0:
            return False
    return True


words = ["abc","aabc","bc"]
words = ["ab","a"]
print(makeEqual(words))
