# 2710. Remove Trailing Zeros From a String
# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/
# Beats: 100.00%
def removeTrailingZeros(num):
    num = num[::-1]
    n = len(num)
    for i in range(n):
        if num[i] != "0":
            return num[i:][::-1]
    return num


num = "51230100"
# num = "123"
print(removeTrailingZeros(num))

# def removeTrailingZeros(num):
#     num = num[::-1]
#     output = ""
#     for i in range(len(num)):
#         if num[i] != "0":
#             output = num[i:]
#             break
#     return output[::-1]
