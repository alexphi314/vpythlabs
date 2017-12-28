#Alex Philpott
from visual import *
from visual.graph import *
from math import *

#defining constants
t = 0
dt = 0.001
a1 = 80*pi/180
a2 = a1
a3 = a1
v0 = 85.
mGb = 0.045
g = mGb*vector(0,-9.8,0)
p = 1.3
Cd = 0.5
A = 0.001521
Fd = -0.5*p*(Cd)*A
ac1 = vector(0,0,0)
ac2 = vector(0,0,0)
ac3 = vector(0,0,0)
z = vector(0,0,1)
k = 0.5*mGb
p = mGb*9.8
display(title = 'Ball in flight - with drag (Alex Philpott)',
          background=color.white, center=(100,100,0), range=200)

#ball 1
ball1 = sphere(pos=(0,0.5,0), radius = 0.022, color=color.red, make_trail = True)
ball1.velocity = vector(v0*cos(a1),v0*sin(a1),0.)
k1 = k*mag(ball1.velocity)**2
p1 = p*(ball1.pos.y-0.022)
w1 = k1
ball1.disp = 0

#ball 2
ball2 = sphere(pos=(0,0.5,0), radius = 0.022, color=color.green, make_trail = True)
ball2.velocity = vector(v0*cos(a2), v0*sin(a2),0)
ball2.thrust = 6*9.8*mGb*ball2.velocity
k2 = k*mag(ball2.velocity)**2
p2 = p*(ball2.pos.y-0.022)
w2 = k2
ball2.trail = curve(color=color.magenta)
ball2.disp = 0

#ball 3
ball3 = sphere(pos=(0,0.5,0), radius = 0.022, color=color.blue, make_trail = True)
ball3.velocity = vector(v0*cos(a3), v0*sin(a3), 0)
k3 = k*mag(ball3.velocity)**2
p3 = p*(ball3.pos.y-0.022)
ball3.thrust = 6*9.8*mGb*cross(ball3.velocity,z)
w3 = k3
ball3.trail = curve(color=color.magenta)
ball3.disp = 0

#creating graphs
display2 = gdisplay(x=0, y=0, width=600, height=300, title='Ball x vs t (Alex Philpott)',
                background=color.white, foreground=color.black, ymin = -30, ymax = 300)
display3 = gdisplay(x=0, y=0, width=600, height=300, title='Ball y vs t (Alex Philpott)',
                    background=color.white, foreground=color.black, ymin = -30, ymax = 300)
display4 = gdisplay(x=0, y=0, width=600, height=300, title='Speed v vs t (Alex Philpott)',
                    background=color.white, foreground=color.black, ymin = -20, ymax = 100)
display5 = gdisplay(x=0, y=0, width=600, height =300, title='Distance vs t (Alex Philpott)',
                    background=color.white, foreground=color.black, ymin = -50, ymax= 500)
display6 = gdisplay(x=0, y=0, width=600, height =300, title='Instantaneous Kinetic Energy (J) vs t (Alex Philpott)',
                    background=color.white, foreground=color.black, ymin = -40, ymax= 200)
display7 = gdisplay(x=0, y=0, width=600, height =300, title='Instantaneous Potential Energy (J) vs t (Alex Philpott)',
                    background=color.white, foreground=color.black, ymin = -40, ymax= 200)
display8 = gdisplay(x=0, y=0, width=600, height =300, title='Original K.E. + work done (J) (Alex Philpott)',
                    background=color.white, foreground=color.black, ymin = -40, ymax= 200)
display9 = gdisplay(x=0, y=0, width=600, height =300, title='Instantaneous Total Mechanical Energy (Alex Philpott)',
                    background=color.white, foreground=color.black, ymin = -40, ymax= 200)
function1 = gcurve(gdisplay=display2, color=color.red)
function2 = gcurve(gdisplay=display2, color=color.green)
function3 = gcurve(gdisplay=display2, color=color.blue)
function15 = gcurve(gdisplay=display3, color=color.red)
function25 = gcurve(gdisplay=display3, color=color.green)
function35 = gcurve(gdisplay=display3, color=color.blue)
function16 = gcurve(gdisplay=display4, color=color.red)
function26 = gcurve(gdisplay=display4, color=color.green)
function36 = gcurve(gdisplay=display4, color=color.blue)
function41 = gcurve(gdisplay=display5, color=color.red)
function42 = gcurve(gdisplay=display5, color=color.green)
function43 = gcurve(gdisplay=display5, color=color.blue)
function61 = gcurve(gdisplay=display6, color=color.red)
function62 = gcurve(gdisplay=display6, color=color.green)
function63 = gcurve(gdisplay=display6, color=color.blue)
function71 = gcurve(gdisplay=display7, color=color.red)
function72 = gcurve(gdisplay=display7, color=color.green)
function73 = gcurve(gdisplay=display7, color=color.blue)
function81 = gcurve(gdisplay=display8, color=color.red)
function82 = gcurve(gdisplay=display8, color=color.green)
function83 = gcurve(gdisplay=display8, color=color.blue)
function91 = gcurve(gdisplay=display9, color=color.red)
function92 = gcurve(gdisplay=display9, color=color.green)
function93 = gcurve(gdisplay=display9, color=color.blue)

#updating the scene
while ball2.velocity.x > 0:
    rate(1000)

    #ball 1 updates
    ball1.pos = ball1.pos + ball1.velocity*dt
    ball1.velocity = ball1.velocity + ac1*dt
    drag1 = Fd*mag2(ball1.velocity)*norm(ball1.velocity)
    Fn1 = (drag1 + g)
    ac1 = Fn1/mGb
    k1 = k*mag(ball1.velocity)**2
    p1 = p*(ball1.pos.y-0.022)
    w1 = w1 + dot(Fn1, ball1.velocity*dt)
    m1 = k1+p1
    ball1.disp = ball1.disp + mag(ball1.velocity)*dt

    #ball 2 updates
    ball2.pos = ball2.pos + ball2.velocity*dt
    ball2.velocity = ball2.velocity + ac2*dt
    drag2 = Fd*mag2(ball2.velocity)*norm(ball2.velocity)
    Fn2 = drag2 + g
    ball2.thrust = 6*9.8*mGb*norm(ball2.velocity)
    if t>=1 and t<=3:
        Fn2 = Fn2 + ball2.thrust
        ball2.trail.append(pos=ball2.pos)
    ac2 = Fn2/mGb
    k2 = k*mag(ball2.velocity)**2
    p2 = p*(ball2.pos.y-0.022)
    w2 = w2 + dot(Fn2, ball2.velocity*dt)
    m2 = k2+p2
    ball2.disp = ball2.disp + mag(ball2.velocity)*dt

    #ball 3 updates
    ball3.pos = ball3.pos + ball3.velocity*dt
    ball3.velocity = ball3.velocity + ac3*dt
    drag3 = Fd*mag2(ball3.velocity)*norm(ball3.velocity)
    Fn3 = drag3 + g
    ball3.thrust = 6*9.8*mGb*norm(cross(ball3.velocity,z))
    if t>= 1 and t<=3:
        Fn3 = Fn3 + ball3.thrust
        ball3.trail.append(pos=ball3.pos)
    ac3 = Fn3/mGb
    k3 = k*mag(ball3.velocity)**2
    p3 = p*(ball3.pos.y-0.022)
    w3 = w3 + dot(Fn3, ball3.velocity*dt)
    m3 = k3+p3
    ball3.disp = ball3.disp + mag(ball3.velocity)*dt

    #stopping balls upon impact
    if ball1.pos.y < 0.022:
        ball1.velocity = vector(0,0,0)
        w1 = 0
    if ball2.pos.y < 0.022:
        ball2.velocity = vector(0,0,0)
    if ball3.pos.y < 0.022:
        ball3.velocity = vector(0,0,0)
        w3 = 0
        
    #updating time
    t = t+dt

    #plotting
    function1.plot(pos=(t,ball1.pos.x))
    function2.plot(pos=(t,ball2.pos.x))
    function3.plot(pos=(t,ball3.pos.x))
    function15.plot(pos=(t,ball1.pos.y-0.022))
    function25.plot(pos=(t,ball2.pos.y-0.022))
    function35.plot(pos=(t,ball3.pos.y-0.022))
    function16.plot(pos=(t,mag(ball1.velocity)))
    function26.plot(pos=(t,mag(ball2.velocity)))
    function36.plot(pos=(t,mag(ball3.velocity)))
    function41.plot(pos=(t,ball1.disp))
    function42.plot(pos=(t,ball2.disp))
    function43.plot(pos=(t,ball3.disp))
    function61.plot(pos=(t,k1))
    function62.plot(pos=(t,k2))
    function63.plot(pos=(t,k3))
    function71.plot(pos=(t,p1))
    function72.plot(pos=(t,p2))
    function73.plot(pos=(t,p3))
    function81.plot(pos=(t,w1))
    function82.plot(pos=(t,w2))
    function83.plot(pos=(t,w3))
    function91.plot(pos=(t,m1))
    function92.plot(pos=(t,m2))
    function93.plot(pos=(t,m3))
