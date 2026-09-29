# 806. Number of Lines To Write String
def numberOfLines(widths, s):
    lines, pixels = 1, 0
    alpha_width = {}
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i, j in zip(alphabets, widths):
        alpha_width[i] = j
    for ch in s:
        if (pixels + alpha_width[ch]) > 100:
            lines += 1
            pixels = alpha_width[ch]
        else:
            pixels += alpha_width[ch]
    return [lines, pixels]


widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
# widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# s = "bbbcccdddaaa"
print(numberOfLines(widths, s))
