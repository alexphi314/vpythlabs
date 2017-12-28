#Alex Philpott

from visual import *
from numpy import matrix
from numpy import linalg

# Define inversion function for 3x3 matrix
# usage:  Ainv = invert(A) where A is a declared array 
def invert(inarray):
    debug = 0
    ixx = inarray[0,0]
    ixy = inarray[0,1]
    ixz = inarray[0,2]
    iyx = inarray[1,0]
    iyy = inarray[1,1]
    iyz = inarray[1,2]
    izx = inarray[2,0]
    izy = inarray[2,1]
    izz = inarray[2,2]
    determpls =   ixx*iyy*izz + ixy*iyz*izx + ixz*iyx*izy
    determmns = -(izx*iyy*ixz + izy*iyz*ixx + izz*iyx*ixy)
    determ = determpls + determmns
    oxx = (iyy*izz-izy*iyz)/determ
    oxy = (ixz*izy-izz*ixy)/determ
    oxz = (ixy*iyz-iyy*ixz)/determ
    oyx = (iyz*izx-izz*iyx)/determ
    oyy = (ixx*izz-izx*ixz)/determ
    oyz = (ixz*iyx-iyz*ixx)/determ
    ozx = (iyx*izy-izx*iyy)/determ
    ozy = (ixy*izx-izy*ixx)/determ
    ozz = (ixx*iyy-iyx*ixy)/determ
    outarray = array([ [oxx,oxy,oxz], [oyx,oyy,oyz], [ozx,ozy,ozz]])
    return outarray

# Define scene and title
scene = display(title='Dynamical spinning top (Alex Philpott)', center=(0,0.,0), range=1.8, background=color.white, width=800, height=800)

# Define frame that rotates coordinate system to make:
#  x coming out of screen
#  y rightward
#  z vertically upward,
f = frame(axis=(0,0,1))
f.rotate(angle=-pi/2)

# The following pedestal setup code borrows from Bruce Sherwoods gyro2.py example program

# Define pedestal to be a vertical rod along z with its top at the origin
origin = vector(0,0,0)
hpedestal = 1.
wpedestal = 0.1
pedestal = box(frame=f, pos=origin-vector(0,0,hpedestal/2.),
                 height=wpedestal, length=wpedestal, width=hpedestal,
                 color=color.yellow)

# Define base for pedestal
tbase = 0.05
wbase = 3.*wpedestal
base = box(frame=f, pos=origin-vector(0,0,hpedestal+tbase/2.),
                 height=wbase, length=wbase, width=tbase,
                 color=pedestal.color)

# Define mass & initial position of ball at end of massless rod
M = 1.
phi = -pi/8
theta = pi/3
lenrod = 1.
posball = lenrod*vector(cos(phi)*sin(theta),sin(phi)*sin(theta),cos(theta))
rrod = 0.01
rball = 0.35
Icm = 0.4*M*rball**2
rod = cylinder(frame=f, pos=origin, axis=posball, radius=rrod, color=color.blue,
                 material=materials.rough)
ball = sphere(frame=f, pos=posball, radius=rball, color=color.red)

# Define force of gravity
g = 9.8
Fgrav = vector(0,0,-M*g)

# Define parameters that determine initial angular velocity of ball:
# - Spin about rod (psidot)
# - Precession about z axis (phidot)
# - Nutation along polar angle theta direction (thetadot)
psidot = 250.
#phidot = 0.5
phidot = 0.803226
phidot = 0
phidot = 2.0
thetadot = 0.

# Compute initial angular velocity of ball in cartesian coordinates
omegax0 = psidot*cos(phi)*sin(theta) - thetadot*sin(phi)
omegay0 = psidot*sin(phi)*sin(theta) + thetadot*cos(phi)
omegaz0 = psidot*cos(theta) + phidot
omega = array([[omegax0],[omegay0],[omegaz0]])

# Compute initial inertia tensor from initial position of ball
x = posball.x
y = posball.y
z = posball.z
Ixx = Icm + M*(y**2+z**2)
Ixy = -M*x*y
Ixz = -M*x*z
Iyx = Ixy
Iyy = Icm + M*(x**2+z**2)
Iyz = -M*y*z
Izx = Ixz
Izy = Iyz
Izz = Icm + M*(x**2+y**2)
I = array([[Ixx,Ixy,Ixz],[Iyx,Iyy,Iyz],[Izx,Izy,Izz]])

# Compute current angular momentum from inertia tensor and angular velocity
L = I.dot(omega)

# Define trail for outermost point of ball
trail = curve(frame=f, radius=0.002, color=color.green)

# Define markers near the outermost point of ball to show spin about rod
rhat = norm(posball)
zhat = vector(0,0,1)
perpuv = norm(cross(rhat,zhat))
posmarker1 = posball+rball*(0.999*rhat+0.04471*perpuv)
posmarker2 = posball+rball*(0.999*rhat-0.04471*perpuv)
marker1= points(frame=f, pos=posmarker1, color=color.yellow)
marker2= points(frame=f, pos=posmarker2, color=color.cyan)

# Set up display of angular velocity and momentum vectors with bases at outermost point of ball
omegavector = arrow(frame=f, pos=posball+rball*rhat, axis=0.13*norm(omega), shaftwidth=0.01, color=color.magenta)
Lvector = arrow(frame=f, pos=posball+rball*rhat, axis=0.20*norm(L), shaftwidth=0.01, color=color.green)
                
# Time step 
deltat = 0.000005
t = 0.
Nsteps = 300 # number of calculational steps between graphics updates

while t<8.:
    rate(1000000000000000)
    for step in range(Nsteps): # multiple calculation steps for accuracy
        #print('posball=',posball)
        # Update translational velocities of ball and markers (to be filled in)
        ballv = cross(omega,posball)
        marker1v = cross(omega,posmarker1)
        marker2v = cross(omega,posmarker2)

        # Update positions of ball and marker (to be filled in - use 2nd-order approximation in deltat**2 for better accuracy)
        posball = posball + cross(omega,posball)*deltat + 0.5*cross(omega,cross(omega,posball))*deltat**2
        posmarker1 = posmarker1 + cross(omega,posmarker1)*deltat + 0.5*cross(omega,cross(omega,posmarker1))*deltat**2
        posmarker2 = posmarker2 + cross(omega,posmarker2)*deltat + 0.5*cross(omega,cross(omega,posmarker2))*deltat**2

        # Compute current inertia tensor from current position of ball (to be filled in)
        x = posball.x
        y = posball.y
        z = posball.z
        Ixx = Icm + M*(y**2+z**2)
        Ixy = -M*x*y
        Ixz = -M*x*z
        Iyx = Ixy
        Iyy = Icm + M*(x**2+z**2)
        Iyz = -M*y*z
        Izx = Ixz
        Izy = Iyz
        Izz = Icm + M*(x**2+y**2)
        I = array([[Ixx,Ixy,Ixz],[Iyx,Iyy,Iyz],[Izx,Izy,Izz]])
        

        # Compute torque on ball (to be filled in)
        torque = cross(posball,Fgrav)
        torquearray = array([[torque.x], [torque.y], [torque.z]])
        
        # Update angular momentum according to torque (to be filled in)
        L = L + torquearray*deltat

        # Update angular velocity from new angular momentum (to be filled in)
        Iinv = invert(I)
        omega = Iinv.dot(L)
       
    # Update animation objects:
    ball.pos = posball
    marker1.pos = posmarker1
    marker2.pos = posmarker2
    rod.axis = posball
    trail.append(pos=ball.pos*(lenrod+rball)/lenrod)
    omegavector.pos = posball+rball*norm(posball)
    omegavector.axis = 0.13*norm(omega)
    Lvector.pos = posball+rball*norm(posball)
    Lvector.axis = 0.20*norm(L)

    t = t + deltat*Nsteps
#print('t=',t,', ball (x,y,z)=',ball.pos.x, ball.pos.y, ball.pos.z)

