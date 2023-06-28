from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial",22,"normal")



class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    with open("Day20-21SnakeGame.py\highscore.txt") as data:
      self.high_score = int(data.read())
    self.penup()
    self.color('white')
    self.goto(x=0,y=270)
    self.update_scoreboard()
    self.hideturtle()

  def update_scoreboard(self):
    self.clear()
    self.write(f'Score: {self.score}   High Score: {self.high_score}', align=ALIGNMENT,font=FONT)
    
  def reset_score(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("Day20-21SnakeGame.py\highscore.txt", mode="w") as data:
        data.write(str(self.high_score))
    self.score = 0
    self.update_scoreboard()
    
  
  def increase_score(self):
    self.score += 1
    self.update_scoreboard()
    #needs to continuously rewrite
  
    