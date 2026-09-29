# 2423. Remove Letter To Equalize Frequency (Followed from Solutions)
# Beats: 100.00%
from collections import Counter
def equalFrequency(word):
    cntr = Counter(word)
    v = list(cntr.values())
    mx = v.index(max(v))
    mn = v.index(min(v))
    v1, v2 = [], []
    v1.extend(v)
    v2.extend(v)
    v1[mx] -= 1
    if v1[mx] == 0:
        v1.pop(mx)
    if len(set(v1)) == 1:
        return True
    v2[mn] -= 1
    if v2[mn] == 0:
        v2.pop(mn)
    if len(set(v2)) == 1:
        return True
    return False


# word = "abcc"
# word = "aazz"
# word = "ddaccb"
# word = "abbcc"
word = "aabz"
print(equalFrequency(word))
