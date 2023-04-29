from turtle import Screen,Turtle
from snakeCreate import Snake
from food import Food
from scoreBoard import ScoreBoard

import time

screen=Screen()
screen.setup(width=600,height=600)

screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


#create snake body


# segment_1=Turtle("square")
# segment_1.color("white")
# segment_2=Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20,0)
# segment_3=Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40,0)

end_of_game=False

#move snake
while end_of_game==False:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.cal_score()

    #detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor() < -290 or snake.head.ycor()>290 or snake.head.ycor() <-290:
        end_of_game=True
        scoreboard.gameover()

    #detect collison with tail
    for seg in snake.segments:
        if snake.head.distance(seg)<10 and seg !=snake.head:
            end_of_game=True
            scoreboard.gameover()

        






screen.exitonclick()