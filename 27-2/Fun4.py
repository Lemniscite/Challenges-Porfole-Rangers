'''
You have decided to build a pyramid of stones on this new year. The simple rule is that the top level of the pyramid must consist of 1 stone, the second level must consist of 1 + 2 = 3 stones, the third level must have 1 + 2 + 3 = 6 stones, and so on.

Effectively, the i-th level of the pyramid contains 1 + 2 + ... + (i - 1) + i stones.

You have got n stones and have to build a pyramid from them.

Team Masai wants to know what is the maximum height of the pyramid that you can make using the given stones.
'''

##Tetrahedral numbers

n = int(input())

lists = []
if n<=10000:
    for i in range(100):
        lists = lists + [int(i*(i+1)*(i+2)/6)]



    for j in range(100):
        if lists[j]> n:
            print(j-1)
            break
        else:
            continue 
else:
    print("Overload")