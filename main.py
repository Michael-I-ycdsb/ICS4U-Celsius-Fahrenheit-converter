"""
File: main.py
Author: Michael Iacobelli
Date: 2024-09-16
Description: gets a temperature from user input in Fahrenheit,
             then outputs the equivalent value in Celsius.
"""

import pygame
import sys

from pygame.math import Vector2 as vec

# Initialize Pygame
pygame.init()

# Set up the display
DISPLAY_WIDTH, DISPLAY_HEIGHT = (1280 // 3), (800 // 2)
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Celsius Fahrenheit Converter")

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize more variables and states below
thermometer_image = pygame.image.load("assets/thermometer.png")


# Functions
def get_temp() -> None:
    # gets fahrenheit input from user
    fahrenheit = float(input('User input in Fahrenheit: '))

    # computes the conversion of fahrenheit to celsius and stores as variable
    celsius = (5 / 9) * (fahrenheit - 32)

    # prints a f-string so that I don't have to concatanate 
    # I learned this on my own outside the course
    print(f'This is your temperature in celsius: {celsius}')


def event_loop() -> None:
    """
    Deals with quiting the game.

    Parameters:
        None
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def draw() -> None:
    """
    Draws all objects onto the display at its position.

    Parameters:
        None
    """
    display.fill(WHITE)
    display.blit(thermometer_image, (0,0))


# Define main loop
clock = pygame.time.Clock()  # Initialize clock object to cap frame rate

while True:
    # Handle events
    event_loop()

    # Update game state

    # Draw graphics and output
    draw()

    # Update display
    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 30 fps