import pygame
import math



AU = 1.496 * pow(10, 8)
PIXELAU = 250 
# pygame setup
WIDTH = 1280
HEIGHT = 720
xOffset = WIDTH/2
yOffset = HEIGHT/2
TIMESTEP = 1 * pow(10, -23)
pygame.display.set_caption("PYVERSE by sleepyrazor")
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

class Planeta:
    def __init__(self, nombre, masa, radio, color, x, y):
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.color = color
        self.distanciaSol = 0
        self.x = x
        self.y = y
        self.ax = 1000
        self.ay = 2
        self.xvel = 0
        self.yvel = 0

    def calcular_fuerza_gravitacional(self, sol):

        G = 6.67430 * pow(10, -11)
        dx = sol.x - self.x
        dy = sol.y - self.y
        self.distanciaSol = pow(dx**2 + dy**2, 0.5)
        fuerza = (G * self.masa * sol.masa) / pow(self.distanciaSol, 2)
        angulo = math.atan2(dy, dx)
        self.ax = fuerza * math.cos(angulo) / self.masa
        self.ay = fuerza * math.sin(angulo) / self.masa
        # Actualización de velocidad
        self.xvel += self.ax/2
        self.yvel += self.ay/2

        # Actualización de posición
        self.x += self.xvel
        self.y += self.yvel
    

    def actualizar_posicion(self, timestep):
        self.x += self.ax * timestep
        self.y += self.ay * timestep

    def __str__(self):
        return f"Planeta {self.nombre}: masa={self.masa}, radio={self.radio}, color={self.color}, distanciaSol={self.distanciaSol}, posición=({self.x}, {self.y}), aceleración=({self.ax}, {self.ay})"


def dibujarPlaneta(screen, planeta,scale):
    if (planeta.x < WIDTH and planeta.y < HEIGHT):
        pygame.draw.circle(screen, planeta.color, (planeta.x +
                           xOffset, planeta.y + yOffset), planeta.radio * scale)


def actualizar_posicion(planeta, timestep):
    planeta.calcular_fuerza_gravitacional(sun)
    planeta.actualizar_posicion(timestep)


scale = 1/18

sun = Planeta("Sol", 1.989 * pow(10, 30), (695510 * scale)/44 , (255, 255, 0), 0, 0)
earth = Planeta("Tierra", 5.972 * pow(10, 24), 6371 * scale, (0, 0, 255), 1 * PIXELAU, 100)
venus = Planeta("Venus", 4.867 * pow(10, 24), 6051 * scale, (255, 100, 0), 0.723 * PIXELAU, 200)
mars = Planeta("Marte", 6.39 * pow(10, 23), 3389 * scale, (255, 0, 0), 1.52 * PIXELAU, 150)
jupiter = Planeta("Jupiter", 1.898 * pow(10, 27), 69911 * scale/10, (255, 255, 255), 5.20 * PIXELAU, 300)

planets = [sun, earth,venus,mars,jupiter]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Rueda hacia arriba
                scale *= 8.5
                # Acción a realizar cuando se mueve la rueda hacia arriba
            elif event.button == 5:  # Rueda hacia abajo
                scale *= 0.5
                # Acción a realizar cuando se mueve la rueda hacia abajo

                
    screen.fill((0, 0, 0))  # pa nodejar rastros xd
    font = pygame.font.Font(None, 36)  # Fuente y tamaño del texto
    text = font.render(f"Scale: {scale}", True, (0, 0, 255))  # Renderizar el texto
    screen.blit(text, (10, 10))  # Mostrar el texto en la posición (10, 10) en la pantalla
    for planet in planets:

        dibujarPlaneta(screen, planet, scale)
        if planet != sun:
            actualizar_posicion(planet, TIMESTEP)
            print(planet)
            

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
