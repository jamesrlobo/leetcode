# 2396. Strictly Palindromic Number
# Beats: 100.00%
def isStrictlyPalindromic(n):
    result = []
    for i in range(2, n-1):
        if base(n, i) != base(n, i)[::-1]:
            return False
    return True
    # for item in result:
    #     if item != item[::-1]:
    #         return False
    # return True

def base(num, k):
    digits = [x for x in range(k)]
    output = ""
    while num > 0:
        rem = num%k
        output = str(digits[rem]) + output
        num //= k
    return output


n = 9
# n = 4
print(isStrictlyPalindromic(n))
