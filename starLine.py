stars = int(input("Please input a positive number: "))

while stars <= 0:
    stars = int(input("Please input a positive number: "))

print("Here is your art.")
for i in range(stars):   
    print("*", end = " ")

