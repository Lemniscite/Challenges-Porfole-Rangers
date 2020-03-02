#Count char fun game
                
s = str(input())
ans = ""
count = 1
current_char = s[0]

ans = ans+current_char

for i in range(1,len(s)):
    if s[i] == current_char:
        count+=1
    else:
        ans += str(count)
        ans += s[i]
        count = 1
        current_char = s[i]

ans += str(count)

print(ans)
    

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