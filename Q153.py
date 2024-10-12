# Write a program to check if the input number is positive, negative or zero.
num = int(input("Enter number : "))
print('Number is negative.' if num < 0 else ('Number is positive.' if num > 0 else 'Number is zero.'))