from turtle import Turtle, Screen
import random

mason, henryk, dad, mom = Turtle(), Turtle(), Turtle(), Turtle()
screen = Screen()
mason.name = 'Mason'
henryk.name = 'Henryk'
dad.name = 'Dad'
mom.name = 'Mom'

racers = [mason, henryk, dad, mom]
colors = ['red', 'blue', 'green', 'pink']

# Randomize the start
random.shuffle(racers)


def position_racers(racers):
    """ Position the racer and attach there coloours and shape """
    n = -150.00
    index = 0
    for racer in racers:
        racer.shape('turtle')
        racer.color(colors[index])
        racer.penup()
        racer.setpos(x=-320.00, y=n)
        racer.pendown()
        n += 100
        index += 1

position_racers(racers)

def race_forward(racer):
    """ Move the racers forward a random number of steps """
    steps = random.randint(1, 20)
    racer.fd(steps)

def race(racers):
    """ Start the race and keep it going until a racer reaches 320 """
    race = 'on'
    while race == 'on':
        for racer in racers:
            if racer.xcor() < 320.00:
                race_forward(racer)
            else:
                screen.title(f"And the winner is {racer.name}")
                print(f"And the winner is {racer.name}")
                race = 'off'


race(racers)

screen.exitonclick()