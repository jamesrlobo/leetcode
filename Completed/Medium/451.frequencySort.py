# 451. Sort Characters By Frequency
# Beats: 89.22%
def frequencySort(s):
    output = ""
    d = {}
    for i in (set(s)):
        d[i] = s.count(i)
    sorted_d = sorted(d.items(), key=lambda item:item[1], reverse=True)
    for j in sorted_d:
        output += j[0] * j[1]
    return output


# s = "tree"
# s = "cccaaa"
s = "Aabb"
print(frequencySort(s))
