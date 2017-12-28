from visual import *
from visual.graph import *

#defining constants
t=0
deltat=0.001
g=9.8
display(title='Moving Cart (Alex Philpott)', background=color.white)


#defining track
track = box(pos=vector(0,0.025,0), size=(2.0,0.05,0.10), color=color.green)

# defining barrier
barrier = box(pos=vector(0.95,0.25,0), size=(0.1,0.4,0.1), color=color.red)

#defining cart
cart = box(pos=vector(-0.95,0.075,0), size=(0.1,0.05,0.05), color=color.blue)
vcart = vector(0.5,0,0)
acart = vector(0,-g,0)

#defining trail
cart.trail = curve(color=color.magenta)

#creating a graph
display2 = gdisplay(x=0,y=0, width=600, height=300, title='Cart x vs t (Alex Philpott)',
                  background=color.white, foreground=color.black)
function = gcurve(gdisplay=display2, color=color.green)

#updating scene
while t < 4:
    rate(1000)
    if cart.pos.x > 0.85:
        vcart.x = -vcart.x
    cart.pos = cart.pos + vcart*deltat
    cart.trail.append(pos=cart.pos)
    function.plot(pos=(t, cart.pos.x))
    t=t+deltat
    

