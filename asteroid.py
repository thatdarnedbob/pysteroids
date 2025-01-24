import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            left_new_angle = self.velocity.rotate(-new_angle)
            right_new_angle = self.velocity.rotate(new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            left_rock = Asteroid(self.position.x,
                                 self.position.y,
                                 new_radius)
            
            right_rock = Asteroid(self.position.x,
                                 self.position.y,
                                 new_radius)
            
            left_rock.velocity = left_new_angle * 1.2
            right_rock.velocity = right_new_angle * 1.2