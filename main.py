import pygame
import math
from Planet import Planet
# pygame setup
WIDTH = 1280
HEIGHT = 720
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")

    # RENDER YOUR GAME HERE

    
    sun = Planet("Sun",60,500,0,0,0,(255,100,0))
    earth = Planet("Earth",15,100,100,100,0,(0,100,200))
    xOffset = WIDTH/2
    yOffset = HEIGHT/2
    sun.isSun = True
    planets = [sun,earth]
    for planet in planets:
        pygame.draw.circle(screen,planet.color,(planet.x+xOffset,planet.y+yOffset),planet.radius)
        planet.calculatePosition(sun)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()