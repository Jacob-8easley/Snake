from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food() 
score_board = ScoreBoard()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")

is_playing = True

while is_playing:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #detect food
    if snake.head.distance(food) < 15:
        score_board.increase_score()
        snake.extend_snake()
        food.random_num()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.game_over()
        score_board.update_highscore()
        is_playing = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.game_over()
            score_board.update_highscore()
            is_playing = False
screen.exitonclick()