print('Enter the scores one at a time.')
print('Enter -1 to signal that you are done.')

total = 0
count = 0

oneScore = int(input('Enter a score: '))

while oneScore != -1:
    total = total + oneScore
    count = count + 1
    oneScore = int(input("Enter a score: "))

average = total / count
print('The average of those ' + str(count) + ' scores is: ', average)
