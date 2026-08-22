# 2739. Total Distance Traveled
# Beats: 59.87%
def distanceTraveled(mainTank, additionalTank):
    distance = 0
    if mainTank >= 5 and additionalTank > 0:
        while mainTank >= 5:
            print(distance, mainTank, additionalTank)
            distance +=  (5 * 10)
            if additionalTank > 0:
                mainTank = mainTank-5 + 1
                additionalTank -= 1
            else:
                mainTank = mainTank-5
            print(distance, mainTank, additionalTank)
    print(distance, mainTank, additionalTank)
    if mainTank < 5 and additionalTank == 0:
        distance += (mainTank * 10)
    if mainTank < 5 and additionalTank > 0:
        distance += (mainTank * 10)
    if mainTank >= 5 and additionalTank == 0:
        distance += (mainTank * 10)
    return distance


# mainTank = 5
# additionalTank = 10
# mainTank = 9
# additionalTank = 2
mainTank = 1
additionalTank = 2
# mainTank = 10
# additionalTank = 1
print(distanceTraveled(mainTank, additionalTank))
