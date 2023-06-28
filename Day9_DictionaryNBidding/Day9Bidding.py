# Bidding program
import os
from Day9art import logo
print(logo)
print("Welcome to the bidding simulator.\n")
bids_list = {}

def asking_bid():
    name = input("What is your name?\n")
    bids = int(input("How much would you like to bid?\n"))
    bids_list[name] = bids
    
#run
run = True
while run == True:
    asking_bid()
    other_bid = input("Is there anyother bidder? yes or no.\n").lower()
    if other_bid == "yes":
        _ = os.system('cls')
    elif other_bid == "no":
        for bid in bids_list:
            highest_bid = 0
            bidder = ""
            if bids_list[bid] > highest_bid:
                highest_bid = bids_list[bid]
                bidder = bid
        print(f"The highest bidder was {bidder} with a bid of ${highest_bid}!")
        end_run = input("Use again? yes or no.\n").lower()
        if end_run == "no":
            run = False
