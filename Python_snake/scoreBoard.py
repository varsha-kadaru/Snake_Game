from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.display_score()
        self.hideturtle()
    
    def display_score(self):
        self.write(f"Score : {self.score}",align="center",font=("Arial",24,"normal"))
        

    def cal_score(self):
        self.score+=10
        self.clear()
        self.display_score()

    def gameover(self):
        self.goto(0,0)
        #self.clear()
        self.write(f"GameOver",align="center",font=("Arial",24,"normal"))
        