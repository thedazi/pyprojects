#loops lesson
# fruits = ["apple", "peach", "cherry"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# for loops and range() function
# for number in range(1, 11, 3):
#     print(number)
# total = 0
# for number in range(1,101):
#     total += number
# print(total)
from contextlib import nullcontext
import random

print("Welcome to the PyPassword Generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letter_count = int(input("How many letters would you like in your password?\n"))
number_count = int(input("How your numbers would you like?\n"))
symbol_count = int(input("How many symbols would you like?\n"))

password = []
output_password = ""

for letter in range(1, letter_count + 1):
    password += random.choice(letters)    

for number in range(1,number_count +1):
    password += random.choice(numbers)

for symbol in range(1,symbol_count +1):
    password += random.choice(symbols)

random.shuffle(password)
for x in password:
    output_password += x

print(output_password)