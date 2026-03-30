import pygame
from shot import Shot
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x, y, radius)
       self.rotation = 0
       self.shoot_cooldown_timer = 0
       self.velocity = pygame.Vector2(0, 0)
       self.invulnerable_timer = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        color = "yellow" if self.invulnerable_timer > 0 else "white"
        pygame.draw.polygon(surface=screen, color=color, points=self.triangle(), width=LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.accelerate(1, dt)

        if keys[pygame.K_s]:
            self.accelerate(-1, dt)

        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown_timer <= 0:
                self.shoot()
                self.shoot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

        if self.shoot_cooldown_timer > 0:
            self.shoot_cooldown_timer -= dt

        self.position += self.velocity * dt
        self.velocity *= PLAYER_FRICTION
        self.wrap_position()

        if self.invulnerable_timer > 0:
            self.invulnerable_timer -= dt

    def accelerate(self, direction, dt):
        unit_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += unit_vector * PLAYER_ACCELERATION * direction * dt
        if self.velocity.length() > PLAYER_SPEED:
            self.velocity.scale_to_length(PLAYER_SPEED)

    def reset(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.invulnerable_timer = 1.5

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        shot_velocity = rotated_vector * PLAYER_SHOOT_SPEED
        return Shot(self.position.x, self.position.y, shot_velocity)
