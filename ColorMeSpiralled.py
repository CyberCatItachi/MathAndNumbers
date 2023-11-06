import turtle
t = turtle.Pen()
turtle.bgcolor("black")
#
colors = ["red", "yellow", "blue" , "green", "orange", "purple", "white", "gray"]
#
your_name = turtle.textinput("Введите свое имя", "Как тебя зовут?")
#
sides = int(turtle.numinput("Сколько сторон", "Сколько сторон вы хотите?(1-8)", 4, 1, 8))
for x in range (100):
    #
    t.pencolor(colors[x%sides])
    t.penup()
    t.forward(x * 3 / sides + x)
    t.pendown()
    t.write(your_name, font = ("Arial", int((x + sides)/sides), "bold"))
    t.left(360/sides + 1)