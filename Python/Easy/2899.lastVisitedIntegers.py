# 2899. Last Visited Integers
# Beats: 22.29%
def lastVisitedIntegers(nums):
    seen, ans = [], []
    k = -1
    for i in range(len(nums)):
        print(nums[i])
        if nums[i] > 0:
            seen = [nums[i]] + seen
            print("seen", seen)
        elif nums[i] == -1 and i == 0:
            k = 0
            ans.append(-1)
            print("ans:", ans)
        elif nums[i] == -1 and i != 0 and nums[i-1] != -1:
            k = 0
            if len(seen) > k:
                ans.append(seen[k])
                print("ans:", ans)
            else:
                ans.append(-1)
                print("ans:", ans)
        elif nums[i] == -1 and i != 0 and nums[i-1] == -1:
            k += 1
            if len(seen) > k:
                ans.append(seen[k])
                print("ans:", ans)
            else:
                ans.append(-1)
                print("ans:", ans)
    return ans


nums = [1,2,-1,-1,-1]
nums = [1,-1,2,-1,-1]
nums = [-1,-1,-1,27]
print(lastVisitedIntegers(nums))
