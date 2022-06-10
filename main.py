import random

# options to pick from
options = ['r', 'p', 's']

# setting the choice for the computer
cpu_choice = random.choice(options)

running = True

while running:
    user_choice = input("enter your choice 'r, p, s'\n").lower()
    if user_choice in options:
        if user_choice == cpu_choice:
            print("It is a tie, computer choice was " + cpu_choice)
        elif user_choice == 'p' and cpu_choice == 'r':
            print("You win, computer choice was " + cpu_choice)
            break
        elif user_choice == 'r' and cpu_choice == "s":
            print("You win, computer choice was " + cpu_choice)
            break
        elif user_choice == 's' and cpu_choice == "p":
            print("You win, computer choice was " + cpu_choice)
            break
        else:
            print("You lose, computer choice was " + cpu_choice) 
            break
    else:
        print("Invalid input")
