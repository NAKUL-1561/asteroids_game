import pygame
from constants import LINE_WIDTH, SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=(self.position.x, self.position.y), radius=self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        self.wrap_position()
