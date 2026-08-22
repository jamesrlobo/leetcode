# 1358. Number of Substrings Containing All Three Characters
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
def numberOfSubstrings(s):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n+1):
            temp = s[i:j]
            case_a, case_b, case_c = False, False, False
            for ch in temp:
                if ch == "a":
                    case_a = True
                elif ch == "b":
                    case_b = True
                elif ch == "c":
                    case_c = True
                if case_a == True and case_b == True and case_c == True:
                    count += 1
                    break
    return count

s = "abcabc"
print(numberOfSubstrings(s))
