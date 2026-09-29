# 3838. Weighted Word Mapping
# Beats: 98.67%
def mapWordWeights(words, weights):
    output = ""
    reverse_alpha = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    for i in range(len(words)):
        # print(words[i])
        temp = 0
        for j in words[i]:
            temp += (weights[ord(j)-97])
        output += (reverse_alpha[temp%26])
    return output


words = ["abcd","def","xyz"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

words = ["a","b","c"]
weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

words = ["abcd"]
weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]
print(mapWordWeights(words, weights))
