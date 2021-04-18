# 4/6: 20 min reading manuals and beginning setup
# Getting started: https://realpython.com/pygame-a-primer/
# 4/6: 2 hr creating a sprite and getting movement
# 4/9: 1 hr getting constant movement and ending game for hit edge
# 4/10: 20 min playing around with end game screen
# 4/15: 1 hr 20 min creating food; currently unable to remove food after collision
# 4/15: 1 hr getting food collision and appearance to work
# 4/15: 1 hr attempting snake addition
# 4/16: 30 in gathertown and working on snake body addition
# 4/16: 1 hr still working on snake body addition
# 4/17: 30 min calculating and displaying score
# 4/17: 2 hrs SNAKE BODY WORKING WOOHOO (thanks Abby on gathertown); tyring to get collisions to work
# 4/17: 30 min snake body collision is working decently
# 4/17: 30 min starting to get different snake skins
# 4/17: 1 hr more work on skins and opening screen
# 4/17: 30 min finished skin
# 4/17: 2 hrs getting background options, corresponding foods, etc.
# 4/17: 1 hr how-to screen, fix esc and quit, incorporate high score
# 4/18: 1 hr 30 min sound incorporation
# 4/18: 30 min playing and fixing wrong key bug
# 4/18: 30 min fixed fish image and added space bg option

# IMPORTS ##############################

import pygame
import random
import os

# Import for ability to use keyboard keys
from pygame.locals import *

# END IMPORTS ##############################
############################################


# FIND HIGH SCORE ##############################
snake_high_score = 0  # change this to dictionary snake_high_score later


# END FIND HIGH SCORE ##############################
####################################################


# DEFINE CLASSES ##############################

# Class for background
class Background(pygame.sprite.Sprite):
    # Initialize
    def __init__(self):
        super(Background, self).__init__()
        self.surf = pygame.image.load(os.path.join('images', background))
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = (0, 0)


# Class for snake
class Snake(pygame.sprite.Sprite):
    # Initialize
    def __init__(self):
        super(Snake, self).__init__()
        self.surf = pygame.image.load(os.path.join('images', snake_skin))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Define constant moving function
    def constant_move(self, x_direction, y_direction):
        milliseconds = pygame.time.get_ticks()
        if milliseconds % 25 == 0:
            self.rect.move_ip(x_direction, y_direction)
            moved_position = self.rect
            return moved_position
        else:
            return None

    # Define moving function
    def move(self, key_pressed):
        if key_pressed[K_UP]:
            x_direction = 0
            y_direction = -5
        if key_pressed[K_DOWN]:
            x_direction = 0
            y_direction = 5
        if key_pressed[K_LEFT]:
            x_direction = -5
            y_direction = 0
        if key_pressed[K_RIGHT]:
            x_direction = 5
            y_direction = 0
        return x_direction, y_direction

    # Define function to check if snake is on screen
    def on_screen(self):
        truth = True
        if self.rect.left < 0:
            truth = False
        elif self.rect.right > screen_width:
            truth = False
        elif self.rect.top < 0:
            truth = False
        elif self.rect.bottom > screen_height:
            truth = False
        return truth


# Class for food
class Food(pygame.sprite.Sprite):
    # Initialize
    def __init__(self):
        super(Food, self).__init__()
        self.surf = pygame.image.load(os.path.join('images', food_img))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(random.randint(25, screen_width - 25),
                    random.randint(25, screen_height - 25)))


# END DEFINE CLASSES ##############################
###################################################


# SET-UP DISPLAY ##############################

# Initialize sounds
pygame.mixer.init()

# Initialize
pygame.init()

# Screen dimensions
screen_width = 500
screen_height = 500

# Create display screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set-up font
font = pygame.font.SysFont("comicsansms", 24)

# Set-up sound
# https://freesound.org/people/Kodack/sounds/258020/
food_sound = pygame.mixer.Sound(os.path.join('sounds', 'food.wav'))
# https://freesound.org/people/myfox14/sounds/382310/
collide_sound = pygame.mixer.Sound(os.path.join('sounds', 'collide.wav'))
# https://freesound.org/people/ProjectsU012/sounds/341695/
button_sound = pygame.mixer.Sound(os.path.join('sounds', 'button.wav'))

# Variable to keep opening skin screen running
open_running_skin = True

# Variable to keep opening background screen running
open_running_bg = True

# Variable to keep opening how-to screen running
open_running_how_to = True

# Variable to keep the main loop running
running = True

# END SET-UP DISPLAY ##############################
###################################################


# OPENING SCREEN ##############################

# Opening loop skin
while open_running_skin:
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Display text
    text = font.render('Press number to choose snake skin', True, (255, 255, 255))
    screen.blit(text, (screen_width / 2 - text.get_rect().width / 2,
                       screen_height / 2 - text.get_rect().height / 2))

    number_text = font.render('1 - green, 2 - coral, 3 - rattle, 4 - eel', True, (255, 255, 255))
    screen.blit(number_text, (screen_width / 2 - number_text.get_rect().width / 2,
                              screen_height / 2 - number_text.get_rect().height / 2 + text.get_rect().height))

    # Event for loop
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # Check what key is pressed
            if event.key == K_1:
                snake_skin = 'green.jpg'
                open_running_skin = False
                button_sound.play()

            if event.key == K_2:
                snake_skin = 'coral.png'
                open_running_skin = False
                button_sound.play()

            if event.key == K_3:
                snake_skin = 'rattle.png'
                open_running_skin = False
                button_sound.play()

            if event.key == K_4:
                snake_skin = 'eel.jpeg'
                open_running_skin = False
                button_sound.play()

            # Check for ESC key press
            if event.key == K_ESCAPE:
                snake_skin = 'green.jpg'
                background = 'dirt.jpeg'
                food_img = 'apple.png'
                open_running_skin = False
                open_running_bg = False
                open_running_how_to = False
                running = False

        # Check for QUIT event
        elif event.type == QUIT:
            snake_skin = 'green.jpg'
            background = 'dirt.jpeg'
            food_img = 'apple.png'
            open_running_skin = False
            open_running_bg = False
            open_running_how_to = False
            running = False

    # Update display
    pygame.display.flip()

# Opening loop background
while open_running_bg:
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Display text
    text = font.render('Press number to choose background', True, (255, 255, 255))
    screen.blit(text, (screen_width / 2 - text.get_rect().width / 2,
                       screen_height / 2 - text.get_rect().height / 2))

    number_text = font.render('1 - dirt, 2 - grass, 3 - water, 4 - space', True, (255, 255, 255))
    screen.blit(number_text, (screen_width / 2 - number_text.get_rect().width / 2,
                              screen_height / 2 - number_text.get_rect().height / 2 + text.get_rect().height))

    # Event for loop
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # Check what key is pressed
            if event.key == K_1:
                background = 'dirt.jpeg'
                food_img = 'apple.png'
                open_running_bg = False
                button_sound.play()

            if event.key == K_2:
                background = 'grass.jpeg'
                food_img = 'bug.png'
                open_running_bg = False
                button_sound.play()

            if event.key == K_3:
                background = 'water.jpeg'
                food_img = 'fish.png'
                open_running_bg = False
                button_sound.play()

            if event.key == K_4:
                background = 'space.jpeg'
                food_img = 'star.png'
                open_running_bg = False
                button_sound.play()

            # Check for ESC key press
            if event.key == K_ESCAPE:
                background = 'dirt.jpeg'
                food_img = 'apple.png'
                open_running_bg = False
                open_running_how_to = False
                running = False

        # Check for QUIT event
        elif event.type == QUIT:
            background = 'dirt.jpeg'
            food_img = 'apple.png'
            open_running_bg = False
            open_running_how_to = False
            running = False

    # Update display
    pygame.display.flip()

# Opening loop how-to
while open_running_how_to:
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Display text
    t1 = font.render('HOW TO PLAY', True, (255, 255, 255))
    screen.blit(t1, (screen_width / 2 - t1.get_rect().width / 2,
                     screen_height / 2 - 2 * t1.get_rect().height))

    t2 = font.render('- use keyboard arrows to move snake', True, (255, 255, 255))
    screen.blit(t2, (screen_width / 2 - t2.get_rect().width / 2,
                     screen_height / 2 - 2 * t2.get_rect().height + t1.get_rect().height))

    t3 = font.render('- collect food but do not hit self or edge', True, (255, 255, 255))
    screen.blit(t3, (screen_width / 2 - t3.get_rect().width / 2,
                     screen_height / 2 - 2 * t3.get_rect().height + 2 * t1.get_rect().height))

    t4 = font.render('PRESS SPACEBAR TO BEGIN', True, (255, 255, 255))
    screen.blit(t4, (screen_width / 2 - t4.get_rect().width / 2,
                     screen_height / 2 - 2 * t4.get_rect().height + 4 * t1.get_rect().height))

    # Event for loop
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # Check what key is pressed
            if event.key == K_SPACE:
                open_running_how_to = False
                button_sound.play()

            # Check for ESC key press
            if event.key == K_ESCAPE:
                open_running_how_to = False
                running = False

        # Check for QUIT event
        elif event.type == QUIT:
            open_running_how_to = False
            running = False

    # Update display
    pygame.display.flip()

# END OPENING SCREEN ##############################
###################################################

# SET-UP MAIN LOOP ##############################

# Create background
bg = Background()

# Create snake
snake = Snake()

# Create snake body group
body = pygame.sprite.Group()

# Create food group
foods = pygame.sprite.Group()

# Create food
food = Food()
foods.add(food)

# Set initial direction to the right
x_direction = 5
y_direction = 0

# Initialize position list
position_list = []

# Initialize score variable
snake_score = 0

# END SET-UP MAIN LOOP ##############################
#####################################################


# MAIN LOOP ##############################

while running:
    # Quit if snake is off screen
    if not snake.on_screen():
        running = False
        collide_sound.play()

    # Event for loop
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # Change direction according to key pressed
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_UP] or key_pressed[pygame.K_DOWN] \
                    or key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_LEFT]:
                x_direction, y_direction = snake.move(key_pressed)

            # Check for ESC key press
            if event.key == K_ESCAPE:
                running = False

        # Check for QUIT event
        elif event.type == QUIT:
            running = False

    # Fill the screen with black and display background
    screen.fill((0, 0, 0))
    screen.blit(bg.surf, bg.rect)

    # Get snake constant movement and get new position
    moved_position = snake.constant_move(x_direction, y_direction)

    # Append new position to position list
    if moved_position is not None:
        position_list.append((moved_position[0], moved_position[1]))

    # Keep position list at max length 100
    if len(position_list) >= 1000:
        position_list = position_list[-1000:]

    # Check for food collisions
    if pygame.sprite.spritecollideany(snake, foods):
        for item in foods:
            # Remove food
            foods.remove(item)

            # Increase score by one
            snake_score += 1
            food_sound.play()

            # Add new food
            new_food = Food()
            foods.add(new_food)

            # Add on snake body
            snake_body = Snake()
            body.add(snake_body)

    # Draw snake head
    screen.blit(snake.surf, snake.rect)

    # Draw snake body and check for collision with head
    i = 1
    for item in body:
        # Draw snake body
        screen.blit(item.surf, position_list[-5 * i - 1])

        # Collision detection
        x_pos = position_list[-5 * i - 1][0]
        y_pos = position_list[-5 * i - 1][1]
        head_x = position_list[-1][0]
        head_y = position_list[-1][1]
        for z in range(7, 18):
            if ((head_x + z) in list(range(x_pos + 7, x_pos + 18))) and \
                    ((head_y + z) in list(range(y_pos + 7, y_pos + 18))):
                running = False
                collide_sound.play()

        # Update i
        i += 1

    # Draw food
    for item in foods:
        screen.blit(item.surf, item.rect)

    # Update foods
    foods.update()

    # Update display
    pygame.display.flip()

# END MAIN LOOP ##############################
##############################################


# FINAL SCREEN ##############################

# New high score if player beats current high score
if snake_score > snake_high_score:
    snake_high_score = snake_score

# Make score into string
string_score = "Score: " + str(snake_score)

# Make high score into string
string_hs = "High Score: " + str(snake_high_score)

# End screen loop
end = False
while not end:
    # Fill screen grey
    screen.fill((0, 0, 0))

    # Define and display text
    text = font.render('GAME OVER', True, (255, 0, 0))
    screen.blit(text, (screen_width / 2 - (text.get_rect().width) / 2,
                       screen_height / 2 - (text.get_rect().height) / 2))

    number_text = font.render(string_score, True, (255, 0, 0))
    screen.blit(number_text, (screen_width / 2 - number_text.get_rect().width / 2,
                              screen_height / 2 - number_text.get_rect().height / 2 + text.get_rect().height))

    hs_text = font.render(string_hs, True, (255, 0, 0))
    screen.blit(hs_text, (screen_width / 2 - hs_text.get_rect().width / 2,
                          screen_height / 2 - hs_text.get_rect().height / 2 + 2 * text.get_rect().height))

    # Update display
    pygame.display.flip()

    # Wait 5 seconds then end
    pygame.time.delay(5000)
    end = True

# END FINAL SCREEN ##############################
#################################################
