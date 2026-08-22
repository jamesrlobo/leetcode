# 1461. Check If a String Contains All Binary Codes of Size K
# Beats: 8.81%
def hasAllCodes(s, k):
    output = []
    i = 0
    while i < len(s)-k+1:
        if len(s[i:i+k]) == k:
            output.append(s[i:i+k])
        i+=1
    print(output)
    print(len(output), 2**k)
    if len(set(output)) == 2 ** k:
        return True
    return False


s = "00110"
k = 2

# s = "00110110"
# k = 2

# s = "0110"
# k = 1

# s = "0110"
# k = 2

# s = "00000000001011100"
# k = 3
print(hasAllCodes(s, k))
