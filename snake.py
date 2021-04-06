# 4/6: 20 min reading manuals and beginning setup
# 4/6: 1 hr creating a sprite and trying to get it to move

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

    # Define moving function
    def move(self, key_pressed):
        if key_pressed[K_UP]:
            self.rect.move_ip(0, 5)
        if key_pressed[K_DOWN]:
            self.rect.move_ip(0, -5)
        if key_pressed[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if key_pressed[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Screen dimensions
screen_width = 500
screen_height = 500

# Initialize
pygame.init()

# Create snake
snake = Snake()

# Create display screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    # Set key pressed
    key_pressed = pygame.key.get_pressed()

    # Move snake
    snake.move(key_pressed)

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw snake
    screen.blit(snake.surf, (screen_width/2, screen_height/2))

    # Update display
    pygame.display.flip()
