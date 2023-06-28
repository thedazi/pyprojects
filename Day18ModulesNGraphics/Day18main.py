from tkinter.simpledialog import SimpleDialog
from turtle import Turtle, Screen, exitonclick
from random import randint, choice
# can also import * to import all variables
# import as {variable} can change the keyword for the import

missy = Turtle()
missy.shape('turtle')
missy.color('pink')
screen = Screen()
screen.colormode(255)

def random_colors():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  colors = (r, g, b)
  return colors

direction = [0,90,180,270]
missy.pensize(1)
# square
# missy.fd(100)
# missy.left(90)
# missy.fd(100)
# missy.left(90)
# missy.fd(100)
# missy.left(90)
# missy.fd(100)

# dashed line
# for _ in range(300):
#     missy.pendown()
#     missy.fd(10)
#     missy.penup()
#     missy.fd(10)


# shape diagram
# sides = 3
# while sides < 20:
#     for _ in range(sides):
#         missy.fd(40)
#         missy.right(360/sides)
#     sides += 1
#     missy.color(choice(colors))

# ##random walk
# for _ in range(200):
#   missy.fd(30)
#   missy.setheading(choice(direction))
#   missy.pencolor(random_colors())

#Spirograph
missy.speed("fastest")
num_of_circ = 100

for _ in range(num_of_circ):
  missy.color(random_colors())
  missy.circle(120)
  missy.left(360/num_of_circ)
  


#screen setup
screen.colormode(255)
screen = exitonclick()
