import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
        

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return self.position.distance_to(other.position) <= (self.radius + other.radius)