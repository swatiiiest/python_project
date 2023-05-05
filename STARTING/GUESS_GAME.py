import random
level = input('which level you want to play. Easy or Hard?').lower()
number = random.randint(1,100)
game_on = True
easy_guess = 10
hard_guess = 5
while game_on:

    guess = int(input('Make a guess'))

    if level == 'easy':
        print(f'You have total of {easy_guess} attempts to guess')
        print(f'you have only {easy_guess} attempts left.')

        if easy_guess == 0:
            game_on = False
            print('you have no more attempts to guess.')
        if guess > number:
            print(f'Guess is too high.\nGuess again')
            easy_guess-=1
        elif guess < number:
            print(f'Guess is too low.\nGuess again')
            easy_guess-= 1
        elif guess == number:
            print('You guessed right.')
            game_on = False



