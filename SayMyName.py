import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue" , "green", "orange", "purple"]
your_name = turtle.textinput("Введите свое имя", "Как тебя зовут?")
for x in range (100):
    t.pencolor(colors[x%6])
    t.penup()
    t.forward(x * 6)
    t.pendown()
    t.write(your_name, font = ("Arial", int((x + 6)/6), "bold"))
    t.left(61)