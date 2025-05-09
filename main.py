import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (bullets, updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for bullet in bullets:
            for asteroid in asteroids:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()