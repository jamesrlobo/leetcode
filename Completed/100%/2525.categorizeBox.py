# 2525. Categorize Box According to Criteria
# Beats: 100.00%
def categorizeBox(length, width, height, mass):
    output = []
    volume = length * width * height
    if length >= 10**4 or width >= 10**4 or height >= 10**4 or mass >= 10**4:
        output.append("Bulky")
    if volume >= 10**9 and "Bulky" not in output:
        output.append("Bulky")
    if mass >= 100:
        output.append("Heavy")
    print(output)
    if output == ['Bulky', 'Heavy']:
        return "Both"
    elif output == ['Heavy']:
        return "Heavy"
    elif output == ['Bulky']:
        return "Bulky"
    else:
        return "Neither"


length = 2909
width = 3968
height = 3272
mass = 727

# length = 1000
# width = 35
# height = 700
# mass = 300

# length = 200
# width = 50
# height = 800
# mass = 50
print(categorizeBox(length, width, height, mass))
