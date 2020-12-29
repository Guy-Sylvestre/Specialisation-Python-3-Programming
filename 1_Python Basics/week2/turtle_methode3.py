import turtle
wn = turtle.Screen()
# wn.bgcolor("lightgreen")
tess = turtle.Turtle()
# tess.color("blue")
tess.shape("turtle") #donner une forme à la turture "share()"

dist = 50
tess.up()                     # this is new => lever
for _ in range(3):
    # start with size = 5 and grow by 2
    tess.forward(dist)
    tess.stamp()                # leave an impression on the canvas =>tampon laisse des traces
   
wn.exitonclick()
