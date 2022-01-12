import turtle
my_turtle=turtle.Turtle()
my_turtle.speed(0)

def van():
	
	my_turtle.right(-45)
	my_turtle.forward(100)
	my_turtle.right(135)
	my_turtle.forward(-50)
	my_turtle.right(-90)
	my_turtle.forward(100)
	my_turtle.right(90)
	my_turtle.forward(122)
	my_turtle.right(90)
	my_turtle.forward(175)
	my_turtle.right(90)


for i in range(5):	
    van()
    my_turtle.right(10)
turtle.done()

