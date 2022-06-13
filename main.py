import random

# options to pick from
options = ['Rock', 'Paper', 'Scissors']

# setting the choice for the computer
cpu_choice = random.choice(options)
running = True

# loop for game
while running:
    user_choice = input("enter your choice 'r, p, s'\n").lower()
    # resetting user_choice
    if user_choice =='r':
        user_choice = 'Rock'
    elif user_choice == 'p':
        user_choice = 'Paper'
    elif user_choice == 's':
        user_choice = 'Scissors'

    # cross checking options
    if user_choice in options:
        # determining the winner
        if user_choice == cpu_choice:
            print("It is a tie.")
        elif user_choice == 'Paper' and cpu_choice == 'Rock':
            print('{}'.format('You win\nPlayer('+ user_choice + ') : CPU('+ cpu_choice +')'))
            break
        elif user_choice == 'Rock' and cpu_choice == 'Scissors':
            print('{}'.format('You win\nPlayer('+ user_choice + ') : CPU('+ cpu_choice +')'))
            break
        elif user_choice == 'Scissors' and cpu_choice == 'Paper':
            print('{}'.format('You win\nPlayer('+ user_choice + ') : CPU('+ cpu_choice +')'))
            break
        else:
            print('{}'.format('You lose\nPlayer('+ user_choice + ') : CPU('+ cpu_choice +')'))
            break
    else:
        print("Invalid input")
