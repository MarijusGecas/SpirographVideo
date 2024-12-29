import turtle, random

colors = [
    "red", "orange", "yellow", "lime", "springgreen", "chartreuse",
    "cyan", "deepskyblue", "royalblue", "mediumslateblue",
    "violet", "magenta", "orchid", "darkorchid",
    "pink", "hotpink", "gold", "white", "silver", "lightgray"
]

screen = turtle.Screen()
screen.bgcolor("black")

tim = turtle.Turtle()
tim.width(2)
tim.speed(100)

angle = 5

while angle <= 360:
    tim.color(random.choice(colors))
    tim.circle(100)
    tim.right(5)
    angle += 5


screen.mainloop()
