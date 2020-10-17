import turtle
import random as r

print('''
1. Koch Snowflake
2. Fractal Tree
3. Dragon Curve
4. Fractal Plant
5. Pentaplexity
6. Peano-Gosper-Curve
7. Quadratic-Gosper
8. Own Plant
9. Own Geometric 
''')
choice = int(input('Fractal number: '))

rules = axiom = iterations = length = startAngle = angle = 0
if choice == 1:
	# KOCH SNOWFLAKE
	rules = {'F': 'F-F++F-F'}
	axiom = 'F++F++F'
	iterations = 4
	length = 5
	startAngle = 0
	angle = 60
elif choice == 2:
	# FRACTAL TREE
	rules = {'F': 'G[-F]+F', 'G': 'GG'}
	axiom = 'F'
	iterations = 8
	length = 3
	startAngle = 90
	angle = 45
elif choice == 3:
	# DRAGON CURVE
	rules = {'X': 'X+YF+', 'Y': '-FX-Y'}
	axiom = 'FX'
	iterations = 13
	length = 5
	startAngle = 90
	angle = 90
elif choice == 4:
	# FRACTAL PLANT
	rules = {'X': 'F-[[X]+X]+F[+FX]-X', 'F': 'FF'}
	axiom = 'X'
	iterations = 6
	length = 3
	startAngle = 90
	angle = 22.5
elif choice == 5:
	# Pentaplexity
	rules = {'F': 'F++F++F+++++F-F++F'}
	axiom = 'F++F++F++F++F'
	iterations = 5
	length = 3
	startAngle = 0
	angle = 36
elif choice == 6:
	# Peano-Gosper-Curve
	rules = {"X":"X+YF++YF-FX--FXFX-YF+", "Y":"-FX+YFYF++YF+FX--FX-Y"}
	axiom = 'FX'
	iterations = 4
	length = 10
	startAngle = 90
	angle = 60
elif choice == 7:
	# Quadratic-Gosper
	rules = {
		"X": "XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-",
		"Y": "+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY"
	}
	axiom = 'YF'
	iterations = 3
	length = 5
	startAngle = 0
	angle = 90
elif choice == 8:
	# OWN PLANT
	rules = {"X": "X[-XXX][+XF]FX", "Y": "YFX[+YY][-X]"}
	axiom = 'Y'
	iterations = 6
	length = 4
	startAngle = 90
	angle = 25.7
elif choice == 9:
	# OWN GEOMETRIC
	rules = {"F": "FF+F++F++F+F"}
	axiom = 'F+F+F+F'
	iterations = 5
	length = 3
	startAngle = 90
	angle = 90


word = [axiom]
for i in range(iterations):
	nextWord = word[len(word)-1]
	nextAxiom = []
	for symbol in nextWord:
		if symbol in rules:
			nextAxiom.append(rules[symbol])
		else:
			nextAxiom.append(symbol)
	word.append(''.join(nextAxiom))


wn = turtle.Screen()
rootwindow = wn.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
screen = turtle.Screen()
screen.tracer(False)
screen.screensize(1500, 1500)


turt = turtle.Turtle(visible=False)
turt.screen.title("L-System")
turt.speed(0)
turt.setheading(startAngle)

stack = []
for action in word[len(word)-1]:
	turt.pd()
	if action in ["F", "G"]:
		turt.forward(length)
	elif action == "f":
		turt.pu()
		turt.forward(length)
	elif action == "+":
		turt.right(angle)
	elif action == "-":
		turt.left(angle)
	elif action == "[":
		stack.append((turt.position(), turt.heading()))
	elif action == "]":
		turt.pu()
		position, heading = stack.pop()
		turt.goto(position)
		turt.setheading(heading)

screen.update()
screen.exitonclick()
