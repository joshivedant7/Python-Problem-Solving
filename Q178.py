#  Draw a pattern using a python program:
#       1
#     2  2
#   3  3  3
#  4  4  4  4
n = 4
for i in range(1,n+1):
    print(' '*(n+1-i),end="")
    print((str(i)+' ')*i)