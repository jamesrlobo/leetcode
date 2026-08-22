# 1047. Remove All Adjacent Duplicates In String
# Beats: 81.10%
def removeDuplicates(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)


s = "abbaca"
# s = "aaaaaaaa"
print(removeDuplicates(s))

# def removeDuplicates(s):
#     s = list(s)
#     i = 1
#     while i <= len(s):
#         if s[i-1] == s[i]:
#             s.pop(i)
#             s.pop(i-1)
#             if i > 2:
#                 i = i-2
#             else:
#                 i = 1
#         else:
#             i+=1
#         print(s)
#     return "".join(s)
