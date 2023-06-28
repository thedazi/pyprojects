from turtle import Turtle, Screen, exitonclick
import random

screen = Screen()
screen.setup(width=500,height=480)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red",'orange','yellow','green','blue','purple']
y_positions = [-100,-60,-20,20,60,100]
all_turtles = []

for turtle_index in range(0,6):
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(colors[turtle_index])
  new_turtle.penup()
  new_turtle.goto(x=-230,y=y_positions[turtle_index])
  all_turtles.append(new_turtle)
  
if user_bet:
  race_start = True
  
while race_start:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      winning_turtle = turtle.pencolor()
      race_start = False
      if winning_turtle == user_bet:
        print(f"{user_bet} was correct!")
      else:
        print(f"Unfortunely, {winning_turtle} was the winner!")
      
    random_distance = random.randint(0,20)
    turtle.fd(random_distance)


screen = exitonclick()

