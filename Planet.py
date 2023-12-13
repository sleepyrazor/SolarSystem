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
        print(self.name)
        ax = p.x - self.x
        ay = p.y - self.y
        if ax != 0 or ay != 0:
            distanceBetween = math.sqrt(pow(ax,2)+pow(ay,2)) 
            
        else:
            distanceBetween = 0
            print(distanceBetween)
        
        
        f = (Planet.G*self.mass * p.mass)/pow(distanceBetween,2) 
        angle = math.atan2(ay, ax) #el 2 es para tener en cuenta el angulo 0
        fx = math.cos(angle)*f
        fy = math.sin(angle)*f
        print("fx:"+str(fx))
        print("fy:"+str(fy))
        self.x += fx * pow(10,8)
        self.y += fy * pow(10,8) 