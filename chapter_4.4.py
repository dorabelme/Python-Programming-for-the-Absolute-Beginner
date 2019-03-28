# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random


WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

word = random.choice(WORDS)
correct = word

print("There are", len(correct), "letters in the word.")

for i in range(5):
  tries_1 = input("Guess a letter: ")
  if tries_1 in correct:
   print("Yes")
  else:
   print("No")


final_guess = input("Now you have to guess the word! ")
if final_guess == correct:
  print("You got this!")
else:
  print("You failed here!")

