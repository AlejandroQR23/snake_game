
from turtle import Turtle
from random import randint

class Food( Turtle ):

    def __init__( self ):
        super().__init__()
        self.shape( "circle" )
        self.penup()
        self.color( "blue" )
        self.speed( "fastest" )
        self.refresh()

    def refresh( self ):
        self.goto( x=randint(-280, 280), y=randint(-280, 280) )