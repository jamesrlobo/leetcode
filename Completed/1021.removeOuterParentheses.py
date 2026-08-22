# 1021. Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/
# Beats: 23.96%
def removeOuterParentheses(s):
    n = len(s)
    stack = []
    output = ""
    for i in range(n):
        stack.append(s[i])
        if stack.count("(") == stack.count(")"):
            temp = "".join(stack)
            temp = temp[1:-1]
            stack = []
            output += temp
    return output


s = "(()())(())"
print(removeOuterParentheses(s))
