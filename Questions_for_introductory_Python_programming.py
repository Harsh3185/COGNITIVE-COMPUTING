#       1

print("Harsh Choudhary")


#       2

#2.1
a = 2
b = 4
print(a+b)

#2.2
a = "Hello "
b = "World"
print(a+b)

#2.3
a = "THIS IS : "
b = str(3)
print(a+b)


#       3

#3.1
a = int(input("Enter the Number :"))
if(a > 0):
    print("POSITIVE")
elif(a < 0):
    print("NEGATIVE")
else:
    print("ZERO")

#3.2
a = int(input("Enter the Number :"))
if(a %2 == 0):
    print("EVEN")
else:
    print("ODD")


#       4

#4.1
for i in range(1 , 11):
    print(i)

#4.2
i = 1
while(i < 11):
    print(i)
    i += 1

#4.3
sum = 0
for i in range(1 , 101):
    sum += i
print(sum)


#       5

#5.1
list1  = [34, 56, 31, 9, 78]
print("MAXIMUM NO. :" , max(list1))
print("MINIMUM NO. :" , min(list1))

#5.2
dic1 = {
    "name" : "Harsh",
    "Roll NO" : 102317157,
    "Branch" : "CSE"
}
print("Name is :" + dic1["name"])

#5.3
list1  = [34, 56, 31, 9, 78]

list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

#5.4
dic1 = {
    "name" : "Harsh",
    "Roll NO" : 102317157,
    "Branch" : "CSE"
}

dic2 = {
    "Group" : "2Q16",
    "Location" : "Jaipur"
}

dic3 = dic1|dic2
print(dic3)


#       6

#6.1
s = input("Enter the string")
count =0
for char in s:
    if(char in "aeiouAEIOU"):
        count += 1
print("Number of vowels :" , count)

#6.2
s = "Today is Sunday"
reversed_s = s[::-1]
print("Reversed : ", reversed_s)

#6.3
s = "Today is Sunday"
reversed_s = s[::-1]
if(reversed_s == s):
    print("Palindrome")
else:
    print("Not a palindrome")


#       7

#7.1
f=open("demo.txt","w")
f.write("Today is Sunday")
f=open("demo.txt","r")
data=f.read()
print(data)
f.close()

#7.2
f=open("demo.txt","a")
f.write(". Tomorrow is Monday")
f=open("demo.txt","r")
data=f.read()
print(data)
f.close()

#7.4
f=open("demo.txt","r")
lines = f.readlines()
print(len(lines))


#       8

#8.1
a=28
b=0
try:
    print(a/b)
except:
    print("Divided by zero")

#8.2
try:
    x=int(input("Enter a no."))
except:
    print("Need the number.")

#8.3
a=28
b=0
try:
    print(a/b)
except:
    print("Divided by zero")
finally:
    print("Program ended.")


#       9

#9.1
import random

for i in range(1, 6):
    n = random.randint(1,100)
    print(n)

#9.2
n = random.randint(1,100)

flag=True
for i in range(2,n):
    if(n%i==0):
        flag=False
        break

if(flag):
    print(n , " is prime")
else:
    print(n , " is not prime")

#9.3
x=random.randint(1,6)
print(x)

#9.4
list1=[5 ,8 , 9, 3, 7]
random.shuffle(list1)
print(list1)

#9.5
list1=[5 ,8 , 9, 3, 7]
x=random.randint(0,len(list1)-1)
print(list1[x])

#9.6
import random
import string
length = int(input("Enter the length : "))
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
print("password:", password)

#9.7
import random
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
card = random.choice(ranks) + random.choice(suits)
print("Random card :", card)


#       10

#10.1
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
print("Sum is ",a+b)

#10.2
s = input("Enter a string : ")
print("Your string is ",s)
print("Length is : ",len(s))



#       11

#11.1
import math
a = int(input("Enter a Number"))
print("Square is ", math.sqrt(a))

#11.2
import datetime

d = datetime.datetime.today()
print(d)

#11.3
import os
f = open("demo.txt", "r")
f.close() 
os.remove("demo.txt")  







