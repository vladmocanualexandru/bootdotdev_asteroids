import pygame
from constants import SHOT_RADIUS, SHOT_COLOR, SHOT_SPEED, LINE_WIDTH
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            surface=screen,
            color=SHOT_COLOR,
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * SHOT_SPEED * dt
