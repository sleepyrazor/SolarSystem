import pygame
import math
from Planet import Planet


def dibujarPlaneta(screen, p: 'Planet'):
    WIDTH = 1280
    HEIGHT = 720
    xOffset = WIDTH/2
    yOffset = HEIGHT/2
    font = pygame.font.Font(None, 40)
    text_surface = font.render(str(round(p.xvel)), True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.center = (p.x+xOffset, p.y+yOffset+40)
    screen.blit(text_surface, text_rect)
    pygame.draw.circle(screen,planet.color,(planet.x+xOffset,planet.y+yOffset),planet.radius)
    
    
# pygame setup
WIDTH = 1280
HEIGHT = 720
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
refactor = 1
gravityForce = 0.000000000000000005
#planet =   name,      radius,             mass,     distanceToSun,x,y,color):
sun = Planet("Sun", 69.6340 * refactor, 3.955* math.pow(10, 30)*gravityForce, 0, 0, 'yellow')
sun.isSun = True
# 5.97 * math.pow(10, 24)
earth = Planet("Earth", 22.389* refactor, 5.972*math.pow(10,24)*gravityForce, 300, 40, 'blue')
# 6.39 * math.pow(10, 23),
mars = Planet("Mars", 9.389 * refactor, 6.39*math.pow(10,23)*gravityForce, 150, 20, 'red')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")

    # RENDER YOUR GAME HERE

    screen.fill((0, 0, 0)) #pa nodejar rastros xd
    
    xOffset = WIDTH/2
    yOffset = HEIGHT/2
    sun.isSun = True
    planets = [sun, earth,mars]
    for planet in planets:
        if planet.isSun == False:
            
            planet.calculatePosition(sun)
           

        
        dibujarPlaneta(screen,planet)
        #pygame.draw.circle(screen,planet.color,(planet.x+xOffset,planet.y+yOffset),planet.radius)
        

    # flip() the display to put your work on screen
    pygame.display.update()

    clock.tick(30)  # limits FPS to 60

pygame.quit()


    
