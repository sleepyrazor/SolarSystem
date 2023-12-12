import math

class Planet:
    G = pow(6.672,-11)
    def __init__(self, name, radius, mass, distanceToSun,x,y,color):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distanceToSun = distanceToSun
        self.isSun = False
        self.x = x
        self.y = y
        self.color = color

    
    def isSun(self, status):
        self.isSun = status

    def calculatePosition(self, p: 'Planet' ):
        ax = p.x - self.x
        ay = p.y - self.y
        if ax > 0 and ay > 0:
            distanceBetween = math.sqrt(pow(ax,2)+pow(ay,2)) 
        else:
            distanceBetween = 0
        
        if Planet.isSun == False:
            f = (Planet.G*self.mass * p.mass)/pow(distanceBetween,2)
            angle = math.atan(ay/ax)
            fx = math.cos(angle)*f
            fy = math.sin(angle)*f
            self.x = fx
            self.y = fy