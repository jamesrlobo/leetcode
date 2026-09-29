# 3340. Check Balanced String
def isBalanced(num):
    odd, even = 0, 0
    for i in range(len(num)):
        if i%2 == 0:
            odd += int(num[i])
        else:
            even += int(num[i])
    return odd == even


# num = "1234"
num = "24123"
print(isBalanced(num))
