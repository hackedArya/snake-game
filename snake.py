
from turtle import Turtle
STARTING_POSTION = [(0 , 0), (-20 , 0), (-40 , 0)]
MOVE_DIS = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segment = []
        self.creat_snake()
        self.head = self.segment[0]
        
    def creat_snake(self):
        for postion in STARTING_POSTION:
            self.add_segment(postion)
            
    def add_segment(self, postion):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(postion)
        self.segment.append(new_segment)


    def extend(self):
        self.add_segment(self.segment[-1].position())

        
    def move(self):
        for seg_num in range(len(self.segment) -1, 0 , -1):
            new_x = self.segment[seg_num -1].xcor()
            new_y = self.segment[seg_num -1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DIS)   

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)     

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)     

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)     

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)     
    
