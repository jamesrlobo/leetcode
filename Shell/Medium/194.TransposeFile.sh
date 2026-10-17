#194. Transpose File
#https://leetcode.com/problems/transpose-file/description/
#Beats: 98.99%
# Read from the file file.txt and print its transposed content to stdout.
cat file.txt | awk '{for (i=1; i<=NF; i++) a[i] = (a[i] ? a[i] FS $i : $i)} END {for (i=1; i in a; i++) print a[i]}'
