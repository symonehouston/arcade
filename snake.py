# 4/6: 20 min reading manuals and beginning setup
        #Getting started: https://realpython.com/pygame-a-primer/
# 4/6: 2 hr creating a sprite and getting movement
# 4/9: 1 hr getting constant movement and ending game for hit edge

import pygame

# Import for ability to use keyboard keys
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)

# Class for snake
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super(Snake, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # Define constant moving function
    def constant_move(self, x_direction, y_direction):
        milliseconds = pygame.time.get_ticks()
        if milliseconds % 100 == 0:
            self.rect.move_ip(x_direction, y_direction)

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

# Screen dimensions
screen_width = 500
screen_height = 500

# Initialize
pygame.init()

# Create snake
snake = Snake()

# Create display screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set initial direction to the right
x_direction = 5
y_direction = 0

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Quit if snake is off screen
    if not snake.on_screen():
        running = False

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # Change direction according to key pressed
            key_pressed = pygame.key.get_pressed()
            x_direction, y_direction = snake.move(key_pressed)

            # Check for ESC key press
            if event.key == K_ESCAPE:
                running = False

        # Check for QUIT event
        elif event.type == QUIT:
            running = False

    # Get constant movement
    snake.constant_move(x_direction, y_direction)

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw snake
    screen.blit(snake.surf, snake.rect)

    # Update display
    pygame.display.flip()
