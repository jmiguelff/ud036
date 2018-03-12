import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("cyan")

	brad = turtle.Turtle()
	brad.shape("blank")
	brad.speed(10)
	brad.color("pink")
	brad.width(10)

	
	brad.forward(100)
	brad.right(90)
	
	brad.forward(100)
	brad.right(90)
	
	brad.forward(100)
	brad.right(90)
	
	brad.forward(100)
	brad.right(90)

	window.exitonclick()

draw_square()