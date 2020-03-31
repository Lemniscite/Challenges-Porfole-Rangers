import time

t1=time.time()










def bin(arr,check):
    mid=len(arr)//2
    if mid<=0:
        return "Not present"

    
    if arr[mid]==check:
        return arr[mid]
    elif arr[mid]>check:
        return bin(arr[:mid],check)
    else:
        return bin(arr[mid:],check)
                   


print(bin(list(range(1000)),111))


t2=time.time()

print(t2-t1)

