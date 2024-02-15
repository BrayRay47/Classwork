points_possible = int(input('How many total points were possible? '))
points_earned = int(input('How many points did you earn? '))
grade = float(points_earned / points_possible * 100)

print(f'That is {grade}%')

if grade >= 72:
    print('You can enroll in data structures')

else:
    print('You should retake CS1')
