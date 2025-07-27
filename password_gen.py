#Project-2
#PASSWORD GENERATOR
import random
num=[0,1,2,3,4,5,6,7,8,9]
sym=['~','!','@','#','%','$','^','&','*','(',')','_','+',';','"','?','{','}','|']
let=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print("Welcome to the Password Generator")
letters=input("How many letters would you like in your password?")
symbols=input("How many symbols would you like in your password?")
numbers=int(input("How many numbers would you like in your password?"))
letters=int(letters)
symbols=int(symbols)
password=[]
for i in range(1,numbers+1):
    char=random.choice(num)
    char=str(char)
    password+=char
    #print(n,end="")
for i in range(letters):
    char=random.choice(let)
    char=str(char)
    password+=char
    #print(l,end="")
for i in range(symbols):
    char=random.choice(sym)
    password+=char
    #print(s,end="")
#print("Your generated password is :",password)
random.shuffle(password)
#print(password)
passwords=""
for i in password:
    passwords+=i
print("shuffled password:",passwords)

