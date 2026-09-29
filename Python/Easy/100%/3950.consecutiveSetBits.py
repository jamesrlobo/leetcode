# 3950. Exactly One Consecutive Set Bits Pair
# https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/description/
# Beats: 100.00%
def consecutiveSetBits(n):
    result = str(bin(n)[2::])
    print(result)
    count = 0
    for i in range(len(result)-1):
        if result[i] == '1' and result[i+1] == '1':
            count += 1
            if count > 2:
                return False
    if count == 1:
        return True
    return False


n = 6
n = 5
n = 93
print(consecutiveSetBits(n))

# def consecutiveSetBits(self, n: int) -> bool:
#     result = bin(n).count('11')
#     return result == 1
