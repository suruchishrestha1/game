from turtle import *
from random import randrange
from freegames import square, vector

# Initialize game variables
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
game_over = False

# Change the snake's direction
def change(x, y):
    aim.x = x
    aim.y = y

# Check if the head of the snake is within the boundaries
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

# Display message on the screen
def display_message(message):
    pen = Turtle(visible=False)
    pen.up()
    pen.goto(0, 0)
    pen.color('red')
    pen.write(message, align="center", font=("Arial", 16, "bold"))

# Move the snake
def move():
    global game_over
    if game_over:
        return

    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        display_message("Game Over! Press 'R' to replay or 'Q' to quit.")
        game_over = True
        return

    snake.append(head)

    if head == food:
        print('Snake length:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Draw the snake
    for body in snake:
        square(body.x, body.y, 9, 'green')

    # Draw the food
    square(food.x, food.y, 9, 'red')

    update()
    ontimer(move, 100)

# Quit the game
def quit_game():
    print("Quitting the game. Goodbye!")
    bye()

# Replay the game
def replay_game():
    global snake, food, aim, game_over
    snake = [vector(10, 0)]
    food = vector(0, 0)
    aim = vector(0, -10)
    game_over = False
    clear()
    move()

# Set up the screen and controls
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')  # Move right
onkey(lambda: change(-10, 0), 'Left')  # Move left
onkey(lambda: change(0, 10), 'Up')  # Move up
onkey(lambda: change(0, -10), 'Down')  # Move down
onkey(replay_game, 'R')  # Replay the game
onkey(quit_game, 'Q')  # Quit the game

# Start the game
move()
done()