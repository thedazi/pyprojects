import Day14art
from Day14game_data import data
import random
import os

used_celebs = []
option_a = ''
option_b = ''

def choose_person():
  '''Randomly outputs a unqiue person and stores used names in the used celebs list'''
  choice = data[random.choice(range(len(data)))]
  while choice in used_celebs:
    choice = data[random.choice(range(len(data)))]
  used_celebs.append(choice)
  return choice

###Good compare input example!! 

def compare(guess, a_followers,b_followers):
  '''Compares the user input to the follower counts and returns the score'''
  if a_followers > b_followers:
    return guess == 'a'
  elif b_followers > a_followers:
    return guess == 'b'


def HigherOrLower():

  score = 0
  option_a = choose_person()
  option_b = choose_person()
  game_over = False
  while game_over == False:

#for testing
    # print(option_a['follower_count'])
    # print(option_b['follower_count'])
    
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(Day14art.vs)
    print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}\n")

    ##user input
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    answer = compare(user_guess, option_a['follower_count'], option_b['follower_count'])
    if answer == False:
      print(f"Game over! Your score was {score}!")
      game_over = True
    else:
      score += 1
      os.system("CLS")
      print(Day14art.logo)
      print(f"Correct! Your score is now {score}\n\n")
      if option_b['follower_count'] > option_a['follower_count']:
        option_a = option_b
      option_b = choose_person()


  

while input("Do you want to play Higher or Lower? Type 'y' or 'n': ").lower() == 'y':
  os.system("CLS")
  used_celebs = []
  print(Day14art.logo)
  HigherOrLower()
