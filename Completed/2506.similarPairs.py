# 2506. Count Pairs Of Similar Strings
# Beats: 5.09%
def similarPairs(words):
    output = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and set(words[i]) == set(words[j]):
                output.append([words[i], words[j]])
    return len(output)//2


words = ["aba","aabb","abcd","bac","aabc"]
# words = ["aabb","ab","ba"]
# words = ["nba","cba","dba"]
print(similarPairs(words))
