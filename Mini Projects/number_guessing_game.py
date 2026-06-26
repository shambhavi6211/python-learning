import random

secret = random.randint(1, 10)

guess = 0  
while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret:
        print("Too low , try again!")

    elif guess > secret:
        print("Too high , try again!")

    else:
        print("Correct! You guessed it.")