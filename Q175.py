# Draw a pattern using a python program:
#  *
#  #  #
#  *  *  *
#  #  #  #  #
for i in range(1,5):
    if i % 2 == 0 :
        print('#'*i)
    else : print('*'*i)