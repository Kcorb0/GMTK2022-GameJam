# GMTK Game Jam Lets go
# Theme: Roll the dice

import sys, pygame
import scripts.asset_tools as asset_tools

pygame.init()

# Window Settings
TITLE = "Twisted"
WIDTH, HEIGHT = 960, 540
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
asset_scale = 1080 // HEIGHT


# Colours
dark_red = [153, 0, 0]

# Load Assets
chip_white = pygame.image.load("assets\chips\chip_white.png")
chip_blue = pygame.image.load("assets\chips\chip_blue.png")
chip_purple = pygame.image.load("assets\chips\chip_purple.png")
chip_red = pygame.image.load("assets\chips\chip_red.png")
chip_black = pygame.image.load("assets\chips\chip_black.png")
dice_d6 = pygame.image.load("assets\dice\d6\d6_front.png")

dice_d6_scaled = asset_tools.scale_asset(dice_d6, asset_scale)
chip_purple_scaled = asset_tools.scale_asset(chip_purple, asset_scale)


def draw_chips(remaining_health):
    return None


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Draw assets to screen object
    SCREEN.fill(dark_red)
    SCREEN.blit(dice_d6_scaled, dice_d6_scaled.get_rect())

    # Refresh the display
    pygame.display.flip()
