# 202. Happy Number
# Beats: 100.00%
def isHappy(n):
    if n == 1 or n == 7:
        return True
    elif n < 10:
        return False
    else:
        output = 0
        for i in str(n):
            output += (int(i)**2)
    if output != 1:
        return self.isHappy(output)

n = 2
print(isHappy(n))
