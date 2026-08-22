# 1816. Truncate Sentence
# Beats: 100.00%
def truncateSentence(s, k):
    s = s.split(" ")
    s = s[:k]
    print(s)
    return " ".join(s)


s = "Hello how are you Contestant"
k = 4
print(truncateSentence(s, k))
