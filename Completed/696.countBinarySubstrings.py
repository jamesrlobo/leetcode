# 696. Count Binary Substrings (Copied from solutions)
#Beats: 90.57%
def countBinarySubstrings(s):
    pre_len, cur_len, count = 0, 0, 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            cur_len += 1
        else:
            pre_len = cur_len
            cur_len = 1
        if pre_len >= cur_len:
            count += 1
    return count


s = "00110011"
s = "10101"
print(countBinarySubstrings(s))
