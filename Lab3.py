#Alex Philpott
from visual import *
from visual.graph import *
from math import *

#defining constants
t = 0
dt = 0.001
g = vector(0,-9.8,0)
a1 = 30*pi/180
a2 = 45*pi/180
a3 = 60*pi/180
display(title = 'Ball in flight - no drag (Alex Philpott)',
          background=color.white, center=(15,5,0), range=20)

#ball 1
ball1 = sphere(pos=(0,0.5,0), radius = 0.5, color=color.red, make_trail = True)
ball1.velocity = vector(15*cos(a1),15*sin(a1),0)

#ball 2
ball2 = sphere(pos=(0,0.5,0), radius = 0.5, color=color.green, make_trail = True)
ball2.velocity = vector(15*cos(a2), 15*sin(a2),0)

#ball 3
ball3 = sphere(pos=(0,0.5,0), radius = 0.5, color=color.blue, make_trail = True)
ball3.velocity = vector(15*cos(a3), 15*sin(a3), 0)

#creating graphs
display2 = gdisplay(x=0, y=0, width=600, height=300, title='Ball x vs t (Alex Philpott)',
                background=color.white, foreground=color.black, ymin = -5, ymax = 30)
display3 = gdisplay(x=0, y=0, width=600, height=300, title='Ball y vs t (Alex Philpott)',
                    background=color.white, foreground=color.black, ymin = -2.5, ymax = 15)
function1 = gcurve(gdisplay=display2, color=color.red)
function2 = gcurve(gdisplay=display2, color=color.green)
function3 = gcurve(gdisplay=display2, color=color.blue)
function15 = gcurve(gdisplay=display3, color=color.red)
function25 = gcurve(gdisplay=display3, color=color.green)
function35 = gcurve(gdisplay=display3, color=color.blue)

#updating the scene
while ball3.velocity.x > 0:
    rate(1000)

    #ball 1 updates
    ball1.pos = ball1.pos + ball1.velocity*dt
    ball1.velocity = ball1.velocity + g*dt

    #ball 2 updates
    ball2.pos = ball2.pos + ball2.velocity*dt
    ball2.velocity = ball2.velocity + g*dt

    #ball 3 updates
    ball3.pos = ball3.pos + ball3.velocity*dt
    ball3.velocity = ball3.velocity + g*dt

    #stopping balls upon impact
    if ball1.pos.y < 0.5:
        ball1.velocity = vector(0,0,0)
    if ball2.pos.y < 0.5:
        ball2.velocity = vector(0,0,0)
    if ball3.pos.y < 0.5:
        ball3.velocity = vector(0,0,0)

    #updating time
    t = t+dt

    #plotting
    function1.plot(pos=(t,ball1.pos.x))
    function2.plot(pos=(t,ball2.pos.x))
    function3.plot(pos=(t,ball3.pos.x))
    function15.plot(pos=(t,ball1.pos.y-0.5))
    function25.plot(pos=(t,ball2.pos.y-0.5))
    function35.plot(pos=(t,ball3.pos.y-0.5))
