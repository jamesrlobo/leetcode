# 2595. Number of Even and Odd Bits
# Beats: 100.00%
def evenOddBit(n):
    s = (bin(n)[2:][::-1])
    # print(s)
    evenBit, oddBit = 0, 0
    for i in range(len(s)):
        if s[i] == "1":
            print(i)
            if i%2 == 0:
                evenBit +=1
            else:
                oddBit += 1
    return [evenBit, oddBit]


# n = 50
# n = 2
n = 5
print(evenOddBit(n))
