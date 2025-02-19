from turtle import Turtle
SEGMENT_START=[(0, 0), (-20, 0), (-40, 0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segments=[]
        self.createSnake()
        self.head=self.segments[0]

    def createSnake(self):
        for pos in SEGMENT_START:
            new_segment = Turtle("square")
            new_segment.speed("fastest")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.speed("fastest")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto( self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)


    def move(self):
        for segment in range(len(self.segments)-1,0,-1):
            x = self.segments[segment-1].xcor()
            y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x,y)
        self.segments[0].forward(20)

    def go_up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)