import pygame, os
import main


class SpriteSheet(object):
    # class used to grab images of out a sprite sheet
    sprite_sheet = None
    
    def __init__(self, file_name):
        # pass in the file of the sprite sheet
        
        self.sprite_sheet = pygame.image.load(file_name).convert()
        
    def get_image(self, frame, width, height, scale):
        # getting images out of a large spread sheet
        # pass in the x, y cords and the width/height of the sprite
        
        # make a new blank image
        image = pygame.Surface([width, height]).convert()
        
        # copying the sprite from the image
        image.blit(self.sprite_sheet, (0, 0), ((frame * width), 0, (width, height)))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(0, 0, 0) # removing black around the image
        
        return image
    
    def get_background(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(constants.BLACK)

        # Return the image
        return image
