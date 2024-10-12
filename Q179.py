# Draw a pattern using a python program:
#       *
#     #  #
#   *  *  *
#  #  #  #  #
n = 4
for i in range(1,n+1):
    print(' '*(n + 1 - i),end="")
    if i % 2 == 0 :
        print('# '*i)
    else : print('* '*i)