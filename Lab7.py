#Alex Philpott
#Lab 7
 
# Import necessary packages
from visual import *
from visual.graph import *

# Define displays for graphs (don't forget -- you are not Isaac Newton -- change the name!)
gdisplay1 = gdisplay(x=0,   y=0,   width=400, height=200, xtitle='time (s)', ytitle='x (m)', title = 'Ball positions vs time (Alex Philpott)', background=color.white, foreground=color.black)
x1vst = gcurve(gdisplay=gdisplay1, color=color.red)
x2vst = gcurve(gdisplay=gdisplay1, color=color.green)

gdisplay2 = gdisplay(x=0,   y=200, width=400, height=200, xtitle='time (s)', ytitle='v (m/s)', title = 'Ball velocities (lab) vs time (Alex Philpott)', background=color.white, foreground=color.black)
v1vst = gcurve(gdisplay=gdisplay2, color=color.red)
v2vst = gcurve(gdisplay=gdisplay2, color=color.green)

gdisplay3 = gdisplay(x=0,   y=400, width=400, height=200, xtitle='time (s)', ytitle='p (kg m / s)', title = 'Ball momenta (lab) vs time (Alex Philpott)', background=color.white, foreground=color.black)
p1vst = gcurve(gdisplay=gdisplay3, color=color.red)
p2vst = gcurve(gidsplay=gdisplay3, color=color.green)
ptotvst = gcurve(gdisplay=gdisplay3, color=color.blue)

gdisplay4 = gdisplay(x=400, y=400, width=400, height=200, xtitle='time (s)', ytitle='KE (J)', title = 'Ball kinetic energies (lab) vs time (Alex Philpott)', background=color.white, foreground=color.black)
ke1vst = gcurve(gdisplay=gdisplay4, color=color.red)
ke2vst = gcurve(gdisplay=gdisplay4, color=color.green)
ketotvst = gcurve(gdisplay=gdisplay4, color=color.blue)

# Coefficient of restitution (1.0 - elastic, 0.0 - fully inelastic) - relevant to extra credit option
cor = 1.0

# Choose initial condition set
set = 0
#set = 1

# Set ball masses initial velocities
if set==0:
  m1 = 1.0
  m2 = 2.0
  v1i = 2.0
  v2i = 0.5
elif set==1:
  m1 = 1.0
  m2 =3.0
  v1i = 1.0
  v2i = 0.0

# Ball radius
R = 0.25 

# Create ball objects in each animation frame 
scenelab = display(x=400, y=0, width=400, height=200, center=(8,0,0), range=10, title='1-d collision animation - lab frame (Alex Philpott)', background=color.white)
ball1lab = sphere(pos=(0,0,0), radius=R, color=color.red, make_trail=True, visible=True)
ball2lab = sphere(pos=(5,0,0), radius=R, color=color.green, make_trail=True, visible=True)

scenecm = display(x=400, y=200, width=400, height=200,  center=(3,0,0), range=10, title='1-d collision animation - cm frame (Alex Philpott)', background=color.white)
ball1cm =  sphere(pos=(0,0,0), radius=R, color=color.red, make_trail=True, visible=True)
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
    
    # If ball centers are closer than the sum of their radii AND they are approaching each other, then make them bounce
    r12 = mag(ball1lab.pos-ball2lab.pos)
    if r12 < 2*R and dot(ball2cm.pos-ball1cm.pos,ball1cm.vel)>0:
      
        
        # Reverse velocities in the c.m. frame and apply coefficient of restitution, if appropriate
        ball1cm.vel = -cor*ball1cm.vel
        ball2cm.vel = -cor*ball2cm.vel

        # Recompute velocities in the lab frame from new c.m.-frame velocities
        ball1lab.vel = ball1cm.vel+cmv
        ball2lab.vel = ball2cm.vel+cmv

    # Update graphs
    x1vst.plot(pos=(t,ball1lab.pos.x))
    x2vst.plot(pos=(t,ball2lab.pos.x))
    v1vst.plot(pos=(t,ball1lab.vel.x))
    v2vst.plot(pos=(t,ball2lab.vel.x))
    p1vst.plot(pos=(t,ball1lab.vel.x*m1))
    p2vst.plot(pos=(t,ball2lab.vel.x*m2))
    ptotvst.plot(pos=(t,ball1lab.vel.x*m1+ball2lab.vel.x*m2))
    ke1vst.plot(pos=(t,0.5*m1*mag2(ball1lab.vel)))
    ke2vst.plot(pos=(t,0.5*m2*mag2(ball2lab.vel)))
    ketotvst.plot(pos=(t,0.5*m1*mag2(ball1lab.vel)+0.5*m2*mag2(ball2lab.vel)))
    
    # Increment time step
    t = t + dt

# Print out final kinetic energy for comparison with analytical calculation
print('Done - Final total kinetic energy (J) in lab frame is', 0.5*m1*mag2(ball1lab.vel)+0.5*m2*mag2(ball2lab.vel))
print('Final velocity of ball 1 is:', ball1lab.vel.x)
print('Final velocity of ball 2 is:', ball2lab.vel.x)
print('cmv', cmv)
