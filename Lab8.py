#Alex Philpott

# Designed to simulate a non-head-on, 2-D collision between two same-size balls of arbitrary mass and initial velocities

# Students are recommended to follow the template, not only because it
# provides a natural structure, but also because assistance from the instructor
# and learning assistants can be more effective when the code is familiar.

# Ordinary comments have a pound sign (#) as the first character, as in this line

## Suggested but incomplete programming statements below are marked with two pounds signs, as in this line
 
# Import necessary packages
from visual import *
from visual.graph import *
from math import*

# Define displays for graphs
#Defining graphs
gdisplay1 = gdisplay(x=0,   y=0,   width=400, height=200, xtitle='time (s)', ytitle='p (kg m / s)', title = 'Ball x momenta (lab) vs time (Isaac Newton)', background=color.white, foreground=color.black)
p1vst = gcurve(gdisplay=gdisplay1, color=color.red)
p2vst = gcurve(gdisplay=gdisplay1, color=color.green)
ptotvst = gcurve(gdisplay=gdisplay1, color=color.blue)
gdisplay2 = gdisplay(x=0,   y=200, width=400, height=200, xtitle='time (s)', ytitle='KE (J)', title = 'Ball kinetic energies (lab) vs time (Isaac Newton)', background=color.white, foreground=color.black)
k1vst = gcurve(gdisplay=gdisplay2, color=color.red)
k2vst = gcurve(gdisplay=gdisplay2, color=color.green)
ktotvst = gcurve(gdisplay=gdisplay2, color=color.blue)

# Coefficient of restitution (1.0 - elastic, 0.0 - fully inelastic)
COR = 1.0
#COR = 0.5


# Choose initial condition set
set = 2

# Ball radius
R = 0.5

# Set ball masses, initial velocities and ball 1's impact parameter
m1 = 1.0

if set==1:
  m2 = 2.0
  v1i = 1.0
  v2i = 0.0
  b = R/sqrt(2.)
elif set==2:
  m2 = 2.0
  v1i = 1.0
  v2i = 0.0
  b = R
elif set==3:
  m2 = 0.2
  v1i = 2.0
  v2i = 0.5
  b = 1.9*R
elif set==4:
  m2 = 1.5
  v1i = 1.0
  v2i = 0.0
  b = R/2.0
elif set==5:
  m2 = 2.0
  v1i = 2.0
  v2i = 0.5
  b = 0.0


# Create ball objects in each animation frame 
scenelab = display(x=400, y=0,   width=400, height=200, center=(8,0,0), range=12, title='1-d collision animation - lab frame (Isaac Newton)', background=color.white)
ball1lab = sphere(pos=(0,b,0), radius=R, color=color.red, make_trail=True, visible=True)
ball2lab = sphere(pos=(5,0,0), radius=R, color=color.green, make_trail=True, visible=True)

scenecm = display(x=400, y=200, width=400, height=200,  center=(3,0,0), range=12, title='1-d collision animation - cm frame (Isaac Newton)', background=color.white)
ball1cm =  sphere(pos=(0,b,0), radius=R, color=color.red, make_trail=True, visible=True)
ball2cm =  sphere(pos=(5,0,0), radius=R, color=color.green, make_trail=True, visible=True)

# Set initial lab frame ball velocity vectors
ball1lab.vel = vector(v1i,0,0)
ball2lab.vel = vector(v2i,0,0)

# Compute velocity of the center of mass of the balls as seen in the lab frame
cmv = (m1*ball1lab.vel+m2*ball2lab.vel)/(m1+m2)

# Compute ball velocities as seen in the c.m. frame
ball1cm.vel = ball1lab.vel-cmv
ball2cm.vel = ball2lab.vel-cmv

# Initialize time and define time step
dt = 0.001
t = 0.

# Loop over time steps

while t <= 8.:

    # Limit refresh rate if animating
    rate(1./dt)

    # Update ball positions in both frames
    ball1lab.pos = ball1lab.pos+ball1lab.vel*dt
    ball2lab.pos = ball2lab.pos+ball2lab.vel*dt
    ball1cm.pos = ball1cm.pos+ball1cm.vel*dt
    ball2cm.pos = ball2cm.pos+ball2cm.vel*dt
    rhat = norm(ball1lab.pos-ball2lab.pos)
    
    # If ball centers are closer than the sum of their radii AND they are approaching each other, then make them bounce
    rdiff = ball2cm.pos-ball1cm.pos
    if mag(rdiff) < 2*R and dot(rdiff,ball1cm.vel)>0:
        v1parallel = -COR*dot(ball1cm.vel,rhat)*rhat
        v1perp = cross(rhat,cross(ball1cm.vel,rhat))
        ball1cm.vel = v1parallel+v1perp
        ball1lab.vel = ball1cm.vel+cmv
        
        v2parallel = -COR*dot(ball2cm.vel,rhat)*rhat
        v2perp = cross(rhat,cross(ball2cm.vel,rhat))
        ball2cm.vel = v2parallel+v2perp
        ball2lab.vel = ball2cm.vel+cmv

    # Update graphs
    p1vst.plot(pos=(t,ball1lab.vel.x*m1))
    p2vst.plot(pos=(t,ball2lab.vel.x*m2))
    ptotvst.plot(pos=(t,ball1lab.vel.x*m1+ball2lab.vel.x*m2))
    k1vst.plot(pos=(t, 0.5*m1*mag2(ball1lab.vel)))
    k2vst.plot(pos=(t,0.5*m2*mag2(ball2lab.vel)))
    ktotvst.plot(pos=(t,0.5*m1*mag2(ball1lab.vel)+0.5*m2*mag2(ball2lab.vel)))

    # Increment time step
    t = t + dt

print('Done')
print('The angle between v1 and v1i in radians is:', acos(dot(ball1lab.vel,vector(v1i,0,0))/mag(ball1lab.vel)/v1i))
print('The angle between v2 and v2i in radians is:', atan(ball2lab.vel.y/ball2lab.vel.x))
