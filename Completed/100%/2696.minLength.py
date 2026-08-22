# 2696. Minimum String Length After Removing Substrings
# Beats: 100.00%
def minLength(s):
    stack = []
    for i in range(len(s)):
        if stack and ((s[i] == "B" and stack[-1] == "A") or (s[i] == "D" and stack[-1] == "C")):
            stack.pop()
        else:
            stack.append(s[i])
    return len(stack)


s = "ABFCACDB"
s = "ACBBD"
print(minLength(s))

# Without Stack:
# Beats: 5.19%
# def minLength(s):
#     output = 0
#     while "AB" in s or "CD" in s:
#         for i in range(len(s)-1):
#             if s[i:i+2] == "AB":
#                 s = s[:i] + s[i+2:]
#                 output += 1
#                 break
#             elif s[i:i+2] == "CD":
#                 s = s[:i] + s[i+2:]
#                 output += 1
#                 break
#     return len(s)
