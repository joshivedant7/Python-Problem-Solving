# Write a program to take 10 values from keyboard using loop and print their average on the screen
avg = 0
for i in range(10):
    a = int(input('Enter Number : '))
    avg+=a
print('Avg = ',avg/10)