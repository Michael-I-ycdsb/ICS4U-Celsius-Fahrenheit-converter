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
DISPLAY_WIDTH, DISPLAY_HEIGHT = 500, 100
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Celsius Fahrenheit Converter")

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize more variables and states below
celsius = 0
font = pygame.Font("assets/text/Arial.ttf", 20)

celsius_text = font.render("CELSIUS", True, BLACK)
fahrenheit_text = font.render("FAHRENHEIT", True, BLACK)
celsius_value_text = font.render("0", True, BLACK)
fahrenheit_value_text = font.render("0", True, BLACK)

quadrant_rect_list = [
    pygame.Rect((0, 0), (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)),
    pygame.Rect((DISPLAY_WIDTH // 2, 0), (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)),
    pygame.Rect((0, DISPLAY_HEIGHT // 2), (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)),
    pygame.Rect((DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2), (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)),
]


# Functions
def get_temp() -> None:
    global celsius
    # gets fahrenheit input from user
    fahrenheit = float(input('User input in Fahrenheit: '))

    # computes the conversion of fahrenheit to celsius and stores as variable
    celsius = (5 / 9) * (fahrenheit - 32)

    # prints a f-string so that I don't have to concatanate 
    # I learned this on my own outside the course
    print(f'This is your temperature in celsius: {celsius}')


def draw_chart() -> None:
    """
    Draws the temperature chart.

    Parameters:
        None
    """
    for index, quadrant_rect in enumerate(quadrant_rect_list):
        pygame.draw.rect(display, BLACK, quadrant_rect, 1)

        if index == 0:
            display.blit(celsius_text, (quadrant_rect.centerx - celsius_text.get_width() / 2, quadrant_rect.centery - celsius_text.get_height() / 2))
        elif index == 1:
            display.blit(celsius_value_text, (quadrant_rect.centerx - celsius_value_text.get_width() / 2, quadrant_rect.centery - celsius_value_text.get_height() / 2))
        elif index == 2:
            display.blit(fahrenheit_text, (quadrant_rect.centerx - fahrenheit_text.get_width() / 2, quadrant_rect.centery - fahrenheit_text.get_height() / 2))
        else:
            display.blit(fahrenheit_value_text, (quadrant_rect.centerx - fahrenheit_value_text.get_width() / 2, quadrant_rect.centery - fahrenheit_value_text.get_height() / 2))


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

    draw_chart()


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