# 1763. Longest Nice Substring
# Beats: 23.44%
def longestNiceSubstring(s):
    output = ""
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            # print("Temp:", s[i:j])
            temp = s[i:j]
            if len(temp) >= 2:
                for ch in set(temp):
                    if ch.upper() not in temp or ch.lower() not in temp:
                        break
                else:
                    if len(temp) > len(output):
                        output = temp
    return output


s = "YazaAay"
s = "Bb"
s = "c"
print(longestNiceSubstring(s))
