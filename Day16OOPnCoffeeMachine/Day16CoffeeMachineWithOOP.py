import Day16coffee_maker
import Day16money_machine
import Day16menu

coffeemenu = Day16menu.Menu()
coffeemaker = Day16coffee_maker.CoffeeMaker()
moneymachine = Day16money_machine.MoneyMachine()

is_on = True

while is_on:
  all_items = coffeemenu.get_items()
  startup = input(f"Welcome to the coffee machine. Please pick between {all_items}: ")

  if startup == "report":
    coffeemaker.report()

  elif startup == "off":
    is_on = False

  else:
    order = coffeemenu.find_drink(startup)
    resource_check = coffeemaker.is_resource_sufficient(order)
    if resource_check == True:
      ## IMPORT for calling on specific attributes in objects!!!!
      pay = moneymachine.make_payment(order.cost)
#                                   ^^^^^^^^^^^^^
      if pay == True:
        coffeemaker.make_coffee(order)


