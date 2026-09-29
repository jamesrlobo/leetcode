# 1103. Distribute Candies to People
# Beats: 78.84%
def distributeCandies(candies, num_people):
    output = [0] * num_people
    temp = 1
    while candies > 0:
        for i in range(num_people):
            output[i] += temp
            candies -= temp
            temp += 1
            print(output, temp, candies)
            if candies < temp:
                if i < len(output)-1:
                    output[i+1] += candies
                    return output
                else:
                    output[0] += candies
                    return output
    return output


# candies = 7
# num_people = 4

candies = 10
num_people = 3

candies = 80
num_people = 4
print(distributeCandies(candies, num_people))
