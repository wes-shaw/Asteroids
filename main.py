import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        
        for shot in shots:
            if asteroid.collisioncheck(shot):
                asteroid.split()
                shot.kill()

        for asteroid in asteroids:
            if asteroid.collisioncheck(player):
                print("Game over!")
                sys.exit()   
        
        screen.fill("black")
        for drawers in drawable:
            drawers.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000       

if __name__ == "__main__":
    main()