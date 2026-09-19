import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x:float, y:float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0
        self.shoot_cooldown = 0.0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(surface=screen, color=PLAYER_COLOR, points=self.triangle(), width=LINE_WIDTH)

    def rotate(self, dt:float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        self.shoot_cooldown -= dt

    def move(self, dt:float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self, dt:float):
        if self.shoot_cooldown <= 0:
            new_shot = Shot(self.position[0], self.position[1])

            shot_velocity = pygame.Vector2(0, 1)
            shot_velocity = shot_velocity.rotate(self.rotation)
            shot_velocity = shot_velocity * SHOT_SPEED * dt

            new_shot.velocity = shot_velocity

            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
