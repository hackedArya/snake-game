
import time
from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import ScoreBoard
 

screen = Screen()
screen.setup(width=600 , height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My snake game")

snake = Snake()
food = Food()
screen.listen()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 289 or snake.head.xcor() < -289  or snake.head.ycor() > 289 or snake.head.ycor() < - 289:
        is_game_on = False
        scoreboard.game_over()   

    for segment in snake.segment[1:]:
        
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()    

    







screen.exitonclick()