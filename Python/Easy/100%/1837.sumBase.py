# 1837. Sum of Digits in Base K
#Beats: 100.00%
def sumBase(n,k):
    digits = [x for x in range(k)]
    result = 0
    output = ""
    while n > 0:
        rem = n%k
        output = str(digits[rem]) + output
        n //= k
    for i in output:
        result += int(i)
    return result


n = 34
k = 6
# n = 10
# k = 10
print(sumBase(n,k))
