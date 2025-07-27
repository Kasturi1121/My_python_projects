import random
print("Let's play Hangman game")
list1=["apple","doggy","roses","kasturi"]
word=random.choice(list1)
#print(word)
count=[]
for l in word: 
    count+='-'
print(count)
letter=input("Guess a letter:")
if letter in word:
    letter=count[0]
print(count)


#Types of arguments  
def greet(name,dept,sub="some"):
    print(name)
    print(f"{name} is from {dept} and sub is {sub}")
greet(dept="Aiml",name="kasturi",sub="py")
#greet("py","Bangaram",dept="AIML",)

#arbitrary positional
def add(*num):
    c=0
    for i in num:
        c=c+i
    print(f"sum is {c}")
add(1,2,3,4,5,6,8,1)

#args and kwargs
def info(*num,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
        print(num)
info(1,2,3,4,5,name="kasturi",age=21,dept="AIML")

def multiply(*num):
    c=1
    for i in num:
        c*=i
    print(c)
multiply(2,3,4)
multiply(2,3,-6,8)
multiply(2,5,8,9,0,6)
import math
a=1.4
print(math.ceil(a))

import math
def wall(cover,height,width):
    paint=(height*width)/cover
    print(f"you will be required {math.ceil(paint)} paint cans")
h=int(input("enter height"))
w=int(input("enter weight"))
wall(7,height=h,width=w)

#prime or not
def prime(num):

    is_prime=True
    if num==1:
        is_prime=False
    for i in range(2,num):
        if num%i==0:
            is_prime=False
    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")            
n=int(input("enter a number"))
prime(num=n)