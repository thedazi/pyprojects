##########Scope#####

  #Local Scope

  # def drink_water():
  #   water_str = 2
  #   print(water_str)

  # drink_water()
  # print(water_str)

  #Global Scope
  # player_health = 10

  # def game():
  #   def drink_potion():
  #     potion_strength = 2
  #     print(player_health)

  #   drink_potion()

  # def game():
  #   game_level = 3
  #   enemies = ["Skeleton", "Zombie", "Alien"]
  #   if game_level < 5:
  #     new_enemy = enemies[0]
  # #Works because it becomes local
  #   print(new_enemy)

  # #does not work because the new_enemy variable is not global
  # print(new_enemy)

  ## Modifying Global Scope ##

  # enemies = 1

  # def increase_enemies():
  #   enemies = 2
  #   print(f"enemies inside function: {enemies}")

  # increase_enemies()
  # print(f"enemies inside function: {enemies}")

  #YOU CAN edit a global variable with a local variable by adding the 'global' command in from of the variables
  #good uses are for global constants

  #Global Constants 
  # PI = 3.14159
  # URL = "google.com"
  # twitch_handle = "dazthenord"

