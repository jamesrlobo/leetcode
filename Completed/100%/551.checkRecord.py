# 551. Student Attendance Record I
def checkRecord(s):
    absent = s.count('A')
    if absent >= 2:
        return False
    if 'L' in s:
        for i in range(len(s)):
            if str(s[i:i+3]) == "LLL":
                return False
    return True


# s = "PPALLP"
# s = "PPAALL"
s = "AA"
print(checkRecord(s))
