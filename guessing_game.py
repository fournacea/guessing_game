# Print "guess a number between 1 and 5"
# while loop -> while rand_num != 5: continue asking for input
# If guess is correct break from loop and print "you won!. It took you {i} many tries"


import random 

i = 0
random_num = random.randint(1, 5)

while True:
    guess = int(input("Guess a number between 1 and 5: "))
    i += 1
    if guess == random_num:
        print(f"You guessed correct! {guess} was the number. It took you {i} tries.")
        break