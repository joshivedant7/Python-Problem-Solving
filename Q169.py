# Draw a pattern using a python program:
#  *  *  *  *
#     *  *  *
#        *  *
#           *
for i in range(1,5):
    print(' '*(i-1),end="")
    for y in range(i,5):
        print('*',end="")
    print()