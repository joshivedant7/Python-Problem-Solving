#  Write a python program to read three numbers (a,b,c) and check how many numbers between ‘a’ and ‘b’ are divisible by ‘c’.
a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))
count = 0
for i in range(a,b + 1):
    if i % c == 0 : count+=1
print('Answer : ',count)