# 1291. Sequential Digits
# https://leetcode.com/problems/sequential-digits/description/
# Beats: 100.00%
def sequentialDigits(low, high):
    output = []
    l = len(str(low))
    h = len(str(high))
    print(l, h)
    num = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(l, h+1):
        j = 0
        while j < len(num)-i+1:
            temp = (num[j:j+i])
            temp = int("".join(temp))
            print(temp)
            if temp >= low and temp <= high and temp not in output:
                output.append(temp)
            j+=1
    return sorted(output)


low = 100
high = 300

low = 1000
high = 13000
print(sequentialDigits(low, high))
