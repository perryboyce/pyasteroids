from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.speed = PLAYER_SHOOT_SPEED
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        # forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # self.position += forward * self.speed * dt
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)