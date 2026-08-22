# 1957. Delete Characters to Make Fancy String
# Beats: 10.74%
def makeFancyString(s):
    s = s + "0" + "1"
    s = list(s)
    output = ""
    i = 2
    while i < len(s):
        print(s[i-2], s[i-1], s[i])
        if s[i-2] != s[i-1] or s[i-1] != s[i]:
            output += s[i-2]
            print("output:", output)
        i+=1
    return output



s = "leeetcode"
s = "aaabaaaa"
s = "aab"
print(makeFancyString(s))
