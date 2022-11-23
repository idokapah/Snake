from turtle import Turtle
MOVE_DISTANCE=20

class Snake:

    def __init__ (self):
        self.snake_body = []
        self.create_snake()
        self.head=self.snake_body[0]
        self.score=0

    def create_snake(self):
        for j in range(3):
            timi = Turtle("square")
            timi.color("white")
            timi.penup()
            timi.goto((-20 * j), 0)
            self.snake_body.append(timi)

    def extend(self):
        timi = Turtle("square")
        timi.color("white")
        timi.penup()
        timi.goto(self.snake_body[-1].position())
        self.snake_body.append(timi)


    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
         self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
           self.head.setheading(270)

    def move(self):
        for s in range(len(self.snake_body) - 1, 0, -1):
            x_cor = self.snake_body[s - 1].xcor()
            y_cor = self.snake_body[s - 1].ycor()
            self.snake_body[s].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)



