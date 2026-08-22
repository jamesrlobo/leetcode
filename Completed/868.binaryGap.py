# 868. Binary Gap
# Beats: 0.00%
def binaryGap(n):
    binary = bin(n)[2:]
    print(binary)
    if binary.count('1') < 2:
        return 0
    output, index = [], []
    n = len(binary)
    for i in range(n):
        if binary[i] == "1":
            index.append(i)
    # print(index)
    for j in range(len(index)-1):
        output.append(index[j+1]-index[j])
    return max(output)

n = 22
# n = 8
# n = 5
# n = 12
print(binaryGap(n))
