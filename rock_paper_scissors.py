import random

name = input('What is your name?: ')
print('Hi, ', name, ", nice to meet you!")
answer = input('Do you want to play rock, paper, scissors? (yes/no): ').lower()
if answer == "yes":
    print('Yayy, let\'s play!!!')
elif answer == "no":
    print('Okay, maybe next time...')
    exit()
else:
    print('Invalid answer')
    exit()

options = ["rock", "paper", "scissors"]
player = input('Choose: rock, paper or scissors: ').lower()

computer = random.choice(options)

print("I chose: ", computer)

if player == computer:
    print('It\'s a tie.')
elif player == "rock" and computer == "scissors":
    print('You won!')
elif player == "scissors" and computer == "paper":
    print('You won!')
elif player == "paper" and computer == "rock":
    print('You won!')
else:
    print("You lost...")
