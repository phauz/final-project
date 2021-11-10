import pygame

from spritesheets import SpriteSheet

# defining platform locations

LONG_GRASS = (0, 1545, 2031, 503)
VERTICAL_GRASS = (1561, 0, 475, 1009)


class Platform(pygame.sprite.Sprite):
    
    def __init__(self, sprite_sheet):
        
        pygame.sprite.Sprite.__init__(self)
            
        sprite_sheet = SpriteSheet("mossy/Mossy Tileset", "Mossy-FloatingPlatforms.png")
        
        self.image = sprite_sheet.get_background(sprite_sheet[0], sprite_sheet[1],
                                            sprite_sheet[3], sprite_sheet[4],
                                            sprite_sheet[5])
        
        self.rect = self.image.get_rect()