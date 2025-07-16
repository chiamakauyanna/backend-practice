# Import random module  'import random'
#   generate secret number 'random.randint(1, 10)'
#     get users guess
#       match the guess using match case
#         if guess is correct, display 'Congratulations, you guessed it!'
#         if guess is too high 'Oops, your guess is a bit high. Try again!'
#         if guess is too low 'Nope, your guess is a bit low. Give it another shot!'
# play game again using user input

import random

print("Let's play a guessing game and see if you can guess the secret number.")
secret_number = random.randint(1, 10)
guess = int(input('guess a number from 1 - 10: '))

match guess:
  case guess if guess == secret_number:
    print('Congratulations, you guessed it!')
  case guess if guess > secret_number:
    print('Oops, your guess is a bit high. Try again!')
  case guess if guess < secret_number:
    print('Nope, your guess is a bit low. Give it another shot!')
  case _:
      print('Make a guess')

print()
play_again = input('Would you like to play again? (yes / no) ')
if play_again == 'yes': 
  guess = int(input('guess a number from 1 - 10: ')) 
else:
  print('Game over!')
  
