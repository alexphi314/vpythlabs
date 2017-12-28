from visual import *
from visual.graph import *

#defining constants
gvector = vector(0,-9.8,0)
t = 0
dt = 0.0005
scene.autoscale = True
display(title='Ball in a Box Animation (Alex Philpott)', background=color.white)

#defining sets
set = 1

#setting variables for each set
if set==1:
    x0 = 0
    y0 = 0
    z0 = 0
    xv0 = 3
    yv0 = 3
    zv0 = 1

if set==2:
    x0 = -4
    y0 = 0
    z0 = 0
    xv0 = 1
    yv0 = -10
    zv0 = 1

if set==3:
    x0 = 4.7
    y0 = 4.7
    z0 = 4.7
    xv0 = -30
    yv0 = -30
    zv0 = -30

if set==4: #these are the test conditions from the lab
    x0 = 1
    y0 = 2
    z0 = 3
    xv0 = -3
    yv0 = 4
    zv0 = 2
    
#defining ball
ball = sphere(pos=(x0,y0,z0), radius = 0.2, color=color.blue, make_trail=True)
ball.velocity = vector(xv0,yv0,zv0)

#defining box
thickness=0.1
wallB = box(pos=(0,-5.05,0), size=(10,thickness,10), color=color.yellow)
wallT = box(pos=(0,5.05,0), size=(10,thickness,10), color=color.yellow)
wallR = box(pos=(5.05,0,0), size=(thickness,10,10), color=color.yellow)
wallL = box(pos=(-5.05,0,0), size=(thickness,10,10), color=color.yellow)
wallback = box(pos=(0,0,-5.05), size=(10,10,thickness), color=color.yellow)
wallF = box(pos=(0,0,5.05), size=(10,10,thickness), color=color.yellow, opacity=0.2)

#creating graphs
display2 = gdisplay(x=0, y=0, width=600, height=300, title='Ball x vs t (Alex Philpott)',
                    background=color.white, foreground=color.black)
function2 = gcurve(gdisplay=display2, color=color.blue)
display3 = gdisplay(x=0, y=0, width=600, height=300, title='Ball y vs t (Alex Philpott)',
                    background=color.white, foreground=color.black)
function3 = gcurve(gdisplay=display3, color=color.blue)
display4 = gdisplay(x=0, y=0, width=600, height=300, title='Ball z vs t (Alex Philpott)',
                    background=color.white, foreground=color.black)
function4 = gcurve(gdisplay=display4, color=color.blue)

#updating scene
while t<10:
    rate(1000)
    t= t+dt
    ball.pos = ball.pos + ball.velocity*dt
    ball.velocity = ball.velocity + gvector*dt
    if ball.pos.x + ball.radius > wallR.pos.x - thickness/2:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.x - ball.radius < wallL.pos.x + thickness/2:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.y + ball.radius > wallT.pos.y - thickness/2:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.y - ball.radius < wallB.pos.y + thickness/2:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.z + ball.radius > wallF.pos.z - thickness/2:
        ball.velocity.z = -ball.velocity.z
    if ball.pos.z - ball.radius < wallback.pos.z + thickness/2:
        ball.velocity.z = -ball.velocity.z
    function2.plot(pos=(t, ball.pos.x))
    function3.plot(pos=(t, ball.pos.y))
    function4.plot(pos=(t, ball.pos.z))
    

