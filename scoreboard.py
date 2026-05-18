from turtle import Turtle
FONT=("Arial" , 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0, 270)
        self.color("white")

        self.write(f"score: {self.score}",align="center",font=FONT)
        self.hideturtle()
        self.penup()


    def increase(self):

        self.score+=1
        self.clear()
        self.write(f"score: {self.score}",align="center",font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)