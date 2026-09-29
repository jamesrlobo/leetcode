# 1903. Largest Odd Number in String
# Beats: 19.04%
# Copied from the solutions
def largestOddNumber(num):
    n = len(num)
    for i in range(n):
        number = num[n-1:n:]
        if(int(number)%2 != 0):
            return num[:n:]
        n-=1
    return ""


# num = "52"
# num = "4206"
num = "35427"
# num = "215466"
print(largestOddNumber(num))
