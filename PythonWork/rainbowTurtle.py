import turtle
t = turtle.Pen()
t.color(1,0,0)
t.begin_fill()
t.circle(50)
t.end_fill()
def mycircle(red,green,blue):
    t.color(red,green,blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()


mycircle(0.75,0.75,0.75)
mycircle(1,0,0)
mycircle(1,0.5,0)
mycircle(1,1,0)
mycircle(0,1,0)
mycircle(0,1,0.5)
mycircle(0,1,1)
mycircle(0,0,1)
mycircle(1,0.5,0.5)
mycircle(1,0.50,0.50)
t.reset
mycircle(0,0,0)
mycircle(0.75,1,1)
mycircle(0,0.75,0)
mycircle(1,0,1)
mycircle(0,0,0)
