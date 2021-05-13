
from turtle import Turtle

class Snake:

    MOVE_DISTANCE = 20

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake( self ):
        xcor = 0
        for i in range( 3 ):
            position = ( xcor, 0 )
            self.extend( position )
            xcor -= 20

    def extend( self, position ):
        segment = Turtle( shape="square" )
        segment.color("white")
        segment.penup()
        segment.goto( position )

        self.segments.append( segment )

    def move( self ):
        for i in range( len( self.segments )-1, 0, -1 ):
            x = self.segments[ i - 1 ].xcor()
            y = self.segments[ i - 1 ].ycor()
            self.segments[i].goto( x, y )
        self.head.forward( self.MOVE_DISTANCE )

    def reset( self ):
        for segment in self.segments:
            segment.goto( 1000, 1000 )
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # * Snake movements
    def up( self ):
        if self.head.heading() != 270:
            self.head.setheading( 90 )
    
    def down( self ):
        if self.head.heading() != 90:
            self.head.setheading( 270 )

    def left( self ):
        if self.head.heading() != 0:
            self.head.setheading( 180 )

    def right( self ):
        if self.head.heading() != 180:
            self.head.setheading( 0 )
