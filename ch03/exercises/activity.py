import random

num = random.randrange(1, 11)
num_guesses = 0
number_guessed = False

for i in range(3):
  if number_guessed:
    break
    print("break")
  guess_num = int(float(input("Please enter a guess: ")))
  num_guesses +=1
  if guess_num > num:
    print("Your guess is too high.")
  elif guess_num < num:
    print("Your guess is too low.")
  else:
    number_guessed = True
    print("Correct!")
if number_guessed:
  print("it took you ", num_guesses, " to guess correctly!")
else:
  print("You didn't get it in three tries!")