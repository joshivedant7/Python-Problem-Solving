#  Write a python program to print all numbers between 1 and 100 (including 1 and 100) that are both, Disarium and Harshad numbers.
#  A number is said to be a Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself.
#  For example, 175 is a Disarium number as follows:
#  1**1+ 7**2 + 5**3 = 1+ 49 + 125 = 175
#  A harshad number is a number that is divisible by the sum of its digits. E.g., the number 18 is a harshad number, because 
# the sum of the digits 1 and 8 is 9 (1 + 8 = 9), and 18 is divisible by 9. 
def isDisarium(num):
    length = len(str(num))
    num1 = num
    sum = 0
    while num > 0 :
        temp = num % 10
        sum += temp**length
        length-=1
        num//=10
    return True if sum == num1 else False

def isHarshad(num):
    num1 = num
    sum = 0
    while num > 0:
        temp = num % 10
        sum += temp
        num //= 10
    return True if num1 % sum == 0 else False

x = int(input('Enter Number : '))
print('Number is Disarium : ',isDisarium(x))
print('Number is Harshad : ',isHarshad(x))