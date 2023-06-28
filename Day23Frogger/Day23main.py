import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# player turtle
player = Player()

# car manager
car_manager = CarManager()

# scoreboard
scoreboard = Scoreboard()

# controls
screen.listen()
screen.onkeypress(key='w',fun=player.up)
screen.onkeypress(key='s',fun=player.down)
screen.onkeypress(key='a',fun=player.left)
screen.onkeypress(key='d',fun=player.right)
screen.onkeypress(key='f',fun=scoreboard.game_over)

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    #car spawning
    car_manager.create_car()
    car_manager.move_cars()
    #collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    #next level
    if player.finish_level() == True:
        player.set_to_start()
        scoreboard.next_level()
        car_manager.increase_speed()

screen.exitonclick()