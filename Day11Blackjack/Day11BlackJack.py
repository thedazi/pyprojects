from Day11art import logo
import random
import os

############### Blackjack Project #####################

#draw a card
def draw_card(target):
    """return a random card"""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return target.append(random.choice(deck))

#scores
def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)     
    return sum(cards)

#compare scores
def compare(player, comp):
    if player > 21 and comp > 21:
        return "You went over. You lose"
    elif player == comp:
        return "draw"
    elif comp == 0:
        return "Computer wins with a Blackjack"
    elif player == 0:
        return "Player wins with a Blackjack" 
    elif player > 21:
        return "You went over, so the Computer wins"   
    elif comp > 21:
        return "Computer went over, so you player wins"
    elif comp > player:
        return f"Computer wins with a score of {comp}"
    elif player > comp:
        return f"Player win with a score of {player}"
    else:
        return "You lose"

def play_game():
    #hand set up
    player_hand = []
    computer_hand = []

    game_over= False

    #drawing cards 
    for x in range(2):
        draw_card(player_hand)
        draw_card(computer_hand)

    while not game_over:
        player_score = calc_score(player_hand)
        computer_score = calc_score(computer_hand)
        print(f"    Your cards:{player_hand}, current score: {player_score}")
        print(f"    Computer's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            draw_stand = input("Type 'd' to draw another card, or type 's' to stand: ")
            if draw_stand == 'd':
                draw_card(player_hand)
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        draw_card(computer_hand)
        computer_score = calc_score(computer_hand)

    print(f"Your final cards:{player_hand}, final score: {player_score}")
    print(f"Computer final cards:{computer_hand}, Computer final score: {computer_score}")
    print(compare(player_score, computer_score))
 

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':

    os.system("CLS")
    print(logo)
    play_game()