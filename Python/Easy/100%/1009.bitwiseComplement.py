# 1009. Complement of Base 10 Integer
# Beats: 100.00%
def bitwiseComplement(n):
    s = list(bin(n)[2:])
    output = ""
    for i in range(len(s)):
        if s[i] == '1':
            output += "0"
        else:
            output += '1'
    return int(output,2)


# n = 5
# n = 7
n = 10
print(bitwiseComplement(n))
