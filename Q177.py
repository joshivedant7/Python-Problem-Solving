# Draw a pattern using a python program:
#       1
#     1  2
#   1  2  3
#  1  2  3  4
n = 4
for i in range(1,n+1):
    print(' '*(n+1-i),end="")
    for z in range(1,i+1):
        print(z,' ',end="")
    print()