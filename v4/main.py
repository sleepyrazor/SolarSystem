import pygame
import math

pygame.init()

WIDTH,HEIGHT = 1280,720
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PYVERSE v0.4 by sleepyrazor")

FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
    AU = 1.495978707e11 # AU in meters
    G = 6.67408e-11 # Gravitational constant
    SCALE = 250 / AU # 1 pixel = 250 meters
    def __init__(self,  mass, x, y, radius, color):
        self.mass = mass
        self.x = x
        self.y = y
        self.xvel = 0
        self.yvel = 0
        self.radius = radius
        self.color = color
        self.isSun = False

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def calcForce(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        dist = math.sqrt(dx**2 + dy**2)
        force = self.G * self.mass * other.mass / dist**2
        angle = math.atan2(dy, dx)
        fx = force * math.cos(angle)
        fy = force * math.sin(angle)
        return fx, fy
    
    def calcAccel(self, fx, fy):
        ax = fx / self.mass
        ay = fy / self.mass
        return ax, ay
    
    def update(self, timestep, planets):
        if not self.isSun:
            fx, fy = 0, 0
            for planet in planets:
                if planet != self:
                    fx1, fy1 = self.calcForce(planet)
                    fx += fx1
                    fy += fy1
            ax, ay = self.calcAccel(fx, fy)
            self.xvel += ax * timestep
            self.yvel += ay * timestep
            self.x += self.xvel * timestep
            self.y += self.yvel * timestep
       
def main():
    running = True
    clock = pygame.time.Clock()

    sun = Planet(1.989e30, 0, 0, 33, (255, 255, 0))
    sun.isSun = True

    mercury = Planet(3.285e23, 0, -0.387 * Planet.AU, 6, (100, 150, 100))
    #earth = Planet(5.972e24, 0, 1 * Planet.AU, 10, (100, 150, 255))

    planets = [sun, mercury]


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        WIN.fill((0, 0, 0))  # Clear the screen
        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 frames per second

    pygame.quit()
        
main()