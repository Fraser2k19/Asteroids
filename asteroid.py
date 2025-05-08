import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(surface, "white", center, int(self.radius), 2)

    