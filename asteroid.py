from turtle import width

import pygame, random
from circleshape import CircleShape
from logger import log_event
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x:float, y:float, radius:float):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            surface=screen,
            color=ASTEROID_COLOR,
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            random_angle = random.uniform(20,50)
            new_asteroid1_velocity = self.velocity.rotate(random_angle) * 1.2
            new_asteroid2_velocity = self.velocity.rotate(-random_angle) * 1.2
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(x=self.position[0], y=self.position[1], radius=new_asteroid_radius)
            new_asteroid2 = Asteroid(x=self.position[0], y=self.position[1], radius=new_asteroid_radius)

            new_asteroid1.velocity = new_asteroid1_velocity
            new_asteroid2.velocity = new_asteroid2_velocity
