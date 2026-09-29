# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/
# Beats: 100.00%
def lengthOfLastWord(self, s: str) -> int:
    s = s.split(" ")
    words  = [x for x in s if x != ""]
    return(len(words[-1]))
