
from turtle import Turtle

FONT = ("Courier", 18, "normal")

class Scoreboard( Turtle ):

    def __init__( self ):
        super().__init__()
        self.score = 0
        self.color( "white" )
        self.hideturtle()
        self.penup()
        self.goto( x=0, y=270 )
        self.write( arg=f"Score: {self.score}", align="center", font=FONT )

    def update( self ):
        self.score += 1
        self.clear()
        self.write( arg=f"Score: {self.score}", align="center", font=FONT )
    
    def game_over( self ):
        self.home()
        self.write( arg="Game Over", align="center", font=FONT )
