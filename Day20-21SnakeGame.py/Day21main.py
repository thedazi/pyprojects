from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
from time import sleep

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

missy = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(missy.up, "Up")
screen.onkey(missy.down, "Down")
screen.onkey(missy.left, "Left")
screen.onkey(missy.right, "Right")

game_run = True

while game_run:
  screen.update()
  sleep(0.05)
  missy.move()

## collision detection
  if missy.snakehead.distance(food) < 15:
    food.refresh()
    scoreboard.increase_score()
    missy.extend()

#Detect wall collision
  if missy.snakehead.xcor() > 290 or missy.snakehead.xcor() < -290 or missy.snakehead.ycor() > 290 or missy.snakehead.ycor() < -290:
    scoreboard.reset_score()
    missy.reset_snake()
    
#Dectent tail collision
  for segment in missy.segments[1:]:
    # if segment == missy.snakehead:
    #   pass
    #useful appliciation for pass
    if missy.snakehead.distance(segment) < 10:
      scoreboard.reset_score()
      missy.reset_snake()
    
screen.exitonclick()
