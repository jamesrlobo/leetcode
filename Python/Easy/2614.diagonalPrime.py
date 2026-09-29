# 2614. Prime In Diagonal
# Beats:51.25%
def diagonalPrime(nums):
    def isPrime(k):
        if k <= 1:
            return False
        else:
            for i in range(2, int(k**0.5)+1):
                if k%i == 0:
                    return False
        return True
    output = []
    for i in range(len(nums)):
        if isPrime(nums[i][i]):
            output.append(nums[i][i])
        if isPrime(nums[i][len(nums[i])-(i+1)]):
            output.append(nums[i][len(nums[i])-(i+1)])
    # for j in range(len(nums)):
    #     if isPrime(nums[j][len(nums[j])-(j+1)]):
    #         output.append(nums[j][len(nums[j])-(j+1)])
    return max(output)


nums = [[1,2,3],[5,6,7],[9,10,11]]
print(diagonalPrime(nums))

# def diagonalPrime(nums):
#     def isPrime(k):
#         if k <= 1:
#             return False
#         else:
#             for i in range(2, int(k**0.5)+1):
#                 if k%i == 0:
#                     return False
#         return True
#     output = []
#     diagonals = []
#     for i in range(len(nums)):
#         if nums[i][i] not in diagonals:
#             diagonals.append(nums[i][i])
#     for j in range(len(nums)):
#         if nums[j][len(nums[j])-(j+1)] not in diagonals:
#             diagonals.append(nums[j][len(nums[j])-(j+1)])
#     for k in diagonals:
#         if isPrime(k):
#             output.append(k)
#     return max(output)
