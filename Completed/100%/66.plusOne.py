# 66. Plus One
# Beats: 100.00%
def plusOne(digits):
    temp = ""
    output = []
    for i in digits:
        temp += str(i)
    temp = int(temp)+1
    for j in str(temp):
        output.append(int(j))
    return output


digits = [1,2,3]
digits = [4,3,2,1]
digits = [9]
digits = [9,9]
print(plusOne(digits))
