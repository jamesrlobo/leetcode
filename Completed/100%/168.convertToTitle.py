# 168. Excel Sheet Column Title
# Beats: 100.00%
def convertToTitle(columnNumber):
    result = []
    while columnNumber > 0:
        columnNumber = columnNumber - 1
        result.append(chr(columnNumber%26 + ord('A')))
        columnNumber = columnNumber//26
    return "".join(result[::-1])


columnNumber = 701
print(convertToTitle(columnNumber))
