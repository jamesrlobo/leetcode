# 3582. Generate Tag for Video Caption
# Beats: 100.00%
def generateTag(caption):
    caption = caption.split()
    if caption == []:
        return "#"
    output = "#" + caption[0].lower()
    for i in range(1, len(caption)):
        output += caption[i][0].upper() + caption[i][1:].lower()
    if len(output) > 100:
        return output[:100]
    else:
        return output


# caption = "Leetcode daily streak achieved"
# caption = "can I Go There"
caption = "   "
# caption = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
print(generateTag(caption))
