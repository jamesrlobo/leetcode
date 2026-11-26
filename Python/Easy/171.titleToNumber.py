# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/description/
# Beats: 33.86%
def titleToNumber(columnTitle):
    ans = 0
    n = len(columnTitle)
    for ch in range(n):
        # print(ord(columnTitle[ch])-64)
        ans = ans * 26 + ord(columnTitle[ch]) - 64
    return ans

columnTitle = "A"
columnTitle = "AB"
columnTitle = "ZY"
titleToNumber(columnTitle)
print(titleToNumber(columnTitle))
