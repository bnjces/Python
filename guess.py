# This is a guess the number game. 3/2/2023 - Udemy Python


import random  #import random module for using randint
print('Hey! What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between one and twenty.')
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess.

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
    
    
    

print('You took ' + str(guessesTaken) + ' guesses.')

