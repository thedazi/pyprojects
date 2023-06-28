from turtle import Turtle

starting_position = [(0,0),(-20,0),(-40,0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
  def __init__(self):
    self.segments = []
    self.start_snake()
    self.snakehead = self.segments[0]
    
  def start_snake(self):
    for position in starting_position:
      self.add_segment(position)
  
  def add_segment(self, position):
    snake_segment = Turtle(shape="square")
    snake_segment.color('white')
    snake_segment.penup()
    snake_segment.goto(position)
    self.segments.append(snake_segment)
      
  def extend(self):
    self.add_segment(self.segments[-1].position())
    
  def reset_snake(self):
    for seg in self.segments:
      seg.goto(1000,1000)
    self.segments.clear()
    self.start_snake()
    self.snakehead = self.segments[0]
      
  def move(self):
    for seg_num in range(len(self.segments)-1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x,new_y)
    self.segments[0].fd(move_distance)
  
  def up(self):
    if self.snakehead.heading() != DOWN:
      self.snakehead.setheading(UP)

  def down(self):
    if self.snakehead.heading() != UP:
      self.snakehead.setheading(DOWN)

  def left(self):
    if self.snakehead.heading() != RIGHT:
      self.snakehead.setheading(LEFT)

  def right(self):
    if self.snakehead.heading() != LEFT:
      self.snakehead.setheading(RIGHT)


    