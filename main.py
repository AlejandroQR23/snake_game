
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

# * Set up the screen
screen = Screen()
screen.setup( width=600, height=600 )
screen.bgcolor( "black" )
screen.title( "Snake Game" )
screen.tracer( 0 )

# * Create the snake, scoreboard and the food
snake      = Snake()
food       = Food()
scoreboard = Scoreboard()

# * Listen the snake controls
screen.listen()
screen.onkey( fun=snake.up, key="Up" )
screen.onkey( fun=snake.down, key="Down" )
screen.onkey( fun=snake.left, key="Left" )
screen.onkey( fun=snake.right, key="Right" )

# * Game flow
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep( 0.1 )
    snake.move()

    # Detect collision with food
    if snake.head.distance( food ) < 15:
        food.refresh()
        scoreboard.update()
        snake.extend( snake.segments[-1].position() )

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance( segment ) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick() 