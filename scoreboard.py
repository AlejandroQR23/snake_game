
from turtle import Turtle

FONT = ("Courier", 18, "normal")

class Scoreboard( Turtle ):

    def __init__( self ):
        super().__init__()

        self.score = 0
        self.get_highscore()
        
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
            self.set_highscore()
        self.score = 0
        self.update()

    def get_highscore( self ):
        with open( "data.txt" ) as file:
            self.high_score = int( file.read() )

    def set_highscore( self ):
        with open( "data.txt", mode="w" ) as file:
            file.write( str( self.high_score ) )

