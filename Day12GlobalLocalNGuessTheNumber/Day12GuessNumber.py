from Day12art import logo
import random
import os

# def find_number():  
#   random_number = random.choice(range(100))
#   return random_number

def difficulty():
  choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if choice == "easy":
    lives = 10
  else:
    lives = 5
  return lives

def guess(guess, rand_number):
  if guess == rand_number:
    return "win"
  elif guess > rand_number:
    return "Too high."
  else:
    return "Too low."
    
def play_guessthenumber():
  # random_number = find_number()
  print("I'm thinking of a number between 1 and 100.")
  random_number = random.randint(1,100)
  lives = difficulty()
  print(f"You have {lives} lives to start!")
  game_over = False

  while lives != 0 and game_over == False:
    user_guess = int(input("what is your guess?: "))
    print(f"You make a guess: {user_guess}")
    if guess(user_guess,random_number) == 'Too high.':
      print("Too high")
      lives -= 1
    elif guess(user_guess,random_number) == 'Too low.':
      print("Too low.")
      lives -= 1
    else:
      print(f"{user_guess} was correct! You win!")
      game_over = True

    print(f"You have {lives} attempts remaining to guess the number.")

    if lives != 0 and game_over == False:
      print("Try again.")
    else:
      print(f"Unfortunely, the number was {random_number}. Game over!")
      game_over = True
  
    
print(logo)  
while input("Would you like to play Guess the Number? y or n: ") == 'y':
  os.system("CLS")
  print(logo)
  play_guessthenumber()