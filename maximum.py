"""
File : maximum.py
Author : CS 1510 and Braydon Cunningham
Description : Determines which of two exams had the better score
"""

examOne = input('What was your score on the first exam? ')
examTwo = input('What was your score on he second exam? ')

scoreOne = int(examOne)
scoreTwo = int(examTwo)

if scoreOne > scoreTwo:
    print('Your score of '+examOne+' on the first exam was higher.')

elif scoreOne < scoreTwo:
    print('Your score of '+examTwo+' on the second exam was higher.')

else:
    print('Your two exam scores were exactly the same.')

