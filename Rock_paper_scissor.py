# Rock Paper Scissors Game
import random
#if system chooses rock, if we chhoose paper we win 
#if system chooses paper, if we choose scissor we win
#if system chooses scissor, we choose rock we win
options=['rock','paper','scissor']
while True:
    system_choice=random.choice(options)
    user_choice=input("Enter rock, paper, or scissor (or 'q' to quit): ").strip().lower()
    if user_choice == 'q':
        print("Thanks for playing!")
        break
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue
    print(f"System chose: {system_choice}")
    if user_choice == system_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and system_choice == 'scissor') or (user_choice == 'paper' and system_choice == 'rock') or (user_choice == 'scissor' and system_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")