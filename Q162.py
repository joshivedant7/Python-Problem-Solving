# Write a python program to display the Fibonacci sequence up to n-th term.
n = int(input('Enter n-th number : '))
if n == 1 :
    print('0')
elif n == 2 :
    print('0, 0')
else :
    a = 0
    b = 1
    c = a + b
    print(f"{a}, {b}, ",end="")
    for i in range(n - 2):
        c = a+b
        a = b
        b = c
        print(f"{c}, ",end ="")