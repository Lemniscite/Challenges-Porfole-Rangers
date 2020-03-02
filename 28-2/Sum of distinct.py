#You are given an array of N elements. Your task is to write a program that calculates the sum of all distinct elements present in the array.



n= list(input("Type n distinct elements"))
print(n)
distinct = set(n)


dear = map(int,distinct)

sum = 0

for i in dear:
    sum += i

    
    
print(sum)
