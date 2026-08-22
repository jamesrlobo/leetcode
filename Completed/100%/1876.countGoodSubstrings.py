1876. Substrings of Size Three with Distinct Characters
Beats: 100.00%
def countGoodSubstrings(s):
    output = []
    for i in range(len(s)):
        if len(s[i:i+3]) == 3 and len(set(s[i:i+3])) == 3:
            output.append(s[i:i+3])
    return len(output)


# s = "xyzzaz"
s = "aababcabc"
print(countGoodSubstrings(s))
