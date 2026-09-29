# 762. Prime Number of Set Bits in Binary Representation
# Beats: 35.78%
def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
    return True

def countPrimeSetBits(left, right):
    output = 0
    for i in range(left, right+1):
        if isPrime(str(bin(i)[2:]).count('1')):
            output +=1
    return output


left = 6
right = 10
print(countPrimeSetBits(left, right))
