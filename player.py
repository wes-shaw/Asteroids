from circleshape import * 
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        polygon = pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(dt):
        return PLAYER_TURN_SPEED * dt
    
        def update(self, dt):
            keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            return keys.rotate(dt.reverse())
        if keys[pygame.K_d]:
            return keys.rotate(dt)