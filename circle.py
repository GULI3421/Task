import turtle as hub
import colorsys as cs

hub.tracer(20)
hub.bgcolor("black")
hub.setpos(0, -230)
r = 0
hub.setup(800,600)
hub.width(20)
hub.ht()
for i in range(2000):
    r += 0.01
    color = cs.hsv_to_rgb(r,1,1)
    hub.fillcolor(color)
    hub.begin_fill()
    hub.circle(i,120)
    hub.circle(90,90)
    hub.circle(i,120)
    hub.end_fill()
hub.done()
