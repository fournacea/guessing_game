import random 

i = 0
random_num = random.randint(1, 5)

while True:
    guess = int(input("Guess a number between 1 and 5: "))
    i += 1
    if guess < random_num:
        print("Too low!")
    elif guess > random_num:
        print("Too high!")
    else:
        print(f"You guessed correct! {guess} was the number. It took you {i} tries.")
        play_again = input("Do you want to play again? (y/n)").lower()

        if play_again == "y":
            random_num = random.randint(1, 5)
            guess = None
            i = 0
        else:
            break