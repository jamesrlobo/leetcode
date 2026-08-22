# 476. Number Complement
def findComplement(num):
    s = list(bin(num)[2:])
    output = ""
    for i in range(len(s)):
        if s[i] == '1':
            output += "0"
        else:
            output += '1'
    return int(output,2)


num = 5
print(findComplement(num))
