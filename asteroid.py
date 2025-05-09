import pygame
from circleshape import *
from constants import *
import random
angle = random.uniform(20, 50)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(surface, "white", center, int(self.radius), 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        left_vector = self.velocity.rotate(random_angle)
        right_vector = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_radius = self.radius - ASTEROID_MIN_RADIUS


        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = left_vector * 1.2  


        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = right_vector * 1.2