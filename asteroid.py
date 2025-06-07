import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        circle = pygame.draw.circle (screen, (255,0,0), self.position, self.radius, 2)
        return circle

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        asteroid.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID-MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2