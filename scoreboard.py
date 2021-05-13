
from turtle import Turtle

FONT = ("Courier", 18, "normal")

class Scoreboard( Turtle ):

    def __init__( self ):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color( "white" )
        self.hideturtle()
        self.penup()
        self.goto( x=0, y=270 )
        self.update()

    def increase_score( self ):
        self.score += 1
        self.update()

    def update( self ):
        self.clear()
        self.write( arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=FONT )

    def reset( self ):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()
