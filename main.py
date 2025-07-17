import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shots import *


def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    asteroid_field = AsteroidField()
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
           for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                          return                
           dt = game_clock.tick(60) / 1000
           updatable.update(dt)
           for asteroid in asteroids:
                 if player1.collision(asteroid):
                       print("Game over!")
                       pygame.QUIT
                       return
           screen.fill("black")
           for sprite in drawable:
                 sprite.draw(screen)
           pygame.display.flip()



            
if __name__ == "__main__":
    main()
