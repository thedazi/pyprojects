# dictionaries are a combo of keys and values
# the dictionary syntax is {"key":value}
1


# programming_dicitonary = {
#     "Bug": "An error in a program that precents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again.",
# }
# retriving items from dictionaries
# print(programming_dicitonary["Bug"])

# adding new items to dictionary
# programming_dicitonary["Dictionary"] = "Not a list"
# print([programming_dicitonary])

##creating an empty dictionary
# empty_dictionary = {}

##wipe an existing dictioanry
# programming_dicitonary = {}
# print(programming_dicitonary)

# #edit an item in a dictionary
# programming_dicitonary["Bug"] = "a moth in your computer."
# print(programming_dicitonary)

#loop through a dictionary
# for thing in programming_dicitonary:
    # print(thing)
    #this will print the key
    # print(programming_dicitonary[thing])
    #this will print the values

#### Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",

}

#Nesting a List in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Little", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 7},

}

#nesting Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Little", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 7
    },
]

