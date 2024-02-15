'''
File : quiz.py
Author : Diesburg
Description : Uses a WHILE structure to calculate
    the average score for N scores
    where N is provided by the user.
'''

numberOfQuizzes = int(input('Enter the number of quizzes: '))
total = 0
quizCount = 1

while quizCount <= numberOfQuizzes:
    scoreString = input('Enter the score on quiz ' + str(quizCount) + ': ')
    score = float(scoreString)
    total = total + score
    quizCount = quizCount + 1

average = total / numberOfQuizzes
print('The average quiz score is ' + str(average))
