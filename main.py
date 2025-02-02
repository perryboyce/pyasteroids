import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main_clock = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Update objs
        updatable.update(dt)

        #Check collisions
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()
        
        #Draw objs
        screen.fill((0, 0, 0))

        for thing in drawable:
            thing.draw(screen)       
        
        #Update display
        pygame.display.flip()
        dt = main_clock.tick(60) / 1000

if __name__ == "__main__":
    main()