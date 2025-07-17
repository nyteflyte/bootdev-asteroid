import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y):
        radius = SHOT_RADIUS
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    def update(self, dt):
        self.position += self.velocity * dt