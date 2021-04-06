#4/6: (45 min) Having problems installing pygame + setting up

import pygame, sys


#Initialize pygame
pygame.init()

screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #shuts down code

    pygame.display.update()

    #baserate speed of the game
    clock.tick(120)





#Quit pygame
#pygame.quit()