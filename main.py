from turtle import Turtle, Screen

mason, henryk, dad, mom = Turtle(), Turtle(), Turtle(), Turtle()
screen = Screen();


racers = [mason, henryk, dad, mom]
colors = ['red', 'blue', 'green', 'pink']
# Position the racers

def position_racers(racers):
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









screen.exitonclick()