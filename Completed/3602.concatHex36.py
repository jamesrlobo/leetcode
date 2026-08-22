# 3602. Hexadecimal and Hexatrigesimal Conversion
# Beats: 56.21%
def concatHex36(n):
    digits1 = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    digits2 = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    a = n*n
    output1 = ""
    while a > 0:
        rem = a%16
        output1 = str(digits1[rem]) + output1
        a //= 16
    b = n*n*n
    output2 = ""
    while b > 0:
        rem = b%36
        output2 = str(digits2[rem]) + output2
        b //= 36
    return output1+output2


# n = 13
n = 36
print(concatHex36(n))
