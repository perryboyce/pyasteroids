from circleshape import *
from random import *
from constants import *

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
                random_angle = uniform(20, 50)

                new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
                new_asteroid1.velocity = self.velocity.rotate(random_angle) * ASTEROID_BREAK_VELOCITY_BOOST

                new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
                new_asteroid2.velocity = self.velocity.rotate(random_angle * -1) * ASTEROID_BREAK_VELOCITY_BOOST