# 3270. Find the Key of the Numbers
# Beats: 30.00%
def generateKey(num1,num2,num3):
    output = []
    num1 = [int(x) for x in str(num1)]
    num2 = [int(x) for x in str(num2)]
    num3 = [int(x) for x in str(num3)]
    if len(num1) != 4:
        temp1 = 4 - len(num1)
        for i in range(temp1):
            num1.insert(0,0)
    if len(num2) != 4:
        temp2 = 4 - len(num2)
        for j in range(temp2):
            num2.insert(0,0)
    if len(num3) != 4:
        temp3 = 4 - len(num3)
        for k in range(temp3):
            num3.insert(0,0)
    for x,y,z in zip(num1, num2, num3):
        output.append(str(min(x,y,z)))
    return int("".join(output))


# num1 = 1
# num2 = 10
# num3 = 1000

# num1 = 987
# num2 = 879
# num3 = 798

num1 = 1
num2 = 2
num3 = 3
print(generateKey(num1,num2,num3))
