# 3541. Find Most Frequent Vowel and Consonant
def maxFreqSum(s):
    vowels = ['a','e','i','o','u']
    max_vowels, max_consonants = 0, 0
    for i in s:
        if i in vowels:
            if s.count(i) > max_vowels:
                max_vowels = s.count(i)
        else:
            if s.count(i) > max_consonants:
                max_consonants = s.count(i)
    return max_vowels + max_consonants


# s = "successes"
s = "aeiaeia"
print(maxFreqSum(s))
