import random
#random module
#import xxx common imports from xxx library
#modules are created by importing files, even your own, for example Day4_module
#import Day4module

#print(Day4_module.pi)
#which will print 3.14 from the other file


# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float * 5)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# # lists are a combination of items within []. ex) [item1, item2]
# fruits = ["apple", "cherry", "pear"]
# print(fruits[0])
# #should extract apple
# print(fruits[-1])
# #should print pear, because negatives start from the end of the code
# fruits[1] = "red berry"
# should change cherry to red berry 

# https://docs.python.org/3/tutorial/datastructures.html
# #list commands
# nested lists are lists within lists
# list1 = ["thing"]
# list2 = ["another thing"]
# nested_list = [list1, list2]
# print(nested_list)

# ***** CTRL + / will mass comment all highlights lines

print("Welcome to Rock, Paper, Scissors")
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer = random.randint(0,2)
rock ="""                 _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
"""
paper = """
     _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|   
"""
scissors = """
  _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
"""    
game_images = [rock, paper, scissors]

if player == computer:
    print(f"Player:{game_images[player]}\nComputer:{game_images[computer]}\nIts a draw")
elif player == 0 and computer == 1:
    print(f"Player:{game_images[player]}\nComputer:{game_images[computer]}\nPaper beats rock. Computer wins.")
elif player == 0 and computer == 2:
    print(f"Player:{game_images[player]}\nComputer:{game_images[computer]}\nRock beats scissors. Computer wins.")
elif player == 1 and computer == 0:
    print(f"Player:{game_images[player]}\nComputer:{game_images[computer]}\nPaper beats rock. Player wins.")
elif player == 1 and computer == 2:
    print(f"Player:{game_images[player]}\nComputer:{game_images[computer]}\nScissors beats paper. Computer wins.")
elif player == 2 and computer == 0:
    print(f"Player:{game_images[player]}\nComputer:{game_images[computer]}\nRock beats scissors. Player wins.")
elif player == 2 and computer == 1:
    print(f"Player:{game_images[player]}\nComputer:{game_images[computer]}\nScissors beats paper. Player wins.")
else:
    print("wtf..")