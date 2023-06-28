from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('black')
        self.goto(x=-250,y=260)
        self.update_level()
        self.hideturtle()
        
    def update_level(self):
        self.write(f"Level: {self.level}",font=FONT)
    
    def next_level(self):
        self.level += 1
        self.clear()
        self.update_level()
    
    def game_over(self):
        self.clear()
        self.goto(x=0,y=0)
        self.write(f"Game over.\nLevel score = {self.level}", font=("Courier", 36, "normal"),align='center')
        self.penup()