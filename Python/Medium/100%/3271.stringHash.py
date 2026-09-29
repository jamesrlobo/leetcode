# 3271. Hash Divided String
# Beats: 100.00%
def stringHash(s, k):
    output = ""
    i, j = 0, k
    while i < len(s):
        substring = (s[i:j])
        temp = 0
        for ch in substring:
            temp += (ord(ch)-97)
        output += chr((temp%26)+97)
        i += k
        j += k
    return output


# s = "abcd"
# k = 2

s = "mxz"
k = 3
print(stringHash(s, k))

# def stringHash(s, k):
#     alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     output = ""
#     substrings = []
#     i = 0
#     while i < len(s):
#         substrings.append(s[i:k+i])
#         i+=k
#     for substring in substrings:
#         temp = 0
#         for ch in substring:
#             temp += (alphabets.index(ch))
#         output += alphabets[temp%26]
#     return output
