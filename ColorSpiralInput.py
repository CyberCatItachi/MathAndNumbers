import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue" , "green", "orange", "purple", "white", "gray"]
sides = int(turtle.numinput("Сколько сторон", "Сколько сторон вы хотите?(1-8)", 4, 1, 8))
for x in range (100):
    t.pencolor(colors[x%sides])
    #t.circle(x * 3 / sides + x)
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 1)
    #t.left(360/sides)
    t.width(x * sides / 200)