import random

print("Let me think of the number range between 1 to 50")
num=random.randrange(50)
level=input("Choose level of difficulty...Type 'easy' or'hard'")
def easy():
    attempts=10
    while (attempts!=0) or (guess!=num):
        print(f"You have {attempts} attempts to guess the number: ")
        attempts-=1
        guess=int(input("Make a guess:"))
        if guess>num:
            print("Your guess is too High") 
        elif guess<num:
            print("Your guess is too Low")
    else:
        print("You have guess the correct number,You WON!!!!.The answer is ",num)
if level=="easy":
    easy()
else:
    print("Your guesses are over,You lose!!")
    

