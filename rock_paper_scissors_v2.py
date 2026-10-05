import random
import sys
import time

options = ["rock", "paper", "scissors"]
answer = (input("Do you want to play rock, paper, scissors? (yes/no): "))
answer = answer.lower()

if (answer == 'no'):
    print("Okay, ending the program...")
    sys.exit()

elif (answer == 'yes'):
    while(answer=='yes'):
        player_choice = (input('Choose an option (rock/paper/scissors): '))
        player_choice = player_choice.lower()
    
        print('*'*10)
        print('ROCK')
        time.sleep(1)
        print('PAPER')
        time.sleep(1)
        print('SCISSORS!')
        time.sleep(1)
        print('*'*10)
    
        computer_choice = random.choice(options)
        print(f'Your choice: {player_choice} \nMy choice: {computer_choice}')
    
        if (computer_choice == player_choice):
            print("It's a draw!")

        elif ((computer_choice == 'rock') and (player_choice == 'scissors')):
            print('I won!')
    
        elif ((computer_choice == 'scissors') and (player_choice == 'paper')):
            print('I won!')
        
        elif ((computer_choice == 'paper') and (player_choice == 'rock')):
            print('I won!')
        
        else:
            print('You win!')
            
        answer2 = (input('Do you want to play again? (yes/no): '))
        answer2 = answer2.lower()
        
        if (answer2 == 'yes'):
            answer = answer2
        else:
            print('Okay, ending the program', end='', flush=True)
            for x in range(3):
                time.sleep(1)
                print(".", end="", flush=True)
            sys.exit()
else:
    print('Invalid answer.')
