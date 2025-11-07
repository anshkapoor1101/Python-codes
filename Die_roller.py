import random
counter = 0
while True:
    Num= int(input("Enter number of dice to roll: "))
    for i in range(Num):
        die_roll = random.randint(1, 6)
        print(f"Die {i+1}: {die_roll}")
        counter += 1
    print(f"Total rolls: {counter}")
    choice=input("Do you still want to play? (y/n): ").strip().lower()
    if choice == 'n':
        print("Thanks for playing!")
        break