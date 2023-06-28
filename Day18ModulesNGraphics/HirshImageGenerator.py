# from colorgram import extract
from turtle import Turtle,Screen, exitonclick
from random import choice
# colors = extract('Day18ModulesNGraphics\hirsh_imagine.jpg', 20)

# rgbcolor = []

# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r,g,b)
#   rgbcolor.append(new_color)

# print(rgbcolor)



missy = Turtle()
missy.penup()
missy.speed("fastest")
missy.hideturtle()
screen = Screen()
screen.colormode(255)
#start position (x500,y500 plane)

color_list = [(233, 233, 232), (231, 233, 237), (235, 231, 233), (224, 233, 227), (207, 160, 82), (54, 89, 130), (145, 91, 40), (140, 26, 49), (222, 206, 108), (132, 177, 203), (45, 55, 104), (158, 46, 83), (169, 160, 39), (129, 189, 143), (83, 20, 44), (38, 43, 67), (186, 94, 107), (186, 140, 170), (85, 120, 180), (59, 39, 31)]

x_start = -250
y_start = -250
x_dots = 10
y_dots = 10
missy.setposition(x_start,y_start)

def row_print():
  for _ in range(x_dots):
    missy.dot(20, choice(color_list))
    missy.fd(abs(2*x_start)/x_dots)

#new position
def column_adjust():
  missy.setheading(90)
  missy.fd(50)
  missy.setheading(180)
  missy.fd(500)
  missy.setheading(0)

 
for _ in range(y_dots):
  row_print()
  column_adjust()
  

screen = exitonclick()