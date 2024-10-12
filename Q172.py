# Draw a pattern using a python program:
#  1  2  3  4  5
#  1  2  3  4
#  1  2  3 
#  1  2  
#  1
for i in range(1,6):
    for y in range(1,6+1-i):
        print(y,end="")
    print()