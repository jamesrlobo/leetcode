# 791. Custom Sort String
# Beats: 100.00%
def customSortString(order, s):
    output = ""
    for i in order:
        for j in s:
            if i == j:
                output += i
        # print(output)
    for j in range(len(s)):
        if s[j] not in output:
            for k in range(s.count(s[j])):
                output += s[j]
        # print(output)
    return output

# order = "cba"
# s = "abcd"
# order = "bcafg"
# s = "abcd"
order = "hucw"
s = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
print(customSortString(order, s))
