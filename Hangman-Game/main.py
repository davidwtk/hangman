import random
import hangman_art
import hangman_words


word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
stages = hangman_art.stages

print(hangman_art.logo)
print("\nYou have 6 lives!")

display = []
for _ in range(word_length):
    display.append("_")

while display.count("_") > 0:
  if lives == 0:
    print("You lose.")
    break
  
  guess = input("Guess a letter: ").lower()
  letter_guessed = False
  if guess in display:
    print(f"{guess} has already been entered, try another letter")
    letter_guessed = True
  for position in range(word_length):
    letter = chosen_word[position]       
    if letter == guess:
      display[position] = letter
      letter_guessed = True
      
  if letter_guessed == False:
    lives -= 1
  if guess not in chosen_word:
    print(f"{guess} is not in the word! Try again!")
 

  calculated_lives = -(7 - lives)
  print(stages[calculated_lives])
  
  print(f"{' '.join(display)}")
  
  if lives == 0:
    print("You lose.")
    print(f"The word is {chosen_word}.")
    break
if display.count("_") < 0 and lives > 0:
  print("You win")

    