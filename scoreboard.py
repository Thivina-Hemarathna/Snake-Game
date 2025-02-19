from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,350)
        self.write(f"Your score is: {self.score}",False,"center",font=('Arial', 24, 'normal'))

    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"Your score is: {self.score}", False, "center", font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!",False,"center",font=('Arial', 24, 'normal'))