print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    elif int(numCats) <= 0:
        print('Um, it is not possible to have a negative amount of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')
    
    
