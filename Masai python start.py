1.Right effort, quantity,quality, direction
2.Honesty
3.Discipline
4.Deliberate Practice
5.Be better
6.Never give up
7.Be proactive
8.Follow instructions
9.Skillaton
10.Help others


https://masai-rangers.slack.com/

discipline@masaischool.com
	


#Arithmetic operation

value_1=6
value_2=4

ans = value_1 - value_2


# Conditional statements


num = 9

if num>7 and num=<9:
   print("Number bettween 9 and 12")
   
elif num==8:
   print(num)
else:
    print(num)






#Looping with for


for i in range(10):

     print("Hiro")



#Range(start,stop,jump)

for i in range(5,10,2):
    print(i)


#While

while True:
     print("Infinite")





# Is prime or not


n = int(input())
is_prime = True

for i in range(2,n):
     if n%i ==0:
	    is_prime = False
		break
	else:
	    is_prime = True

if is_prime==True:
 	print("yes")
else:
    print("no")	
	
	
## U can do with roots

import math 
n = int(input())
is_prime = True

for i in range(2,sqrt(n)):
     if n%i ==0:
	    is_prime = False
		break
	else:
	    is_prime = True

if is_prime==True:
 	print("yes")
else:
    print("no")	


#List

# indexing

lists = range(10)

print(lists[0])

for i in lists:
   print(lists[i])

#Slicing

lists = range(20)

print(lists[0:9])

print(lists[-6:2])


# Lists - sum

lists = range(20)
sum = 0

for i in lists:
   sum+=i
   
 # Products of num in lists
 lists = range(100)
 
 product = 0
 
 
 
 for i in lists:
    product = product * i
	

# New method to get elements


for i in range(length(lists)):
    print(lists[i])
	
#

List methods
key = input()

if key in numbers:
     print("present")
else:
   print("Not")
   
   
   
   
# Strings - sequence of char

name = "Masai School"

print(name[-3:])

# out ool - i mean name[-3], [-2] till last

# Concatenate

first_name = "Hiro"

last_name = "Hamada"

name = first_name + " " + last_name



# Functions


def name(nam):
   print("Your name is "+ str(name))
   return 
   
name("Hire")

# Functions and prime



# Taking inputs


m = input()



# printing
name = "Hiro"
age = 16
print("My name is %s and I am %d years young" %(name,age))


#float - %f
#integer - %d
#string - %s

#Lists without []
lists = range(16)

print(*lists)

# format

print("My name is {} and I am {} years young".format(name,age))

print("shahinapc","gmail",sep='@',end="\n")

# aman@masai



# Mutable - 


# Functiions


# passing args

# By value

def hi(x):
   print(x)
   
# By reference

def unlim(*args):
    print(args)

unlim(name="JDj",sdjs ="sds")	
#*args becomes a tuple


def unlimited(**kwargs):
    print(kwargs)

 	

#calling



#

#7/3

#9/3

#complexity Analysis 