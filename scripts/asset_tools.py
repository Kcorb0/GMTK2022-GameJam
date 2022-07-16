import sys, pygame


def scale_asset(asset, asset_scale):

    asset_width = asset.get_width() * asset_scale
    asset_height = asset.get_height() * asset_scale
    scaled_asset = pygame.transform.scale(asset, (asset_width, asset_height))

    return scaled_asset
