from turtle import Turtle

class Layout(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("square")
        self.color("blue")
        self.goto(-310, 310)
        self.crittt()




    def crittt(self):
            self.pensize(10)
            self.hideturtle()
            self.pendown()
            self.forward(620)
            self.right(90)
            self.forward(620)
            self.right(90)
            self.forward(620)
            self.right(90)
            self.forward(620)