from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial",16,"normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.P1score = 0
    self.P2score = 0
    self.penup()
    self.color('white')
    self.goto(x=0,y=260)
    self.update_scoreboard()
    self.hideturtle()
    
  def update_scoreboard(self):
    self.write(f"{self.P1score}               {self.P2score}", align=ALIGNMENT, font=FONT)
  
  def P1_point(self):
    self.P1score += 1
    self.clear()
    self.update_scoreboard()

  def P2_point(self):
    self.P2score += 1
    self.clear()
    self.update_scoreboard() 