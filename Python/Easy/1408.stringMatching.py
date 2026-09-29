#1408. String Matching in an Array
#Beats: 29.28%
def stringMatching(words):
    output = []
    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] != words[j]:
                if words[i] in words[j]:
                    if words[i] not in output:
                        output.append(words[i])
    return output


# words = ["mass","as","hero","superhero"]
# words = ["leetcode","et","code"]
# words = ["blue","green","bu"]
words = ["leetcoder","leetcode","od","hamlet","am"]
print(stringMatching(words))
