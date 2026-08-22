def countBits(n):
    output = []
    for i in range(n+1):
        output.append(int(str((bin(i)[2:]).count('1'))))
    return output


n = 5
print(countBits(n))
