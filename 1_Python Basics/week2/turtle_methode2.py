import turtle
wn = turtle.Screen()
# wn.bgcolor("lightgreen")
tess = turtle.Turtle()
# tess.color("blue")
tess.shape("square") #donner une forme à la turture "share()"

dist = 100
# tess.up()                     # this is new => lever
for _ in range(7):
    # start with size = 5 and grow by 2
    tess.forward(dist)
    tess.stamp()                # leave an impression on the canvas =>tampon laisse des traces
    tess.forward(-dist)          # move tess along
    tess.right(36)              # and turn her
    # dist = dist + 2
wn.exitonclick()
