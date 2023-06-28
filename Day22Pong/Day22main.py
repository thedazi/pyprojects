from time import sleep
from turtle import Screen
from paddle import Paddle
from ball import Ball 
from scoreboard import Scoreboard

P1_POSITION = -360
P2_POSITION = 360



##Pong Structure

# Screen
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)



# Paddles
P1_paddle = Paddle(P1_POSITION)
P2_paddle = Paddle(P2_POSITION)

# ball
ball = Ball()
# Scoreboard
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(key='w',fun=P1_paddle.up)
screen.onkeypress(key='s',fun=P1_paddle.down)
screen.onkeypress(key='Up',fun=P2_paddle.up)
screen.onkeypress(key='Down',fun=P2_paddle.down)

game_on = True

while game_on:
  sleep(0.05)
  screen.update()
  ball.move()
  #wall collide
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce()
  elif ball.xcor() > 380 or ball.xcor() < -380:
    ball.change_direction()
    if ball.xcor() > 380:
      scoreboard.P2_point()
      ball.reset_speed()
    elif ball.xcor() < -380:
      scoreboard.P1_point()
      ball.reset_speed()
  #paddle collide
  if ball.distance(P1_paddle) < 50 and ball.xcor() < -330 or ball.distance(P2_paddle) < 50 and ball.xcor() > 330:
    ball.change_direction()
    ball.speed_up()
  
  #paddle wall
  if P1_paddle.ycor() > 240:
    P1_paddle.down()
  if P1_paddle.ycor() < -240:
    P1_paddle.up()
  if P2_paddle.ycor() > 240:
    P2_paddle.down()
  if P2_paddle.ycor() < -240:
    P2_paddle.up()
    
  


screen.exitonclick()