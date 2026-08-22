# 3. Longest Substring Without Repeating Characters
# Beats: 87.93%
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
def lengthOfLongestSubstring(s):
    output = []
    n = len(s)
    temp = ""
    for i in range(n):
        if s[i] in temp:
            output.append(len(temp))
            ind = temp.index(s[i])
            temp = temp[ind+1:] + s[i]
            # print(temp)
        else:
            temp += s[i]
            # print(temp)
    output.append(len(temp))
    return max(output)


# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = " "
s = "dvdf"
print(lengthOfLongestSubstring(s))

# Beats: 56.06%
# def lengthOfLongestSubstring(s):
#     output = 0
#     n = len(s)
#     temp = ""
#     for i in range(n):
#         if s[i] in temp:
#             output = max(output, len(temp))
#             ind = temp.index(s[i])
#             temp = temp[ind+1:] + s[i]
#         else:
#             temp += s[i]
#     output = max(output, len(temp))
#     return output
