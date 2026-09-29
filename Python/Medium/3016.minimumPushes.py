# 3016. Minimum Number of Pushes to Type Word II
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/
# Beats: 97.66%
def minimumPushes(word):
    unique_characters = len(set(word))
    if unique_characters <= 8:
        return len(word)
    print("Unique Characters:", unique_characters)
    d = {}
    for i in set(word):
        if i not in d:
            d[i] = word.count(i)
    print(d)
    keys = sorted(d, key=d.get, reverse=True)
    print(keys)
    # vals = (sorted(d.values(), reverse=True))
    # print(vals)
    turn = 1
    count = 0
    while len(keys) > 0:
        if len(keys) <= 8:
            print("here:", keys)
            for x in keys:
                print(x, d[x]*turn, turn)
                count += (d[x] * turn)
            break
        else:
            for x in keys[:8]:
                print(x, d[x]*turn, turn)
                count += (d[x] * turn)
            keys = keys[8:]
        turn += 1
    return count


word = "abcde"
word = "aabbccddeeffgghhiiiiii"
word = "abzaqsqcyrbzsrvamylmyxdjl"
print(minimumPushes(word))
