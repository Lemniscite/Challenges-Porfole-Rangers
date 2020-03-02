
# CHecking palindrome

given =  str(input())
flag = "Yes"

if int(given) < 1000000:
    for i in range(len(given)):
        if given[i] == given[i*-1 -1]:
            flag = "Yes"
        else:
            flag = "No"
            break
print(flag)

