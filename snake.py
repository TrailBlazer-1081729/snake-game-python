from turtle import Turtle,Screen
UP=90
DOWN=270
LEFT=180
RIGHT=0
POSITIONS=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.list=[]
        self.create_snake()
        self.head=self.list[0]
    def create_snake(self):
        for position in POSITIONS:
           self.add_snake(position)
    def move(self):
        for pos in range(len(self.list)-1, 0, -1):
            x_cor = self.list[pos - 1].xcor()
            y_cor = self.list[pos - 1].ycor()
            self.list[pos].goto(x_cor, y_cor)
        self.head.forward(20)
    def extend(self):
        self.add_snake(self.list[-1].position())
    def add_snake(self,position):
        pos = Turtle("square")
        pos.color("white")
        pos.penup()
        pos.goto(position)
        self.list.append(pos)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)


