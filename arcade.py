# 4/17: 3 hrs all coding main arcade screen

# IMPORTS ##########
import pygame
import os
from pygame.locals import *


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

# Set-up font
arc_font = pygame.font.SysFont(None, 40)

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

'''
print(score)
import pickle
score_dict = {}
score_dict['snake'] = score
pickle.dump(score_dict, open( "score_dict.p", "wb" ) )
#to open with pickle
#favorite_color = pickle.load( open( "save.p", "rb" ) )
'''
