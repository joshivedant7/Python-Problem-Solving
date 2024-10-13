# Ask the user to enter 10 test scores. Write a program to do the following:
# a)If user enters score greater than 100, then give warning to user that entered score is more than 100 and take that input again from user.  
# b)Print out the highest and lowest scores.
# c)Print out the average of the scores.
# d)Print out the second largest score.
# e)Drop the two lowest scores and print out the average of the rest of them.

max = None
sec_max = None
min = None
sec_min = None
sum = 0

for i in range(10):
    x = int(input('Enter score(0 to 100): '))
    if x > 100 or x < 0 :
        x = int(input('Enter valid score : '))
    if i == 0 :
        max = min = sec_max = sec_min = x
    if x > max:
        sec_max = max
        max = x
    elif x > sec_max :
        sec_max = x
    if x < min :
        sec_min = min
        min = x
    sum += x

print('Highest value : ',max)
print('Lowest value : ',min)
print('Second largest value : ',sec_max)
print('Avg test score : ',sum / 10)
print('After droping two lowest value Avg is :',(sum - min - sec_min)/8)