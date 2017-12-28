
from visual import *
from math import *

# Program mode:
# 1 - Simulate Earth's circular motion
# 2 - Simulate Halley's Comet's elliptical motion
# 3 - Simulate Jupiter's and Halley's Comet's motion
mode = 3

# Constants common to all modes:

# Newton's constant:
G = 6.67e-11

# Sun mass
MSun = 1.99e30


# Initialization for Earth (mode 1):

if mode==1:

    # Earth's mass
    MEarth = 5.97e24

    # Distance from Sun to Earth
    DistEarthSun = 1.496037e11

    # Initial position of Earth
    PosEarth = vector(DistEarthSun,0,0)

    # Compute speed required for pure circular motion
    SpeedEarth = pow(G*MSun/DistEarthSun,0.5)

    # Define Earth's initial velocity & momentum
    VelEarth = vector(0,SpeedEarth,0)
    MomEarth = MEarth*VelEarth

    # Define animation scene
    scene = display(background=color.white, title='Earth orbit (Alex Philpott)')

    # Scale factor to apply to distances for animation display:
    scalefactor = 1.e-11

    # Create Earth sphere and velocity unit vector arrow animation objects
    EarthSphereRadius = 0.05
    EarthSphere = sphere(pos=PosEarth*scalefactor, radius=EarthSphereRadius, color=color.blue, make_trail=True)
    ArrowLength = 3.0
    EarthVelVector = arrow(pos=EarthSphere.pos, axis=norm(VelEarth)*ArrowLength*EarthSphereRadius, color=color.blue)

    # Time step
    deltat = 100


# Initialization for Halley's Comet  (mode 2 or mode 3)

if mode==2 or mode==3:

    # Halley's mass
    MHalley = 2.2e14

    # Halley's initial distance from the Sun
    DistHalleySun = 8.79e10  
    PosHalley = vector(-DistHalleySun,0,0)

    # Halley's initial speed
    SpeedHalley = 54500

    # Define Halley's initial velocity & momentum
    VelHalley = vector(0,SpeedHalley,0)
    MomHalley = MHalley*VelHalley

    # Define animation scene
    if mode==2:
        scene = display(background=color.white, title='Halley orbit (Alex Philpott)')

        # Scale factor to apply to distances for animation display:
        scalefactor = 2.e-11

        # Create Halley sphere and velocity unit vector arrow animation objects
        HalleySphereRadius = .64
        HalleySphere = sphere(pos=PosHalley*scalefactor, radius=HalleySphereRadius, color=color.green, make_trail=True)

        ArrowLength = 3.0
        HalleyVelVector = arrow(pos=HalleySphere.pos, axis=norm(VelHalley)*ArrowLength*HalleySphereRadius, color=color.green)

    # Time step
    deltat = 4000


# Initialization for Jupiter (mode 3):

if mode==3:

    # Jupiter's mass
    MJupiter = 1.8986e27

    # Distance from Sun to Jupiter
    DistJupiterSun = 7.78e11

    # Initial position of Jupiter with phase angle w.r.t. x-axis
    phi = 3.6*pi/180.
    PosJupiter = vector(DistJupiterSun*cos(phi),DistJupiterSun*sin(phi),0)

    # Compute speed required for pure circular motion
    SpeedJupiter = sqrt(G*MSun/DistJupiterSun)

    # Define Jupiter's initial velocity and momentum
    VelJupiter = vector(-SpeedJupiter*sin(phi),SpeedJupiter*cos(phi),0)
    MomJupiter = MJupiter*VelJupiter

    # Define animation scene
    scene = display(background=color.white, title='Jupiter and Halley orbit (Alex Philpott)')

    # Scale factor to apply to distances for animation display:
    scalefactor = 3.e-12

    # Create Jupiter sphere and velocity unit vector arrow animation objects
    JupiterSphereRadius = 0.05
    JupiterSphere = sphere(pos=PosJupiter*scalefactor, radius=JupiterSphereRadius, color=color.blue, make_trail=True)
    ArrowLength = 3.0
    JupiterVelVector = arrow(pos=JupiterSphere.pos, axis=norm(VelJupiter)*ArrowLength*JupiterSphereRadius, color=color.blue)

    # Create Halley sphere and velocity unit vector arrow animation objects
    HalleySphereRadius = .05
    HalleySphere = sphere(pos=PosHalley*scalefactor, radius=HalleySphereRadius, color=color.green, make_trail=True)
 
    ArrowLength = 3.0
    HalleyVelVector = arrow(pos=HalleySphere.pos, axis=norm(VelHalley)*ArrowLength*HalleySphereRadius, color=color.green)

    # Time step
    deltat = 500

    #vector of positions
    JHVector = arrow(pos=JupiterSphere.pos, axis=norm(-PosJupiter+PosHalley)*ArrowLength*JupiterSphereRadius, color=color.yellow)

# Define Sun sphere for display                                                                                                                                     
SunSphereRadius = 0.08
if mode==2:
    SunSphereRadius *= 8
SunSphere = sphere(pos=vector(0,0,0), radius=SunSphereRadius, color=color.red)

# Initialize time
t = 0

if mode==1:

    # Initialize variable to keep track of 1 orbit
    notdone = True
    firsty = PosEarth.y
    lasty = firsty
    
    # Loop over time
    while notdone:

        rate(100000)

        # Update position of Earth
        PosEarth = PosEarth + VelEarth*deltat

        # Compute gravitational force on Earth from Sun
        Fgrav = -G*MSun*MEarth/mag2(PosEarth)*norm(PosEarth)

        # Update momentum of Earth
        MomEarth = MomEarth+Fgrav*deltat

        # Update velocity of Earth
        VelEarth = MomEarth/MEarth

        # Update display of sphere representing the Earth
        EarthSphere.pos = PosEarth*scalefactor

        # Update display of arrow representing the Earth's velocity
        EarthVelVector.pos = EarthSphere.pos
        EarthVelVector.axis = norm(VelEarth)*ArrowLength*EarthSphereRadius

        # Orbit is completed if y on last step was less than first value and current y is greater than it
        if lasty-firsty<0 and PosEarth.y>firsty:
            print('Completed one orbit at t=',t,' seconds')
            notdone = False
            ndays = t / 86400.
            EarthSphere.label = label(pos=EarthSphere.pos, text='T = %6.2f days' % ndays, color=color.black, xoffset=-1., yoffset=0)
        lasty = PosEarth.y

        t = t + deltat
 

if mode==2:

    # Initialize variable to keep track of 1 orbit
    notdone = True
    firsty = PosHalley.y
    lasty = firsty

    while notdone:

        rate(100000)

        # Update position of Halley
        PosHalley = PosHalley + VelHalley*deltat

        # Compute gravitational force on Halley from Sun
        Fgrav = -G*MSun*MHalley/mag2(PosHalley)*norm(PosHalley)

        # Update momentum of Halley
        MomHalley = MomHalley+Fgrav*deltat

        # Update velocity of Halley
        VelHalley = MomHalley/MHalley

        # Update display of sphere representing Halley
        HalleySphere.pos = PosHalley*scalefactor

        # Update display of arrow representing Halley's velocity
        HalleyVelVector.pos = HalleySphere.pos
        HalleyVelVector.axis = norm(VelHalley)*ArrowLength*HalleySphereRadius

        # Orbit is completed if y on last step was less than first value and current y is greater than it
        if lasty-firsty<0 and PosHalley.y>firsty:
            print('Completed one orbit at t=',t,' seconds')
            notdone = False
            ndays = t / 86400.
            nyears = ndays/365.25
            HalleySphere.label = label(pos=HalleySphere.pos, text='T = %6.2f years' % nyears, color=color.black, xoffset=-1., yoffset=0)
        lasty = PosHalley.y


        t = t + deltat

if mode==3:

    # Initialize variable to keep track of 1 orbit
    notdone = True
    firsty = PosJupiter.y
    lasty = firsty

    while notdone:

        rate(100000)

        # Update position of Jupiter
        PosJupiter = PosJupiter + VelJupiter*deltat
        
        # Update position of Halley
        PosHalley = PosHalley + VelHalley*deltat

        #Update dist b/w Halley and Jupiter
        PosJH = PosJupiter-PosHalley
        #print(PosJH)

        # Compute gravitational force on Jupiter from Sun
        FgravJ = -G*MSun*MJupiter/mag2(PosJupiter)*norm(PosJupiter)

        # Compute gravitational force on Halley from Sun
        FgravH = -G*MSun*MHalley/mag2(PosHalley)*norm(PosHalley)

        # Compute gravitational force on Jupiter from Halley
        FgravJH = -G*MJupiter*MHalley/mag2(PosJH)*norm(PosJH)

        # Compute gravitational force on Halley from Jupiter
        FgravHJ = -FgravJH
        #print(mag(FgravHJ))
        
        #Total force on Halley
        FgravTH = FgravHJ + FgravH

        #Total force on Jupiter
        FgravTJ = FgravJ + FgravJH

        # Update momentum of Jupiter
        MomJupiter = MomJupiter + FgravTJ*deltat

        # Update momentum of Halley
        MomHalley = MomHalley + FgravTH*deltat

        # Update velocity of Jupiter
        VelJupiter = MomJupiter/MJupiter

        # Update velocity of Halley
        VelHalley = MomHalley/MHalley

        # Update display of sphere representing the Jupiter
        JupiterSphere.pos = PosJupiter*scalefactor

        # Update display of arrow representing the Jupiter's velocity
        JupiterVelVector.pos = JupiterSphere.pos
        JupiterVelVector.axis = norm(VelJupiter)*ArrowLength*JupiterSphereRadius

        # Update display of sphere representing Halley
        HalleySphere.pos = PosHalley*scalefactor

        # Update display of arrow representing Halley's velocity
        HalleyVelVector.pos = HalleySphere.pos
        HalleyVelVector.axis = norm(VelHalley)*ArrowLength*HalleySphereRadius

        #updating position vector
        JHVector.pos = JupiterSphere.pos
        JHVector.axis = norm(PosJupiter-PosHalley)*ArrowLength*JupiterSphereRadius
        
        # Orbit is completed if y on last step was less than first value and current y is greater than it
        if lasty-firsty<0 and PosJupiter.y>firsty:
            notdone = False

        t = t + deltat

 
