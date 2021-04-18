# 4/6: (45 min) Having problems installing pygame + setting up
# 4/6: (1.5 hrs) Finished initial background and uploading future images
# 4/11: (4 hrs) Creating Sprite and obstacles
#        Sprite: falls automatically and goes back up w/ user input
#        obstacle: pipes are created and move across the screen
# 4/16: (3.5 hrs): Collision detection
# 4/16: (2 hrs): End/restart game and score/high score
# 4/18: (1.5 hrs): Trying to troubleshoot esc + quit w/ arcade
# 4/18: (15 min): fixing esc

import pygame
import random

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("chalkboard", 40)
end_font = pygame.font.SysFont("chalkboard", 20)


# Game variables
gravity = 0.18  # Makes bird drop
bird_movement = 0  # Makes bird fly
game_running = True  # Variable to make entire game loop run
end = False  # Variable to make end loop to run --> allows player to return to arcade
score = 0
high_score = 0

# Score/High score/End prompt
def display_score(game):
    if game == 'main':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(216, 75))
        screen.blit(score_surface, score_rect)
    if game == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(216, 75))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(216, 125))
        screen.blit(high_score_surface, high_score_rect)

        end_prompt_surface = end_font.render('Press escape to go back to arcade', True, (255, 255, 255))
        end_prompt_rect = end_prompt_surface.get_rect(center=(216, 425))
        screen.blit(end_prompt_surface, end_prompt_rect)


def new_record(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

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
bird = pygame.image.load('images/fb.images/yellowbird-midflap.png').convert_alpha()
bird = pygame.transform.scale(bird, (45, 45))
bird_rect = bird.get_rect(center=(100, 384))

# Bird rotation
def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 2, 1)
    return new_bird

#### PIPES ####
pipe_surface = pygame.image.load('images/fb.images/pipe-green.png').convert()
pipe_surface = pygame.transform.scale(pipe_surface, (75, 600))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
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
        # bottom pipe
        if pipe.bottom >= 768:
            screen.blit(pipe_surface, pipe)
        # top pipe
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

#### Check for collisions ####
def check_collision(pipes):
    for pipe in pipes:
        # hit pipe
        if bird_rect.colliderect(pipe):
            return False
    # hit top or bottom of screen
    if bird_rect.top <= -50 or bird_rect.bottom >= 650:
        return False
    return True


#### Game Loop ####
while True:
    for event in pygame.event.get():
        # Force quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            game_running = False
        # Key press
        if event.type == pygame.KEYDOWN:
            # Key press to quit game
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                game_running = False
            # Key press for bird movement
            if event.key == pygame.K_SPACE and game_running:
                bird_movement = 0
                bird_movement -= 5
            # Key press to restart game
            if event.key == pygame.K_RETURN and game_running == False:
                game_running = True
                pipe_list.clear()
                bird_rect.center = (100, 384)
                bird_movement = 0
                score = 0

        # Creates pipes
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    # background
    screen.blit(background, (0, 0))

    # only display bird/pipes/score if game is running
    if game_running:
        # bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_running = check_collision(pipe_list)

        # pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # score
        score += 0.0062
        display_score('main')

        # floor
        floor_x_pos += -1
        draw_floor()
        if floor_x_pos <= -432:
            floor_x_pos = 0
    else:
        floor = pygame.image.load('images/fb.images/base.png').convert()
        floor = pygame.transform.scale(floor, (432, 150))
        draw_floor()
        high_score = new_record(score, high_score)
        display_score('game_over')

    pygame.display.update()
    # base rate speed of the game
    clock.tick(120)




# Quit pygame
# pygame.quit()
