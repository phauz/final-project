import pygame
import os
from src.platforms import Platform
import src.main
class Level():
    # create child classes for each level
    
    # list of sprites of all levels
    
    platform_list = None
    enemy_list = None
    
    background = None
    
    world_shift = 0
    level_shift = -1000
    
    def __init__(self, player):
        # adding constuctor for the player
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        
    # update everything on the level
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        
    def draw(self, win):
        # draws everything on this level
        
        # don't shift the background to add depths 
        
        win.fill((176, 224, 230))
        win.blit(self.background,(self.world_shift // 3, 0))
        
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
            
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(os.path.join("images/backgrounds", "startingMenu.png")).convert()
        self.background.set_colorkey(255, 255 ,255)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [Platform.LONG_GRASS, 0, 1545],
                  [Platform.VERTICAL_GRASS, 1561, 0]]
        
        # Go through the array above and add platforms
        for platform in level:
            block = Platform.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)