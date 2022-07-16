# GMTK Game Jam Lets go
# Theme: Roll the dice

import sys, pygame
import scripts.asset_tools as asset_tools
import scripts.generate_grid as generate_grid
from objects.dice_enemy import DiceEnemy
from objects.tower import Tower

pygame.init()

# Window Settings
pygame.display.set_caption("Twisted")
WIDTH, HEIGHT = 960, 540
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
asset_scale = 2

# Colours
BLACK = [20, 20, 20]
WHITE = (255, 255, 255)

# Load Assets
background = asset_tools.scale_asset(
    pygame.image.load("assets/background.png"), asset_scale
)
chip_panel = asset_tools.scale_asset(
    pygame.image.load("assets/chip_panel.png"), asset_scale
)
spawn_portal = asset_tools.scale_asset(
    pygame.image.load("assets/spawn_portal.png"), asset_scale
)
# Chips
chip_white = asset_tools.scale_asset(
    pygame.image.load("assets\chips\chip_white.png"), asset_scale
)
chip_blue = asset_tools.scale_asset(
    pygame.image.load("assets\chips\chip_blue.png"), asset_scale
)
chip_purple = asset_tools.scale_asset(
    pygame.image.load("assets\chips\chip_purple.png"), asset_scale
)
chip_red = asset_tools.scale_asset(
    pygame.image.load("assets\chips\chip_red.png"), asset_scale
)
chip_black = asset_tools.scale_asset(
    pygame.image.load("assets\chips\chip_black.png"), asset_scale
)

# Dice
dice_d6 = asset_tools.scale_asset(
    pygame.image.load("assets\dice\d6\d6_front.png"), asset_scale
)

# Chips
path_vert = asset_tools.scale_asset(
    pygame.image.load("assets\paths\path_vert.png"), asset_scale
)
path_hoz = asset_tools.scale_asset(
    pygame.image.load("assets\paths\path_hoz.png"), asset_scale
)
path_angle1 = asset_tools.scale_asset(
    pygame.image.load("assets\paths\path_angle1.png"), asset_scale
)
path_angle2 = asset_tools.scale_asset(
    pygame.image.load("assets\paths\path_angle2.png"), asset_scale
)
path_angle3 = asset_tools.scale_asset(
    pygame.image.load("assets\paths\path_angle3.png"), asset_scale
)
path_angle4 = asset_tools.scale_asset(
    pygame.image.load("assets\paths\path_angle4.png"), asset_scale
)


def draw_chips(remaining_chips, scale):
    chip_gap = 3 * scale
    chip_height = 230 * scale
    left_padding = 10

    for x in range(remaining_chips):

        if x <= 15:
            SCREEN.blit(chip_white, (left_padding, chip_height))
        elif x <= 30:
            SCREEN.blit(chip_purple, (left_padding, chip_height))
        elif x <= 40:
            SCREEN.blit(chip_blue, (left_padding, chip_height))
        elif x <= 50:
            SCREEN.blit(chip_red, (left_padding, chip_height))
        else:
            SCREEN.blit(chip_black, (left_padding, chip_height))

        chip_height -= chip_gap


def draw_grid_path(grid, scale):
    block_size = 18 * scale
    height = 270 * scale
    width = 396 * scale
    left_gap = 36 * scale

    for idxr, row in enumerate(range(0, height, block_size)):
        for idxc, col in enumerate(range(left_gap, width + left_gap, block_size)):
            if grid[idxr][idxc] == 1:
                coords = (col, row)
                path_type = get_path(grid, idxr, idxc)
                SCREEN.blit(path_type, coords)


def get_path(grid, idxr, idxc):

    if grid[idxr - 1][idxc] == 1 and grid[idxr + 1][idxc] == 1:  # Check vertical
        return path_vert
    elif grid[idxr][idxc - 1] == 1 and grid[idxr][idxc + 1] == 1:  # Check horizontal
        return path_hoz
    # Check angles
    elif grid[idxr][idxc + 1] == 1 and grid[idxr + 1][idxc] == 1:
        return path_angle2
    elif grid[idxr][idxc - 1] == 1 and grid[idxr - 1][idxc] == 1:
        return path_angle3
    elif grid[idxr][idxc + 1] == 1 and grid[idxr - 1][idxc] == 1:
        return path_angle4
    elif grid[idxr][idxc - 1] == 1 and grid[idxr + 1][idxc] == 1:
        return path_angle1


def draw_background():
    SCREEN.fill(BLACK)
    SCREEN.blit(background, (0, 0))
    SCREEN.blit(chip_panel, (0, 0))
    draw_grid_path(generate_grid.sample_grid, asset_scale)


def start_game(waves):

    run = True
    remaining_chips = 69

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                remaining_chips -= 1

        # Draw assets to screen object
        draw_background()
        draw_chips(remaining_chips, asset_scale)

        # Refresh the display
        pygame.display.flip()


if __name__ == "__main__":
    start_game(waves=10)
