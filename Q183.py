#  Write a program to encode a number by changing the digits in the given positive integer by user. The rule for changing the digits in number will be:
#  If the digit in number is between 0 to 8 than replace the number with 1 to 9 respectively. (incrementing each digit by +1).
#  If the digit is 9, then replace it with 0.

user = int(input('Enter number :'))
ans = 0
c=0
while user > 0 :
    temp =user%10
    a = 0 if (temp == 9) else temp+1
    ans +=(a)*(10**c)
    c=c+1
    user = user // 10
print(ans)