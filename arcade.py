# 4/17: 3 hrs all coding main arcade screen
# 4/18: 3 hrs all coding, working on high score and details
# 4/21: 1 hr all coding, trying to fix high score 

# IMPORTS ##########
import pygame
import os
import pickle
from pygame.locals import *

# LOAD HIGH SCORES FROM HIGH SCORE DICTIONARY ##########
# Load dictionary
score_dict = pickle.load(open("score_dict.p", "rb"))

# Save high scores
tetris_high_score = score_dict['tetris']
flappybird_high_score = score_dict['flappybird']
snake_high_score = score_dict['snake']


# CLASSES ##########
# Class for background
class Background(pygame.sprite.Sprite):
    # Initialize
    def __init__(self):
        super(Background, self).__init__()
        self.img_load = pygame.image.load(os.path.join('images', 'arcade.jpeg'))
        self.surf = pygame.transform.scale2x(self.img_load)
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = (0, 0)


# SET-UP ##########

# Initialize sounds
pygame.mixer.init()

# Initialize
pygame.init()

# Screen dimensions
arc_screen_width = 718
arc_screen_height = 958

# Create display screen
arc_screen = pygame.display.set_mode((arc_screen_width, arc_screen_height))

# Set-up fonts
arc_font = pygame.font.SysFont(None, 40)
arc_font_small = pygame.font.SysFont(None, 18)

# Set-up sound
# https://freesound.org/people/BloodPixel/sounds/489557/
pygame.mixer.music.load(os.path.join('sounds', 'arcade.wav'))
pygame.mixer.music.play(loops=-1)
# https://freesound.org/people/ProjectsU012/sounds/341695/
button_sound = pygame.mixer.Sound(os.path.join('sounds', 'button.wav'))

# Create background
arc_bg = Background()

# Create variable for running main loop
arcade_running = True

# MAIN LOOP ##########
while arcade_running:
    # Write high scores as strings
    hs_strings = 'TETRIS HIGH SCORE: ' + str(tetris_high_score) + \
                 '  FLAPPYBIRD HIGH SCORE: ' + str(flappybird_high_score) + \
                 '  SNAKE HIGH SCORE: ' + str(snake_high_score)

    # Event for loop
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # Check what key is pressed
            if event.key == K_1:
                pygame.mixer.music.pause()
                button_sound.play()
                file = open('tetris.py')
                read = file.read()
                exec(read)
                file.close()
                tetris_high_score = int(tetris_high_score)
                pygame.mixer.music.unpause()

                # Reset display size
                arc_screen = pygame.display.set_mode((arc_screen_width, arc_screen_height))

            if event.key == K_2:
                pygame.mixer.music.pause()
                button_sound.play()
                file = open('flappybird.py')
                read = file.read()
                exec(read)
                file.close()
                flappybird_high_score = int(flappybird_high_score)
                pygame.mixer.music.unpause()

                # Reset display size
                arc_screen = pygame.display.set_mode((arc_screen_width, arc_screen_height))

            if event.key == K_3:
                pygame.mixer.music.pause()
                button_sound.play()
                file = open('snake.py')
                read = file.read()
                exec(read)
                file.close()
                snake_high_score = int(snake_high_score)
                pygame.mixer.music.unpause()

                # Reset display size
                arc_screen = pygame.display.set_mode((arc_screen_width, arc_screen_height))

            # Check for ESC key press
            # if event.key == K_BACKSPACE:
            # arcade_running = False

        # Check for QUIT event
        elif event.type == QUIT:
            arcade_running = False

    # Fill the screen with black and display background
    arc_screen.fill((0, 0, 0))
    arc_screen.blit(arc_bg.surf, arc_bg.rect)

    # Display text
    high_scores_text = arc_font_small.render(hs_strings, True, (255, 0, 0))
    arc_screen.blit(high_scores_text, (arc_screen_width / 2 - high_scores_text.get_rect().width / 2,
                               arc_screen_height / 3 - 4 * high_scores_text.get_rect().height))

    arc_text = arc_font.render('WELCOME', True, (255, 255, 255))
    arc_screen.blit(arc_text, (arc_screen_width / 2 - arc_text.get_rect().width / 2,
                               arc_screen_height / 2 - 2 * arc_text.get_rect().height))

    text2 = arc_font.render('Press 1 to play Tetris', True, (255, 255, 255))
    arc_screen.blit(text2, (arc_screen_width / 2 - text2.get_rect().width / 2,
                            arc_screen_height / 2 - 2 * text2.get_rect().height + arc_text.get_rect().height))

    text3 = arc_font.render('Press 2 to play Flappy Bird', True, (255, 255, 255))
    arc_screen.blit(text3, (arc_screen_width / 2 - text3.get_rect().width / 2,
                            arc_screen_height / 2 - 2 * text3.get_rect().height + 2 * arc_text.get_rect().height))

    text4 = arc_font.render('Press 3 to play Snake', True, (255, 255, 255))
    arc_screen.blit(text4, (arc_screen_width / 2 - text4.get_rect().width / 2,
                            arc_screen_height / 2 - 2 * text4.get_rect().height + 3 * arc_text.get_rect().height))

    # Update display
    pygame.display.flip()

# Stop sounds
pygame.mixer.music.stop()
pygame.mixer.quit()

# Put new high scores in dictionary
score_dict['tetris'] = tetris_high_score
score_dict['flappybird'] = flappybird_high_score
score_dict['snake'] = snake_high_score

# Write over score_dict with new high scores
pickle.dump(score_dict, open("score_dict.p", "wb"))
