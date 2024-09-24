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
typed_text = ""
celsius_clicked = False
fahrenheit_clicked = False

celsius_text = font.render("CELSIUS", True, BLACK)
fahrenheit_text = font.render("FAHRENHEIT", True, BLACK)
celsius_value_text = font.render("0", True, BLACK)
fahrenheit_value_text = font.render("0", True, BLACK)

num_unicode = []
for num in range(10):
    num_unicode.append(f"{num}")

quadrant_rect_list = [
    pygame.Rect((0, 0), (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)),
    pygame.Rect((DISPLAY_WIDTH // 2, 0), (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)),
    pygame.Rect((0, DISPLAY_HEIGHT // 2), (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)),
    pygame.Rect((DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2), (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)),
]


# Functions
def convert_temp(
        celsius: int = None,
        fahrenheit: int = None
) -> int:
    """
    Converts the tempeture of the given value to the opposite tempeture measure.

    Parameters:
        celsius (int): The tempeture in celsius measure. Defaults to None
        fahrenheit (int): The tempeture in fahrenheit measure. Defaults to None
    
    Returns:
        int: The converted tempeture.
    """
    # computes the conversion of fahrenheit to celsius and stores as variable
    if celsius == None: 
        celsius = (5 / 9) * (fahrenheit - 32)
        return celsius
    if fahrenheit == None:
        fahrenheit = (celsius * (9 / 5)) + 32
        return fahrenheit


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


def enter_temp_value(event) -> None:
    """
    Converts the tempeture of the given value to the opposite tempeture measure.

    Parameters:
        event (Event): Paramenter from the pygame method pygame.event.get() in the event loop.
    """
    global celsius_clicked, fahrenheit_clicked
    global typed_text, celsius_value_text, fahrenheit_value_text
    mouse_pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
            typed_text = ""
            if celsius_clicked or fahrenheit_clicked:
                    celsius_clicked = False
                    fahrenheit_clicked = False
            elif quadrant_rect_list[1].collidepoint(mouse_pos):
                if not celsius_clicked:
                    celsius_clicked = True
            elif quadrant_rect_list[3].collidepoint(mouse_pos):
                if not fahrenheit_clicked:
                    fahrenheit_clicked = True
                
    if celsius_clicked:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]
            elif event.key == pygame.K_RETURN:
                celsius_value_text = font.render(typed_text, True, BLACK)
                fahrenheit_value_text = font.render(str(convert_temp(celsius=int(typed_text))), True, BLACK)

                celsius_clicked = False
                fahrenheit_clicked = False
            elif event.unicode in num_unicode:
                typed_text += event.unicode
    
    if fahrenheit_clicked:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]
            elif event.key == pygame.K_RETURN:
                fahrenheit_value_text = font.render(typed_text, True, BLACK)
                celsius_value_text = font.render(str(convert_temp(fahrenheit=int(typed_text))), True, BLACK)

                celsius_clicked = False
                fahrenheit_clicked = False
            elif event.unicode in num_unicode:
                typed_text += event.unicode


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

        enter_temp_value(event)
        


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