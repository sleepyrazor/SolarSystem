import pygame
import math



class Planet:
    G = 6.674 * math.pow(10, -11) 
    AU = 1.496 * pow(10,8) # km

    
    def __init__(self, name, mass,distanceToSun,color):
        self.name = name
        self.radius = 10 
        self.mass = mass /Planet.AU
        self.distanceToSun = distanceToSun
        self.isSun = False
        self.x = math.sqrt(distanceToSun**2/2)*PIXELAU
        self.y = math.sqrt(distanceToSun**2/2)*PIXELAU
        self.color = color

        #V2.0
        self.xvel = 0
        self.yvel = 1

    
    def isSun(self, status):
        self.isSun = status

    
    

    def attraction(self, p: 'Planet' ):
        ax = p.x - self.x
        ay = p.y - self.y
        distance = math.sqrt(ax**2 + ay**2)

        if distance != 0:
            # Fuerza y ángulo
            force = (Planet.G * self.mass * p.mass) / distance**2
            angle = math.atan2(ay, ax)

            # Componentes de la fuerza en x e y
            fx = math.cos(angle) * force
            fy = math.sin(angle) * force

            # Aceleración en x e y
            ax = fx / self.mass
            ay = fy / self.mass

            # Actualización de velocidad
            self.xvel += ax
            self.yvel += ay

            # Actualización de posición
            self.x += self.xvel
            self.y += self.yvel

def dibujarPlaneta(screen, p: 'Planet'):
    WIDTH = 1280
    HEIGHT = 720
    xOffset = WIDTH/2
    yOffset = HEIGHT/2
    if( (p.x+xOffset) < WIDTH and (p.y+yOffset) < HEIGHT):
        posicionTexto = (p.x+xOffset, p.y+yOffset+40)
        #print(str(p.x)+", y:"+str(p.y)+str(posicionTexto) + " " + str(p.name)+ " " + str(round(p.xvel)))
        font = pygame.font.Font(None, 40)
        text_surface = font.render(str(round(p.xvel)), True, (255,255,255))
        text_rect = text_surface.get_rect()
        text_rect.center = posicionTexto 
        screen.blit(text_surface, text_rect)
        pygame.draw.circle(screen,planet.color,(planet.x+xOffset,planet.y+yOffset),planet.radius)
    
    
# pygame setup
WIDTH = 1280
HEIGHT = 720
TIMESTEP = 3600 * 24 # 1 DAY PER SEC
pygame.display.set_caption("PYVERSE by sleepyrazor")
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
gravityForce = 0.0000000005
PIXELAU = 150
#planet =   name,   mass,     distanceToSun,x,y,color):
sun = Planet("Sun", 3.955* 10**30 *gravityForce,0, 'yellow')
sun.isSun = True
earth = Planet("Earth",5.972 * 10 **24 *gravityForce, 1, 'blue')
mars = Planet("Mars", 6.39* 10 **23*gravityForce, 1.52, 'red')
mercury = Planet("Mercury", 3.285* 10 **23*gravityForce, 0.39, 'gray')
venus = Planet("Venus", 4.867* 10 **24*gravityForce, 0.72, 'orange')


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0, 0, 0)) #pa nodejar rastros xd
    xOffset = WIDTH/2
    yOffset = HEIGHT/2
    planets = [sun, earth,mars,mercury,venus]
    for planet in planets:
        if planet.isSun == False:
            for p2 in planets:
                if p2 != planet:
                    planet.attraction(p2)
            #planet.attraction(sun)
           

        
        dibujarPlaneta(screen,planet)
        #pygame.draw.circle(screen,planet.color,(planet.x+xOffset,planet.y+yOffset),planet.radius)
        

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


    
