### My journal on contests in Masai. Started officially on 25-2-20

##27-2


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

'''
Sarvagaya is trapped in maze. The Masai command center sent him a string which decodes to come out from the maze. He is initially at (0, 0). String contains L, R, U, D denoting left, right, up and down. In each command he will traverse 1 unit distance in the respective direction.

For example if he is at (2, 0) and the command is L he will go to (1, 0).
'''

send = str(input())
send.upper()

x = 0
y = 0

if len(send)<200:
    for cmd in send:
        if cmd == 'L':
            x = x-1
        elif cmd == 'R':
            x = x+1
        elif cmd == 'D':
            y = y-1
        elif cmd == 'U':
            y = y+1
        else:
            break

print(x,y)




'''
You have decided to build a pyramid of stones on this new year. The simple rule is that the top level of the pyramid must consist of 1 stone, the second level must consist of 1 + 2 = 3 stones, the third level must have 1 + 2 + 3 = 6 stones, and so on.

Effectively, the i-th level of the pyramid contains 1 + 2 + ... + (i - 1) + i stones.

You have got n stones and have to build a pyramid from them.

Team Masai wants to know what is the maximum height of the pyramid that you can make using the given stones.
'''

####Tetrahedral numbers

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
        
'''
You are given an array of N elements. Your task is to write a program that calculates the sum of all distinct elements present in the array.
'''


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

## 28-2


# CHecking palindrome

given = input()

rev = given[::-1]

print(rev)


if given == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

#You are given an array of N elements. Your task is to write a program that calculates the sum of all distinct elements present in the array.



n= list(input("Type n distinct elements"))
print(n)
distinct = set(n)


dear = map(int,distinct)

sum = 0

for i in dear:
    sum += i

    
    
print(sum)

## End of Feb - missed sat 29th Feb cuz of not knowing about the day session of SAT
        
## Start of March		
##3-3 Tuesday
'''You are given an array of N integers. Output "Yes" if 42 is present in array, else print "No".

Input Format

First line contains number of integers N present in the array.

Second line contains N space separated integers.

Constraints

N<100

Output Format

Output Yes/No based on condition mentioned above
'''


n = int(input())
ans = input()
num_list = ans.split()

flag = "No"
for i in num_list:
    if i == "42":
        flag = "Yes"

    
print(flag)


'''
You are provided 3 integers: left, right and k. Your task is to write a program that finds out count of all such numbers between left and right (both inclusive) which are divided by k.

Input Format

First line contains 3 space separated integers which are left, right and k respectively.

Constraints

l,r,k<10000

Output Format

Output the count of such numbers

'''




ins = input()
new = list(map(int,ins.split()))

print(int(new[1]/new[2]))

'''

You are given an array of N positive integers. Write a program to output the product of all the elements present in the array.

Input Format

First line contains N.

Second line contains N space separated integers

Constraints

N<100

Output Format

Output one number which is the product of all elements.

Sample Input 0

5
3 5 2 9 4
Sample Output 0

1080

'''

n = input()
ins = list(map(int,input().split()))
pro = 1
def multiply(li):
    pro = 1
    for i in li:
        pro = pro*i
        
    return pro

result = multiply(ins)

if result in ins:
 	print(result)

'''

You are programming an elevator that allows only persons with weight less than 85 to enter it, otherwise it beeps. You are provided weight of n persons in form of an array. Your task is to print either Beep or Enter depending on weight of person.

Effectively, write a program that iterates through an array of n elements and prints "Beep" (without quote) in a new line if weight is greater than or equal to 85, otherwise print "Enter" (without quote).

Input Format

First line contains N which is the number of elements present in the array.

Second line contains N space separated integers.

Constraints

N<100

Output Format

Output N strings (either Beep or Enter depending on the value present)

Sample Input 0

5
24 83 89 43 91
Sample Output 0

Enter
Enter
Beep
Enter
Beep
'''

n = input()
ins = list(map(int,input().split()))

for i in ins:
    if i < 85:
        print("Enter")
    else:
        print("Beep")
'''
Given an array A of N integers. Your task is to print that integer which is present maximum number of times in the given array.

If there are two elements present maximum number of times, print the one which is comes first in the array.

Input Format

N<100

Constraints

The array contains integers only

Output Format

Print one integer, the one which is present the maximum number of times.

Sample Input 0

5
0 2 0 6 9
Sample Output 0

0	
		
'''		
		



n = input()
ins = list(map(int,input().split()))

frequent = max(set(ins), key = ins.count) 


print(frequent)

'''
You are given N integers, your task is to write a program that finds the integer present after 2 in the sequence of numbers given. In case 2 is not present or 2 is the last element, print -1.

Input Format

First line of the input contains N

Second line of the input contains N space separated integers.

Constraints

N<10000

Output Format

Output number present after 2.

In case there's no number present after 2, print -1

Sample Input 0

5
3 4 2 0 1
Sample Output 0

0

'''

n = input()
ins = list(map(int,input().split()))

def after_2(li):
    update = 100000
    for i in range(len(li)-1):
        if li[i] == 2:
            update = li[i+1]
    
    
        
    return update
        
result = after_2(ins)

if result == 100000 or ins[-1] == 2:       

    result = -1
    
    
print(result)





##4-3

'''
You are given a number N, find sum of all odd numbers present below it. (including N if N is an odd number)

Input Format

First and the only line contains number N

Constraints

N<100000

Output Format

Output the sum of all such numbers

Sample Input 0

7
Sample Output 0

16

'''
n = int(input())
sum = 0
for i in range(n+1):
    if i%2 !=0:
        sum+=i
        
  
print(sum)

'''
You are working for Masai Airline. There are n passengers with 2 bags each (one check-in and other hand bag). The limitation for check-in bag is 15kgs and that for hand bag is 7kgs. You are given 2 arrays: First array contains weight of check-in bag of ith passenger. Similarly, second array contains weights of hand bag of ith passenger. Print "Boarding" (without quotes) if the passenger clears both luggage weight limits of Masai Airline, else print "Stop" (without quotes).

Please note that 15 kgs and 7 kgs are inclusive.

Input Format

First line contains n (number of passengers)

Second line contains n positive integers which are the weights of check-in bag of ith passenger.

Third line contains n positive integers which are the weights of hand bag of ith passenger.

Constraints

n<1000

Output Format

Output "Boarding" (without quotes) or "Stop" (without quotes) of the passenger meets criteria of Masai Airlines.

Sample Input 0

4
12 14 15 6
8 5 7 4
Sample Output 0

Stop
Boarding
Boarding
Boarding
Explanation 0

Since, the hand bag of first person is 8kgs (greater than 7kgs), therefore stopped.

'''


n = int(input())
lug = list(map(int,input().split()))
hand = list(map(int,input().split()))
flag = "Boarding"

def board(lug,hand):
    i = lug 
    y = hand
    if i>15 or y > 7:
        flag = "Stop"
        print(flag)
    else:
        flag ="Boarding"
        print(flag)

answer = list(map(board,lug,hand))




'''


You are given an integer N. Your task is to find if the string 420 is present in it or not.

Print "Caught" (without quotes) if 420 is present in it. Otherwise "Escaped" (without quotes) if 420 is not present in it.

Input Format

You are provided an integer N.

Constraints

N<1000000

Output Format

Output an string based on the conditions mentioned above.

Sample Input 0

97420
Sample Output 0

Caught
Explanation 0

97420 contains 420.

Hence output is "Caught"

Contest ends in 2 hours
Submissions: 9
Max Score: 10
Rate This Challenge:

    
More

'''

n = list(input())

ins = list(map(int,n))
flag = "Escaped"



for i in range(len(ins)-1):
    i = i+1
    if ins[i] == 4:        
        
        if ins[i+1] == 2:
            if ins[i+2] ==0:
                
                flag = "Caught"
                break    
print(flag)
  




'''



Haren wants to change his profile picture on Facebook. Now Facebook has some restriction over the dimension of picture that we can upload.

Length of every picture uploaded should be greater than L and width should be greater than W

If his picture passes both the criteria, print "Upload"

In case it could not pass becuase of length, print "Increase Length"

In all other cases, print "Increase Width"

Input Format

First line contains 2 space separated integers which are L and W

Second line contains length and width of uploaded pic

Constraints

L,H<100

Output Format

Output one of the strings based on condition met

Sample Input 0

12 14
8 19
Sample Output 0

Increase Length

'''

n = input()
y = input()
L,W = list(map(int,n.split()))
l,w = list(map(int,y.split()))

if l > L and w > W:
    print("Upload")
else:
    print("Increase Length")




#Largest palindromical substring











##5-3
'''
	JEE is one of the most prestigious exams. You need to implement ranking rule in it. Given marks of Physics, Chemistry and Mathematics of two students, Find out the winner using below rules:

=> If total marks of one student is greater than other, he/she wins

=> If total marks of both the students are same, then the one having more marks in Maths wins. In case their marks in maths are also same, the one whose marks in Physics is more wins the game.

Input Format

First line of input contains 3 space separated integers which is the marks in physics, chemistry and mathematics respectively of first student

Second line of input contains 3 space separated integers which is the marks in physics, chemistry and mathematics respectively of second student

Constraints

Marks < 36000

Output Format

Output "First" (without quotes) if first student wins.

In all other case print "Second"

'''




n = input()
n2 = input()
ins_1 = list(map(int,n.split()))
ins_2 = list(map(int,n2.split()))


if sum(ins_1)>sum(ins_2):
    print("First")
else:
    print("Second")
    
'''
You are given an array of N-1 integers and integers are in the range of 1 to N. There are no duplicates in the array. One of the integers is missing in the array. Find the missing integer

Input Format

The first and only line contains N-1 integers

Constraints

N<100

Output Format

Print the one number belonging from 1 to N which is not present in the array

Sample Input 0

4 5 1 3
Sample Output 0

2

'''

n = input()
ins = list(map(int,n.split()))

ranger = len(ins)

for i in range(1,ranger+1):
    if i not in ins:
        print(i)
		
		
'''

You are given an array of n integers. You have to equalize all elements of the array in minimum possible operation.

In ONE operation, you can increase any of the n-1 elements of the array by 1. That is, except for one element of the array, you can increment all other integers by 1.

Output the minimum number of operations required to equalize all elements of array.

Input Format

First line contains n

Second line contains n space separated integers which are elements of array

Constraints

n<1000

Output Format

Output one number, which is the minimum number of operations required to perform in order to make all the elements of array equal

Sample Input 0

3
1 2 3
Sample Output 0

3
'''
n = input()
ins = list(map(int,input().split()))
maxx = max(ins)
min = min(ins)
ins.sort()
count = 0


for i in ins:
    while i<maxx:
        i+=1 
        count+=1
print(count)

'''

You are given the distance travelled by a car(in kilometres) in certain time (in hours). If the speed of that car is greater than 40 km/hr, you have to print "Apply Brake" (without quotes), else in all other conditions, print "Keep Going" (without quotes)

Input Format

First line contains 2 space separated integers whers first integer represents the distance travelled by car and second represents time taken to cover that distance.
   
   
   

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
ins = list(map(int,input().split()))
#s = d/t

s = int(ins[0]/ins[1])

if s>40:
    print("Apply Brake")
else:
    print("Keep Going")



   k = int(input())
arrival = list(map(int, input().split()))
depart = list(map(int, input().split()))

d2 = [arrival,depart]
print(d2)

        
available = k
occupied = 0
temp_y = 0

for i in arrival:
    for y in arrival:
        
        
   
   
  for i in arrival:
    for y in depart:
        occupied +=1
        available-=1
        if y >= depart[depart.index(y) +1]
		
		
#SIr answ

#list of tuples -new concept

k = input()
arrival = list(map(int,input().split()))
depart = list(map(int,input().split()))

flag = True
li = []
cnt = 0
for i in arrival:
    li.append((i,'a'))
for i in depart:
    li.append((i,'d'))
li.sort()

for i in range(len(li)):
     if li[i][1] == 'a':
	    cnt += 1
	else:
	    cnt -= 1
	if cnt >k:
	   flag = False
	
if flag:
    print("Possible")
else:
    print("Not Possible")
	''' 
You are given scores of last N matches of two different batsmen in form of arrays. Your task is to print the ceil value of better average among the two in case that value is even. If that value is not even, print -1.

Input Format

First line contains the number of matches N.

Second line contains N space separated integers describing scores of first batsman. Third line contains N space separated integers descibing scores of second batsman.

Constraints

N<100

Output Format

Print an integer which can either be ceil of better average of the two batsmen or -1 depending upon the ceil of better average.

Sample Input 0

3
10 20 30
40 80 60
Sample Output 0

60
Explanation 0

Here, the number of matches is 3. And average of first batsman is 20 while average of second batsman is 60. Since 60>20 and 60 is also even, 60 is the output. 	 
'''	 
	 
	 

n = int(input())
fir = list(map(int,input().split()))
sec = list(map(int,input().split()))

def avg(x):
    avg = sum(x)/len(x)
    return int(avg)


best = max(avg(fir),avg(sec))

if best%2==0:
    print(best)
else:
    print(-1)

'''
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, the word anagram can be rearranged into nag a ram.

Given 2 phrases, write a program that detects if both are anagrams of each other.

If both are anagrams, print "True"

Else print "False"

Input Format

First line of input contains first phrase

Second line of input contains second phrase

Constraints

Length of each phrase < 1000

Output Format

Output a string based on conditions mentioned above

Sample Input 0

anagram
nag a ram
Sample Output 0

True

'''
orig = input()
anagram = input().split()
str_ana=""

for i in anagram:
    str_ana += str(i)


sorted_ana = ''.join(sorted(str_ana))
sorted_orig = ''.join(sorted(orig))


if sorted_ana == sorted_orig:
    
    print(True)
else:
    print(False)
 
##9/3
'''
Sprint 2B
Problem
Submissions
Leaderboard
Discussions
You are given the numbers of 1 runs, 2 runs, 3 runs, fours and sixes scored by a batsman. Your task is to compute total run scored by that batsman.

Input Format

First line contains 5 positive space separated integers which represents number of 1s, 2s, 3s, fours and sixes scored by the batsman.

Constraints

All the scores<100

Output Format

Output total run scored by the batsman

Sample Input 0

12 8 5 6 3
Sample Output 0

85
'''


one,two,three,four,six = input().split()

sum = int(one)*1+int(two)*2+int(three)*3+int(four)*4+int(six)*6
print(sum)

'''

You are given a string S. Your task is to write a program that comments if it has all unique character or not (no repeated character).

If it has just unique character, output "Unique"

Else in all other cases, output "No"

Input Format

First and the only line contains string S

Constraints

Length of S < 1000

Output Format

Output one string based on string

Sample Input 0

masai
Sample Output 0

No
'''
n = input()

new =set(n)
if len(n) == len(new):
    print("Unique")
else:
    print("No")
	
'''
	
You are given 3 parameters of two different cricket teams in World Cup Final.

First parameter : Score

Second parameter : Score in super over

Third parameter : Total number of fours scored in the inning.

If first parameter of any one team is greater than other then that team wins.

If first parameter of both the teams are same, then the team whose second parameter is greater wins the match.

In case the second parameter is also same, then the team that has higher value of third parameter wins the game.

Input Format

First line contains the three discussed parameter for New Zealand

Second line contains three discussed parameters for England

Constraints

All parameters < 10000

Output Format

Output "England" (without quotes) if England wins the game, else print "New Zealand" if New Zealand wins the game.

Sample Input 0

241 15 21
241 15 26
Sample Output 0

England
'''
zea_sc = list(map(int,input().split()))
eng_sc = list(map(int,input().split()))


ans=""
for i in range(len(eng_sc)):
    z = zea_sc[i]
   

    
    e=eng_sc[i]
 
    if z>e:
        
        ans = "New Zealand"
        break       
    elif e>z:
        

        ans = "England"
        
        break
    else:
        i+=1
        
        
 

print(ans)
'''
    
    You are given an array A of N elements. Write a program that counts the number of sub-arrays of A in which sum of all the elements is an even number.

Please read sample test case and its explanation for better understanding.

Input Format

First line contains N which is the number of elements present in the array.

Second line contains N space separated integers which are the elements of array A

Constraints

1 ≤ N ≤ 100000

1 ≤ Elements of array ≤ 1000000

Output Format

Output one number which is the count of such sub-arrays

Sample Input 0

5
2 5 4 4 4
Sample Output 0

7
Explanation 0

All the even sum subarrays are:
1) [1,1] (i.e from index 1 to index 1)
2) [3,5] (i.e from index 3 to index 5)
3) [3,4] (i.e from index 3 to index 4)
4) [4,5] (i.e from index 4 to index 5)
5) [3,3] (i.e from index 3 to index 3)
6) [4,4] (i.e from index 4 to index 4)
7) [5,5] (i.e from index 5 to index 5)
'''


ele = int(input())
li = list(map(int,input().split()))
def even_sum(arr, n): 
    result = 0
  
   
    for i in range(0, n, 1): 
        sum = 0
        for j in range(i, n, 1): 
            sum = sum + arr[j] 
            if (sum % 2 == 0): 
                    result = result + 1
  
    return (result) 

print(even_sum(li,ele))
'''
There is a long queue of people in front of ATMs. Due to withdrawal limit per person per day, people come in groups to withdraw money.

Groups come one by one and line up behind the already present queue. The groups have a strange way of arranging themselves. In a particular group, the group members arrange themselves in increasing order of their height(not necessarily strictly increasing). Effectively, all people who have lined up in increasing order of height form one group
Find the minimum number of groups that can be observed in the queue?

Input Format

The first line of input contains one positive integer N. The second line contains N space-separated integers H[i] denoting the height of i-th person. Each group has group members standing in increasing order of their height.

Constraints

N <= 1000000

H[i] <= 1000000

Output Format

Print the minimum number of groups that are at least present in the queue?

Sample Input 0

6
1 2 4 3 5 8
Sample Output 0

2

'''

    

n = int(input())
gp=list(map(int,input().split()))
count = 0
set = []

for i in gp:
    if i > gp.index(i)+1:
        count+=1
            
print(count)

'''

Noddy choosed a city for Advertising his company's product. There are S streets in that city. Each day he travels one street. There are N buildings in a street which are located at points 1,2,3....N(respectively). Each building has some height(Say h meters).

Noddy stands at point 0. His height is 0.5m. Now he starts communicating with the people of each building. He can communicate with people of a particular building only if he can see that building. If he succeed to communicate with any particular building then his boss gives him R rupees. i.e. if he communicates with K buildings in a day, then he will earn K times R rupees. Now Noddy wants to know his maximum Earning for each day.

Note: All the points are on Strainght Line and Noddy is always standing at point 0.

Input Format

First line of input contains an integer S, denoting no of streets in the city.

Details for each street is described in next two lines.

First line contains two integers N and R denoting no of buildings in the Street and earning on communicating with a building.

Second line contains N integers, denoting height of building.

Constraints

N <= 10000

h <= 1000000000

S <= 100



R <= 10000

Output Format

Print S Lines, each containing maximum earning in i-th street.

Sample Input 0

2
6 3
8 2 3 11 11 10
5 12
12 20 39 45 89
Sample Output 0

6
60
Explanation 0

There are two streets in the city.


The first street has 6 buildings and the earning of Napoleon for communicating with each building is 3 rupees.

Height of buildings are 8 2 3 11 11 10 respectively.

As Noddy is standing at point 0, he will be able to see only 1st and 4th building.

So his total earning will be 3*2 = 6 in that street

Similarly for 2nd street his earning will be 60 rupees
'''
    
     

streets = int(input())
n,r= list(map(int,input().split()))
h=list(map(int,input().split()))
n2,r2= list(map(int,input().split()))
h2=list(map(int,input().split()))

def maxearn(r,h):
    count = 1
    flag = h[0]
    for i in range(1,len(h)):
        
        if h[i]>flag:
            count+=1
            flag=h[i]
    result = count*r
    
    return result

mii =maxearn(r,h)
print(mii)
print(maxearn(r2,h2))


## 13-3

'''
Alt Sum

You are given an array of N integers. Your task is to write a program that calculates the sum of all alternate elements starting from the first(0th index element of array) integer.

Input Format

First line contains N

Second line contains N space separated integers

Constraints

N<1000

Output Format

Output the sum under above conditions

Sample Input 0

7
4 5 5 5 6 6 7
Sample Output 0

22
'''

n = int(input())
arr = list(map(int,input().split()))
sum = 0
for i in range(0,n,2):
    sum += arr[i]
    
print(sum)
  
 '''
	
For last N days, you did nothing but eat, sleep and code.

A close friend of you kept an eye on you for last N days. For every single minute of the day, he kept track of your actions and prepared a log file.

The log file contains exactly N lines, each line contains a string of length 1440 ( i.e. number of minutes in 24 hours of the day). The string is made of characters E, S, and C only; representing Eat, Sleep and Code respectively. ith character of the string represents what you were doing during ith minute of the day.

Your friend is now interested in finding out the maximum of longest coding streak of the day - X. He also wants to find the longest coding streak of N days - Y. Coding streak means number of C's without any E or S in between.

See sample test case for clarification.

Input Format

First line of each file contains N - number of days.

Following N lines contains a string of exactly 1440 length representing his activity on that day.

Constraints

1 ≤ N ≤ 365

String consists of characters E, S, and C only.

String length is exactly 1440.

Note: The sample test case does not follow the given constraints on string length to avoid large data. It is meant only for explanation. We assure you that the hidden test files strictly follow the constraints.

Output Format

Print X and Y separated by a space in a single line.

Sample Input 0

4
SSSSEEEECCCCEECCCC
CCCCCSSSSEEECCCCSS
SSSSSEEESSCCCCCCCS
EESSSSCCCCCCSSEEEE
Sample Output 0

7 9
'''


ins = int(input())
arr = input().split('\n')
for i in range(ins-1):
    arr+=input().split('\n')
#### Max of code streaks
cout = []
for i in range(ins):
    count=0
    count_max=0
    kk = arr[i]
    for y in kk:
        if y=='C':
            count+=1
        else:
            if count_max<count:
                count_max = count
            count=0
    cout.append(count_max)
#Longest code streak
arr_streak = ""
for i in arr:
    arr_streak+=i
con =0
con_max=0
for i in arr_streak:
    if i=='C':
        con+=1
    else:
        if con_max<con:
            con_max = con
        con=0
#Display
print(max(cout),con_max)
 

 

##14-3 Sat morning session
'''Bubble Sort Problem

You are given an array of N unsorted numbers. Your task is to write BUBBLE SORT such that numbers present in the array gets sorted.
'''


n = int(input())
li = list(map(int,input().split()))
temp =0

for bling in range(n):
    for z in range(n-1):
        i = li[z]
        if i>li[z+1]:
            li[li.index(i)]= li[z+1]
            li[z+1] = i
       

print(*li)


'''
Amit went down to the Samosa street to have some. But he only has K units of money with him. There are N shops on the street and unfortunately, all of them have only one samosa remaining. You are also given an array A, where Ai is the cost of a samosa on the i'th shop.

Find the maximum samosas that Amit can eat.

Input Format

First line contains two space-separated integers N and K.

Second line contains N space separated integers, the cost of a samosa on the shops.

Constraints

1 ≤ N ≤ 1000

0 ≤ K ≤ 1000

0 ≤ Ai ≤ 100

Output Format

Print the required answer

Sample Input 0

4 10
5 4 2 4
Sample Output 0

3


'''''

ins = list(map(int,input().split()))

cost = list(map(int,input().split()))
cost.sort()
balance = ins[1]
maxs = 0
for i in cost:
    if balance>=i:
        balance =balance- i
        maxs+=1
        
    else:
        break
print(maxs)
        
		
'''
Hassan has discovered his own sorting algorithm. The algorithm has following conditions:

Given an integer k, sort the values in the array according to their modulo with k. That is, if there are two integers a and b, and a%k < b%k, then a would come before b in the sorted array.

If a%k = b%k, then the integer which comes first in the given array remains first in the sorted array.

Your task is to write a program that sorts the given array as per above mentioned condition and print the sorted array.

Input Format

The first line consists of two integers N and k, N being the number of elements in the array and k is the number with which we need to take the modulo.

The next line consists of N space separated integers , denoting the elements of the array A.

Constraints

N < 10000

K < 1000000000

Integers of array < 10000000000

Output Format

Print the modulo sorted array of the given array.

Sample Input 0

5 6
12 18 17 65 46
Sample Output 0

12 18 46 17 65
Explanation 0

12%6=0
18%6=0
17%6=5
65%6=5
46%6=4
So, the sorted order is: 12 18 46 17 65
12 and 18 have same result on modulo , so, 12 remains first in sorted array as it is first in given array
'''

ins = list(map(int,input().split()))
li = list(map(int,input().split()))
n = ins[0]
k = ins[1]


for bling in range(n):
    for z in range(n-1):
        i = li[z]
        if i%k>li[z+1]%k:
            li[li.index(i)]= li[z+1]
            li[z+1] = i
        
            
       

print(*li)