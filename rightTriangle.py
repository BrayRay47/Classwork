height = int(input("Please input a positive height: "))

while height <= 0:
    height = int(input("Please input a positive height: "))

starCount = 1
spaceCount = height

print("Here is your art.")

for rows in range(height):
    for spaces in range(spaceCount - 1):
        print(end = "  ")
    for stars in range(starCount):
        print("*", end = " ")
    spaceCount = spaceCount - 1
    starCount = starCount + 1

    print()
