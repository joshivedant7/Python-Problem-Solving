# Write a program to find average of first N natural numbers given by user.
num = int(input('Enter number : '))
ans = 0
for i in range(1 , num + 1):
    ans+=i
print('Avg : ', ans/num)