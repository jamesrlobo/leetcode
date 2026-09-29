# 3697. Compute Decimal Representation
# Beats: 100.00%
def decimalRepresentation(n):
    output = []
    length = len(str(n))
    for i in range(length):
        temp = n%10
        if temp != 0:
            output.append(temp*(10**i))
        n = n//10
    return output[::-1]


n = 537
n = 102
n = 6
print(decimalRepresentation(n))
