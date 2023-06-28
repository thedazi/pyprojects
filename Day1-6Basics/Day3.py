#if-else conditionals
#print("Welcome to the rollercoaster!")
#height = int(input("How tall are you in cm? "))
#if height > 120:
#    print("you are tall enough!")
#else:
#    print("Come back when you are taller")
# lastly, '=' is for variables and '==' is for equals with conditionals
#nested if/else statement = if/else statement inside an if/else statement
#elif = else if is for additional conditions past the first if and else (for 3 or more conditionals)
#multiple if statments will check all of the if conditionals
#logical operators for if statements = "and", "or", and "not" (all are self explanatory)
#count(x), counts the number of x in something, xxxx.upper() and xxxx.lower() make a string all uppercase or lowercase
#https://ascii.co.uk/art funny pictures
print('''
           _.====.._
         ,:._       ~-_
             `\        ~-_
               | _  _  |  `.
             ,/ /_)/ | |    ~-_
    -..__..-''  \_ \_\ `_      ~~--..__...----...
''')
print("Your boat is hit by a wave and you are washed up on an island.")
choice_1 = input("In front of you is a shovel and firemaking tools. Do you dig or start a fire? ")
choice_1.lower()

if choice_1 == 'dig':
    choice_2 = input("You dig into the sand and find a chest and a ring. Do you wear the ring or open the chest? ")
    choice_2.lower()
    if choice_2 == 'wear the ring':
        print("A beautiful pig appears and tell you to pick the number one, two, or three.")
        choice_3 = input("Which do you pick? ")
        choice_3.lower()
        if choice_3 == "one":
            print("The pig says, 'that's my favorite number!' And you are forced to marry the pig.")
        elif choice_3 == "two":
            print("The pig casts a spell and sends you home. Good job!")
        else:
            print("The pig didn't like that answer, and ate you.")
    else:
        print("The chest eats you. Game over.")
else:
    print("From the fire or noise you've made, you were discovered by maneating boars. Game over.")