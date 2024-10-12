# Write a program to reverse a number.
num =  int(input("Enter number : "))
rev_num = 0
while 0 < num :
    temp = num % 10
    rev_num = rev_num*10 + temp 
    num //= 10
print("Revered Number is : ",rev_num)