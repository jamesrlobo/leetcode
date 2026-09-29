# 1190. Reverse Substrings Between Each Pair of Parentheses
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
# Beats: 5.06%
def reverseParentheses(self, s: str) -> str:
    while "(" in s:
        start, end = -1, -1
        for i in range(len(s)):
            if s[i] == "(":
                start = i
            elif s[i] == ")":
                end = i
            if start > -1 and end > -1:
                temp = s[start+1:end]
                s = s[:start] + temp[::-1] + s[end+1:]
                break
    return s
