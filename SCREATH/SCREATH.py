from turtle import Turtle, Screen


tim = Turtle()
my_screen = Screen()

def move_forward():
    return tim.forward(10)

def move_back():
    return tim.backward(10)

def turn_right():
    return tim.right(10)

def turn_left():
    return tim.left(10)


def clear():
    return tim.reset()

my_screen.listen()
my_screen.onkey(key='w', fun=move_forward)
my_screen.onkey(key='s', fun=move_back)
my_screen.onkey(key='d', fun=turn_right)
my_screen.onkey(key='a', fun=turn_left)
my_screen.onkey(key='c', fun=clear)


my_screen.exitonclick()




