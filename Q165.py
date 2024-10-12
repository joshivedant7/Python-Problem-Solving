# Write a program to check whether a number is Armstrong number or not.
n = int(input("Enter number : "))
z=n
length  = len(str(n))
temp = 0
for i in range(length):
    digit = n % 10
    temp += digit**length
    n//=10
print('Is Armstrong number' if temp == z else "Ain't Armstrong number")