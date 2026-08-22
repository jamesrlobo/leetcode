# 989. Add to Array-Form of Integer
# Beats: 15.56%
def addToArrayForm(num, k):
    n = 0
    for i in num:
        n = n*10 + i
    n += k
    num = []
    while n!= 0:
        num.append(n%10)
        n = n//10
    return num[::-1]


num = [1,2,0,0]
k = 34

num = [2,7,4]
k = 181

num = [2,1,5]
k = 806
print(addToArrayForm(num, k))
