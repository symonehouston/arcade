# 4/6: (45 min) Having problems installing pygame + setting up
# 4/6: (1.5 hrs) Finished initial background and uploading future images
# 4/11: (4 hrs) Creating Sprite and obstacles
#        Sprite: falls automatically and goes back up w/ user input
#        obstacle: pipes are created and move across the screen

import pygame
import sys
import random

# Initialize pygame
pygame.init()

screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()

# Game variables
gravity = 0.18
bird_movement = 0

#### BACKGROUND ####

# Initial background
background = pygame.image.load('images/fb.images/background-day.png').convert()
background = pygame.transform.scale(background, (432, 768))

floor = pygame.image.load('images/fb.images/base.png').convert()
floor = pygame.transform.scale(floor, (432, 150))
floor_x_pos = 0

def draw_floor():
    screen.blit(floor, (floor_x_pos, 650))
    screen.blit(floor, (floor_x_pos + 432, 650))


#### BIRD ####
bird = pygame.image.load('images/fb.images/yellowbird-midflap.png').convert()
bird = pygame.transform.scale(bird, (45, 45))
#bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center=(100, 384))


#### PIPES ####
pipe_surface = pygame.image.load('images/fb.images/pipe-green.png').convert()
pipe_surface = pygame.transform.scale(pipe_surface, (75, 600))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1300)
pipe_height = [300, 400, 500]


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(600, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(600, random_pipe_pos - 250))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 768:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

# Draw on the screen
while True:
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # shuts down code
        # Key press for bird movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 5
        # Creates pipes
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())


    # background
    screen.blit(background, (0, 0))

    # bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird, bird_rect)

    # pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # floor
    floor_x_pos += -1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0



    pygame.display.update()
    # base rate speed of the game
    clock.tick(120)

# Quit pygame
# pygame.quit()
