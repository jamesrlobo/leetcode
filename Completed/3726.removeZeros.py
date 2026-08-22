# 3726. Remove Zeros in Decimal Representation
# Beats: 20.88%
def removeZeros(n):
    output = [x for x in str(n) if int(x)!=0]
    return int("".join(output))


n = 1020030
# n = 1
print(removeZeros(n))

# def removeZeros(n):
#     output = ""
#     n = str(n)
#     for i in range(len(n)):
#         if (n[i]) != '0':
#             output += n[i]
#     return int("".join(output))
