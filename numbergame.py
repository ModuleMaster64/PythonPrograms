number = 64

print ('In this program you will need to guess the number I am thinking of')

print ('I am thinking of a number between 1 and 100')

while number == 64:

    guess = input()

    guess = int(guess)

    if guess < 64:
        print ('your guess is too low')


    if guess > 64:
        print ('your guess is too high')

    if guess == 64:
        print('your guess is correct')

        break