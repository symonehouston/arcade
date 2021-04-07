# 4/6: (45 min) Having problems installing pygame + setting up
# 4/6: (1.5 hrs) Finished initial background and uploading future images
import pygame, sys

#Moving floor function
def draw_floor():
    screen.blit(floor, (floor_x_pos, 650))
    screen.blit(floor, (floor_x_pos + 432, 650))



# Initialize pygame
pygame.init()

screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()

# Initial background
background = pygame.image.load('images/fb.images/background-day.png').convert()
background = pygame.transform.scale(background, (432, 768))

floor = pygame.image.load('images/fb.images/base.png').convert()
floor = pygame.transform.scale(floor, (432, 150))
floor_x_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # shuts down code

    screen.blit(background, (0, 0))
    floor_x_pos += -1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0



    pygame.display.update()

    # base rate speed of the game
    clock.tick(120)

# Quit pygame
# pygame.quit()
