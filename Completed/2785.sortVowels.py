# 2785. Sort Vowels in a String
def sortVowels(s):
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    v = []
    output = ""
    for i in range(len(s)):
        if s[i] in vowels:
            v.append(ord(s[i]))
    v = sorted(v)
    x = 0
    for j in range(len(s)):
        if s[j] not in vowels:
            output += s[j]
        else:
            output += chr(v[x])
            x = x+1
    return output



# s = "lEetcOde"
s = "lYmpH"
print(sortVowels(s))
