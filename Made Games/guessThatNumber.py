import random
print('Guess 4 numbers between 1 and 10')
pGuesses1 = input('Enter your first guess:')
pGuesses2 = input('Enter your second guess:')
pGuesses3 = input('Enter your third guess:')
pGuesses4 = input('Enter your fourth guess:')

pg1 = float(pGuesses1)
pg2 = float(pGuesses2)
pg3 = float(pGuesses3)
pg4 = float(pGuesses4)

player_guesses = [pg1, pg2, pg3, pg4]
correct = random.randint(1,10)
if any(x == correct for x in player_guesses):
	print('You Win! The correct answer was %s' % correct) 
else:
	print('Boom! You lose the correct answer was %s' % correct)
