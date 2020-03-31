import time

t1=time.time()

l = list(range(1000))
i=9
if i in l:
    print(i)
else:
    print("Not Present")
    



t2=time.time()

print(t2-t1)

