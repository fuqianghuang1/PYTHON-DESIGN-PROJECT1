import turtle
bob = turtle.Turtle()
turtle.colormode(255)
bob.speed(0)
turtle.bgcolor(0,0,0)
bob.penup()
bob.goto(-100,-100)
bob.pendown()

for times in range(45):
    bob.color("red")
    bob.forward(200)
    bob.right(100)
    
bob.penup()
bob.goto(1,50)
bob.pendown()

for times in range(40):
    bob.forward(150)
    bob.left(110)
    bob.forward(150)
    bob.color("green")
    
bob.penup()
bob.goto(30,55)
bob.pendown()

for times in range(45):
    bob.color("blue")
    bob.forward(100)
    bob.left(100)

bob.penup()
bob.goto(20,50)
bob.pendown()

for times in range(35):
    bob.color("white")
    bob.forward(100)
    bob.right(200)
    
bob.penup()
bob.goto(20,65)
bob.pendown()

for times in range(55):
    bob.color("blue")
    bob.forward(100)
    bob.right(100)
    
bob.penup()
bob.goto(1,50)
bob.pendown()

for times in range(45):
    bob.color("blue")
    bob.forward(100)
    bob.left(100)

bob.penup()
bob.goto(30,55)
bob.pendown()
 
    



