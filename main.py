from turtle import Turtle, Screen

mason, henryk, dad, mom = Turtle(), Turtle(), Turtle(), Turtle()
screen = Screen();

# Turn them into turles
mason.shape('turtle')
henryk.shape('turtle')
dad.shape('turtle')
mom.shape ('turtle')

# Add different colours to the turtles
mason.color ('red', 'red')
henryk.color ('blue', 'blue')
dad.color ('green', 'green')
mom.color('pink', 'pink')

# Position the racers

mason.penup()
mason.setpos(x=-320.00, y=50.00)
mason.pendown()

henryk.penup()
henryk.setpos(x=-320.00, y=-50.00)
henryk.pendown()

dad.penup()
dad.setpos(x=-320.00, y=150.00)
dad.pendown()

mom.penup()
mom.setpos(x=-320.00, y=-150.00)
mom.pendown()






screen.exitonclick()