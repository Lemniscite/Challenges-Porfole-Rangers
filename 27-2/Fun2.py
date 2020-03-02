#You are given an array of N elements. Your task is to write a program that calculates the sum of all distinct elements present in the array.



n= input()

n = n.split()

sum = n[0]
count =0


for y in range(1,len(n)):
    if n[count] == n[y]:
        y += 1
    else:
        sum += n[y]

print(sum)
        