import random
import turtle

word_list = ["cow", "sheep", "goat", "fish",
             "chicken", "duck", "tiger"]



def user_guess():
    original_word = word_list[random.randint(0,6)]
    guess_count = 5
    word = original_word
    blank_word =("_ " * len(word))
    print(f"The word is {blank_word}")
 
    while guess_count > 0 and len(word) > 0:
        user_guess = input("Enter a letter!")
        value = word.find(user_guess)
        
        if value == -1:
            guess_count -= 1
            print(f"Wrong letter! Guess again! Guesses left = {guess_count}")
            
        else:
            word = word.replace(user_guess, "")
            print("That's right!")
            blank_word = blank_word.replace("_", user_guess, 1)
# problem here since method for replacing _ with a letter is still unknown
            print(blank_word)

            
    if guess_count == 0:
        print((f"Guesses left = 0. The word was {original_word}. Game Over!"))

        
    elif len(word) == 0:
        print(f"You have guessed the word {original_word}! You Win!")

        
print("Welcome to Hangman: Animal Edition! You have 5 guesses to deduce the animal!")            

user_guess()




    
    



