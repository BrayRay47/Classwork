"""
File: sphere.py
Author: Braydon Cunningham
Description: A program to calculate the circumference of a sphere given it's radius.
"""

PI = 3.14159

radiusString = input("Enter the radius of your circle: ")
radiusInteger = int(radiusString)

circumference = 2 * PI * radiusInteger
area = PI * (radiusInteger ** 2)

print("The circumference is:",circumference)
print("The area is:",area)
