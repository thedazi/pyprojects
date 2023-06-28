from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.color('white')
    self.penup()
    self.x_move = 10
    self.y_move = 10

  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x,new_y)
  
  def bounce(self):
    self.y_move *= -1
    
  def change_direction(self):
    self.x_move *= -1
    
  def speed_up(self):
    if self.x_move > 0:
      self.x_move += 2
    else:
      self.x_move -= 2    
    
  def reset_speed(self):
    if self.x_move > 0:
      self.x_move = 10
    else:
      self.x_move =-10