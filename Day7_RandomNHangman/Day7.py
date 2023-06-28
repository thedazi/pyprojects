#Hangman
#Step 1 
import random
import Day7words
import Day7art

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO-4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


#TODO-5: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


#TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

#TODO-7: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 
# 'display' has no more blanks ("_"). Then you can tell the user they've won.

#TODO-8: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#TODO-9: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

#TODO-10: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

chosen_word = random.choice(Day7words.word_list)
stages = Day7art.stages
print(f"Here is a hint {chosen_word}")
display = []
for letter in chosen_word:
    display.append("_")
#display
print(Day7art.logo)
print(display)
print(stages[6])
#variables
lives = 6
wrong_guess = []
end_game = False
while not end_game:
    guess = input("Guess a letter\n").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == chosen_word[position]:
            display[position] = letter
#losing lives
    if guess not in chosen_word:
        lives -= len(guess)
        wrong_guess += guess
        if lives == 0:
            end_game = True
            print("You lose")
#errors
    if guess in display:
        print(f"You have already guessed {guess}. Try again.")


    print(f"{' '.join(display)}")
    print(stages[lives])
    print(f"Incorrect letters: {wrong_guess}")        
    if "_" not in display:
        end_game = True
        print("You win!")

if end_game == True:
    try_again = input("Do you want to play again? Yes or No.\n")
    if try_again == "yes":
        chosen_word = random.choice(Day7words.word_list)
        end_again = False
        lives = 1
        lives =+ 5
        print(Day7art.logo)
        print(display)
        print(stages[6])