# 3751. Total Waviness of Numbers in Range I
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/description/
# Beats: 72.49%
def totalWaviness(num1, num2):
    waviness = 0
    for num in range(num1, num2+1):
        if num > 99:
            temp = str(num)
            print(temp)
            for i in range(1, len(temp)-1):
                if (temp[i - 1] > temp[i]) and (temp[i] < temp[i + 1]):
                    waviness += 1
                elif (temp[i - 1] < temp[i]) and (temp[i] > temp[i + 1]):
                    waviness += 1
                else:
                    break
    return waviness


num1 = 120
num2 = 130

num1 = 198
num2 = 202

num1 = 4848
num2 = 4848

num1 = 991
num2 = 991
print(totalWaviness(num1, num2))
