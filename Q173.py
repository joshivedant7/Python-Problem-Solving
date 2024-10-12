#  Draw a pattern using a python program:
#  1
#  1  2
#  1  2  3
#  1  2  3  4
for i in range(1,5):
    for y in range(1,i+1):
        print(y,end="")
    print()