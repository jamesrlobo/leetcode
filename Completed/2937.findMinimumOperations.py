# 2937. Make Three Strings Equal
# Beats: 28.10%
def findMinimumOperations(s1, s2, s3):
    count = 0
    if s1 == s2 == s3:
        return count
    minLen = min(len(s1), len(s2), len(s3))
    print("minLen:", minLen)
    while minLen > 0:
        if len(s1) > minLen:
            count += len(s1[minLen:])
            s1 = s1[:minLen]
        if len(s2) > minLen:
            count += len(s2[minLen:])
            s2 = s2[:minLen]
        if len(s3) > minLen:
            count += len(s3[minLen:])
            s3 = s3[:minLen]
        if s1 == s2 == s3:
            return count
        minLen -= 1
    return -1


s1 = "a"
s2 = "aabc"
s3 = "a"
print(findMinimumOperations(s1, s2, s3))
