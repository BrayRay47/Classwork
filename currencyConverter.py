"""
File: currencyConverter.py
Author: Braydon Cunningham
Description: A program to calculate the amount of Euros given for
the inputted amount of US Dollars.
"""

euro = (int(input("Enter US Dollars: ")) - 10) * .781

print("You will recieve", euro, "Euros in exchange")
