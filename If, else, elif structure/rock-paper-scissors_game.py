import random
print("***WELCOME TO THE GAME***")
print("MAKE YOUR CHOICE COME TO COMPUTER WIN OR LOSE :)")
user_choice=input()

choice = ['rock', 'paper', 'scissors']

computer_choice = random.choice(choice)
print(computer_choice)
if user_choice==computer_choice:
    print("It is Draw")
elif (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="scissors" and computer_choice=="paper") or (user_choice=="paper" and computer_choice=="rock"):
    print("congratulations, You Win")
else:
    print("You lost :(")