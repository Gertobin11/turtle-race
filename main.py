from turtle import Turtle, Screen
import random

mason, henryk, dad, mom = Turtle(), Turtle(), Turtle(), Turtle()
screen = Screen()
names = ['Mason', 'Henryk', 'Dad', 'Mom', 'Chris', 'Donal']

racers = []
colors = ['red', 'blue', 'green', 'pink', 'orange', 'black']

# Randomize the start
random.shuffle(racers)

def position_racers(racers):
    """ Position the racer and attach there colours and shape """
    n = -150.00
    index = 0
    for racer in range(0, 6):
        racer = Turtle()
        racer.shape('turtle')
        racer.color(colors[index])
        racer.name = names[index]
        racers.append(racer)
        racer.penup()
        racer.setpos(x=-320.00, y=n)
        racer.pendown()
        n += 40
        index += 1

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

def start():
    """ Start the race """
    position_racers(racers)
    race(racers)

start()

screen.exitonclick()