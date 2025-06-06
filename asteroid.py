import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        circle = pygame.draw.circle (screen, (255,0,0), self.position, self.radius, 2)
        return circle

    def update(self, dt):
        self.position += self.velocity * dt