import math

class Planet:
    G = 6.674 * math.pow(10, -11) 
    AU = 1.496 * pow(10,8) # km

    
    def __init__(self, name, radius, mass,x,y,color):
        self.name = name
        self.radius = radius
        self.mass = mass / self.AU
        self.distanceToSun = 0 
        self.isSun = False
        self.x = x
        self.y = y
        self.color = color

        #V2.0
        self.xvel = 0
        self.yvel = 2

    
    def isSun(self, status):
        self.isSun = status

    def attraction(self, p: 'Planet' ):
        
        ax = p.x - self.x
        ay = p.y - self.y
        if ax != 0 or ay != 0:
            self.distanceToSun = math.sqrt(pow(ax,2)+pow(ay,2)) 
            
        else:
            self.distanceToSun = 0
            print(self.distanceToSun)
        
        if self.distanceToSun!= 0:
            f = (Planet.G*self.mass * p.mass)/pow(self.distanceToSun,2) 
            angle = math.atan2(ay, ax) #el 2 es para tener en cuenta el angulo 0
            fx = math.cos(angle)*f
            fy = math.sin(angle)*f
            # f = mass * aceleration
            ax = fx/self.mass * self.TIMESTEP
            ay = fy/self.mass
            self.xvel += ax
            self.yvel += ay
            self.x += self.xvel+(0.5*ax)
            self.y += self.yvel+(0.5*ay) 
