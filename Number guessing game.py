'''Random number guessing game'''
from random import randint

lower = 0
upper = 100
chosen = randint(lower, upper)
tries = 0
guess = -1

print("Number guessing game.")

while guess != chosen:
    tries += 1
    print()
    print("Range is %d to %d. Try number %d." % (lower, upper, tries))
    guess = input("Enter your guess: ")
    if str(guess).isdigit():
        guess = int(guess)
        if guess == chosen:
            print("Bingo! The number is %d. You got it in %d tries!" % (chosen, tries))
        elif guess > chosen:
            print("Lower please!")
            upper = guess
        elif guess < chosen:
            print("Higher please!")
            lower = guess
        else:
            print("This case shouldn't happen at all.....")
    else:
        print("Please enter a positive number between %d and %d. (You have been penalised with 1 try.)" % (lower, upper))
