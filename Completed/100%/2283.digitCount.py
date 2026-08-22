# 2283. Check if Number Has Equal Digit Count and Digit Value
# Beats: 100.00%
def digitCount(num):
    for i in range(len(num)):
        if int(num[i]) != num.count(str(i)):
            return False
    return True


num = "1210"
num = "030"
print(digitCount(num))
