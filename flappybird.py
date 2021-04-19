# 4/6: (45 min) Having problems installing pygame + setting up
# 4/6: (1.5 hrs) Finished initial background and uploading future images
# 4/11: (4 hrs) Creating Sprite and obstacles
#        Sprite: falls automatically and goes back up w/ user input
#        obstacle: pipes are created and move across the screen
# 4/16: (3.5 hrs): Collision detection
# 4/16: (2 hrs): End/restart game and score/high score
# 4/18: (1.5 hrs): Trying to troubleshoot esc + quit w/ arcade
# 4/18: (15 min): fixing esc
# 4/18: (30 min): FIXED THE ESCAPE BUTTON
# 4/18: (2 hrs): Loaded different birds and background
# 4/18: (15 min): Part of group programming; fixing variables to work with main game
# 4/18: (10 min): Part of group programming; fixing variables to work with main game
# 4/18: (1 hr): Trying (and failing) to figure out time delays
# 4/18: (2 hrs): Adding bird flap animation
# 4/19: (1 hr): Added pause screen before first game, but can't figure out how to implement before replaying
#               Centered text


# Imports
import pygame as pygame
import random
import pickle

# Initialize game
pygame.init()
screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("chalkboard", 40)
prompt_font = pygame.font.SysFont("chalkboard", 20)

# Game variables
gravity = 0.18  # Makes bird drop
bird_movement = 0  # Makes bird fly
game_running = True  # Variable to make entire game loop run
open_background = True  # Variable to keep opening background running
open_bird = True  # Variable to keep opening bird running
open_pipe = True  # Variable to keep opening pipe running
pause_start = True  # Variable to create a pause to start screen running
flappybird_score = 0  # Game Score
score_dict = pickle.load(open('score_dict.p', 'rb'))  # Score dictionary
flappybird_high_score = score_dict['flappybird']  # High score


#### SCORE/PROMPTS ####
# Score/High score/End prompt
def display_score(game):
    if game == 'main':
        # Score
        score_surface = game_font.render(str(int(flappybird_score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(216, 75))
        screen.blit(score_surface, score_rect)

    if game == 'game_over':
        # Score
        score_surface = game_font.render(f'Score: {int(flappybird_score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(216, 75))
        screen.blit(score_surface, score_rect)

        # High Score
        high_score_surface = game_font.render(f'High Score: {int(flappybird_high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(216, 125))
        screen.blit(high_score_surface, high_score_rect)

        # Escape to arcade
        end_prompt_surface = prompt_font.render('Press escape to go back to arcade', True, (255, 255, 255))
        end_prompt_rect = end_prompt_surface.get_rect(center=(216, 425))
        screen.blit(end_prompt_surface, end_prompt_rect)

        # Replay Game
        replay_surface = prompt_font.render('Press return to replay', True, (255, 255, 255))
        replay_rect = replay_surface.get_rect(center=(216, 375))
        screen.blit(replay_surface, replay_rect)


# Save + update High Score
def new_record(flappybird_score, flappybird_high_score):
    if flappybird_score > flappybird_high_score:
        flappybird_high_score = flappybird_score
    return flappybird_high_score


#### BACKGROUND ####

# Initial background
background = pygame.image.load('images/fb.images/background-day.png').convert()
background = pygame.transform.scale(background, (432, 768))
screen_width = 432
screen_height = 768

floor = pygame.image.load('images/fb.images/base.png').convert()
floor = pygame.transform.scale(floor, (432, 150))
floor_x_pos = 0


# Floor
def draw_floor():
    screen.blit(floor, (floor_x_pos, 650))
    screen.blit(floor, (floor_x_pos + 432, 650))


#### BIRD ####
# Bird rotation
def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 2, 1)
    return new_bird


# Bird animation
def bird_flap():
    new_bird = bird_animation[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect


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


#### Opening Background Loop ####
while open_background:
    # Initial Background
    screen.blit(background, (0, 0))
    floor = pygame.image.load('images/fb.images/base.png').convert()
    floor = pygame.transform.scale(floor, (432, 150))
    draw_floor()

    # Display text
    text = prompt_font.render('Press number to choose background', True, (255, 255, 255))
    screen.blit(text, [screen_width / 2 - text.get_rect().width / 2, 75])

    number_text = prompt_font.render('1 - day, 2 - night', True, (255, 255, 255))
    number_text_rect = text.get_rect(center=(216, 125))
    screen.blit(number_text, [screen_width / 2 - number_text.get_rect().width / 2, 125])

    # Event for loop
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:

            # Check what key is pressed
            if event.key == pygame.K_1:
                # Day background
                background = pygame.image.load('images/fb.images/background-day.png').convert()
                background = pygame.transform.scale(background, (432, 768))
                open_background = False
                # button_sound.play()

            if event.key == pygame.K_2:
                # Red Pipe
                background = pygame.image.load('images/fb.images/background-night.png').convert()
                background = pygame.transform.scale(background, (432, 768))
                open_background = False
                # button_sound.play()

            # Check for ESC key press
            if event.key == pygame.K_ESCAPE:
                open_background = False
                open_bird = False
                open_pipe = False
                pause_start = False
                game_running = False

        # Check for QUIT event
        if event.type == pygame.QUIT:
            open_background = False
            open_bird = False
            open_pipe = False
            pause_start = False
            game_running = False

    # Update display
    pygame.display.flip()

#### Opening Bird Loop ####
while open_bird:
    # Background
    screen.blit(background, (0, 0))
    floor = pygame.image.load('images/fb.images/base.png').convert()
    floor = pygame.transform.scale(floor, (432, 150))
    draw_floor()

    # Display text
    text = prompt_font.render('Press number to choose bird', True, (255, 255, 255))
    screen.blit(text, [screen_width / 2 - text.get_rect().width / 2, 75])


    number_text = prompt_font.render('1 - yellow, 2 - blue, 3 - red', True, (255, 255, 255))
    screen.blit(number_text, [screen_width / 2 - number_text.get_rect().width / 2, 125])


    # Event for loop
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:

            # Check what key is pressed
            if event.key == pygame.K_1:
                # Yellow bird
                bird_down = pygame.image.load('images/fb.images/yellowbird-downflap.png').convert_alpha()
                bird_down = pygame.transform.scale(bird_down, (45, 45))
                bird_mid = pygame.image.load('images/fb.images/yellowbird-midflap.png').convert_alpha()
                bird_mid = pygame.transform.scale(bird_mid, (45, 45))
                bird_up = pygame.image.load('images/fb.images/yellowbird-upflap.png').convert_alpha()
                bird_up = pygame.transform.scale(bird_up, (45, 45))
                bird_animation = [bird_down, bird_mid, bird_up]
                bird_index = 0
                bird = bird_animation[bird_index]
                bird_rect = bird.get_rect(center=(100, 384))

                BIRDFLAP = pygame.USEREVENT + 1
                pygame.time.set_timer(BIRDFLAP, 200)

                open_bird = False
                # button_sound.play()

            if event.key == pygame.K_2:
                # Blue Bird
                bird_down = pygame.image.load('images/fb.images/bluebird-downflap.png').convert_alpha()
                bird_down = pygame.transform.scale(bird_down, (45, 45))
                bird_mid = pygame.image.load('images/fb.images/bluebird-midflap.png').convert_alpha()
                bird_mid = pygame.transform.scale(bird_mid, (45, 45))
                bird_up = pygame.image.load('images/fb.images/bluebird-upflap.png').convert_alpha()
                bird_up = pygame.transform.scale(bird_up, (45, 45))
                bird_animation = [bird_down, bird_mid, bird_up]
                bird_index = 0
                bird = bird_animation[bird_index]
                bird_rect = bird.get_rect(center=(100, 384))

                BIRDFLAP = pygame.USEREVENT + 1
                pygame.time.set_timer(BIRDFLAP, 200)
                open_bird = False
                # button_sound.play()

            if event.key == pygame.K_3:
                bird_down = pygame.image.load('images/fb.images/redbird-downflap.png').convert_alpha()
                bird_down = pygame.transform.scale(bird_down, (45, 45))
                bird_mid = pygame.image.load('images/fb.images/redbird-midflap.png').convert_alpha()
                bird_mid = pygame.transform.scale(bird_mid, (45, 45))
                bird_up = pygame.image.load('images/fb.images/redbird-upflap.png').convert_alpha()
                bird_up = pygame.transform.scale(bird_up, (45, 45))
                bird_animation = [bird_down, bird_mid, bird_up]
                bird_index = 0
                bird = bird_animation[bird_index]
                bird_rect = bird.get_rect(center=(100, 384))

                BIRDFLAP = pygame.USEREVENT + 1
                pygame.time.set_timer(BIRDFLAP, 200)
                open_bird = False
                # button_sound.play()

            # Check for ESC key press
            if event.key == pygame.K_ESCAPE:
                open_background = False
                open_bird = False
                open_pipe = False
                pause_start = False
                game_running = False

        # Check for QUIT event
        if event.type == pygame.QUIT:
            open_background = False
            open_bird = False
            open_pipe = False
            pause_start = False
            game_running = False

    # Update display
    pygame.display.flip()

#### Opening Pipe Loop ####
while open_pipe:
    # Background
    screen.blit(background, (0, 0))
    floor = pygame.image.load('images/fb.images/base.png').convert()
    floor = pygame.transform.scale(floor, (432, 150))
    draw_floor()

    # Display text
    text = prompt_font.render('Press number to choose pipe color', True, (255, 255, 255))
    screen.blit(text, [screen_width / 2 - text.get_rect().width / 2, 75])


    number_text = prompt_font.render('1 - green, 2 - red', True, (255, 255, 255))
    screen.blit(number_text, [screen_width / 2 - number_text.get_rect().width / 2, 125])

    # Event for loop
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:

            # Check what key is pressed
            if event.key == pygame.K_1:
                # Green Pipe
                pipe_surface = pygame.image.load('images/fb.images/pipe-green.png').convert()
                pipe_surface = pygame.transform.scale(pipe_surface, (75, 600))
                open_pipe = False
                # button_sound.play()

            if event.key == pygame.K_2:
                # Red Pipe
                pipe_surface = pygame.image.load('images/fb.images/pipe-red.png').convert()
                pipe_surface = pygame.transform.scale(pipe_surface, (75, 600))
                open_pipe = False
                # button_sound.play()

            # Check for ESC key press
            if event.key == pygame.K_ESCAPE:
                open_background = False
                open_bird = False
                open_pipe = False
                pause_start = False
                game_running = False

        # Check for QUIT event
        if event.type == pygame.QUIT:
            open_background = False
            open_bird = False
            open_pipe = False
            pause_start = False
            game_running = False

    # Update display
    pygame.display.flip()

#### Pause Before Starting Loop ####
while pause_start:
    # Background
    screen.blit(background, (0, 0))
    floor = pygame.image.load('images/fb.images/base.png').convert()
    floor = pygame.transform.scale(floor, (432, 150))
    draw_floor()

    # Display text
    text = prompt_font.render('Get Ready', True, (255, 255, 255))
    screen.blit(text, [screen_width / 2 - text.get_rect().width / 2, 75])

    press_text = prompt_font.render('Press Space To Begin', True, (255, 255, 255))
    screen.blit(press_text, [screen_width / 2 - press_text.get_rect().width / 2, 125])

    # Event for loop
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:

            # Check what key is pressed
            if event.key == pygame.K_SPACE:
                # Space to Start
                pipe_surface = pygame.image.load('images/fb.images/pipe-green.png').convert()
                pipe_surface = pygame.transform.scale(pipe_surface, (75, 600))
                pause_start = False
                flappy_bird = True
                # button_sound.play()

            # Check for ESC key press
            if event.key == pygame.K_ESCAPE:
                open_background = False
                open_bird = False
                open_pipe = False
                pause_start = False
                game_running = False

        # Check for QUIT event
        if event.type == pygame.QUIT:
            open_background = False
            open_bird = False
            open_pipe = False
            pause_start = False
            game_running = False

    # Update display
    pygame.display.flip()

#### Game Loop ####
while flappy_bird:
    # background
    screen.blit(background, (0, 0))
    floor = pygame.image.load('images/fb.images/base.png').convert()
    floor = pygame.transform.scale(floor, (432, 150))

    for event in pygame.event.get():
        # Force quit game
        if event.type == pygame.QUIT:
            flappy_bird = False

        # Key press
        if event.type == pygame.KEYDOWN:
            # Key press to quit game
            if event.key == pygame.K_ESCAPE:
                flappy_bird = False
            # Key press for bird movement
            if event.key == pygame.K_SPACE and game_running:
                bird_movement = 0
                bird_movement -= 5
            # Key press to restart game
            if event.key == pygame.K_RETURN and game_running == False:
                pause_start = True
                game_running = True
                pipe_list.clear()
                bird_rect.center = (100, 384)
                bird_movement = 0
                flappybird_score = 0

        # Creates pipes
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

        # Bird animation
        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird, bird_rect = bird_flap()

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
        flappybird_score += 0.0062
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
        flappybird_high_score = new_record(flappybird_score, flappybird_high_score)
        display_score('game_over')

    pygame.display.update()
    # base rate speed of the game
    clock.tick(120)
