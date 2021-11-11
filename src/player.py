import pygame, os

from pygame import sprite
from main import main
from spritesheets import SpriteSheet
# calling file name 


class Player(pygame.sprite.Sprite):
    #setting player vectors
    change_x = 0
    change_y = 0
    
    #holding images for moving left and right
    running_l = []
    running_r = []
    
    #showing the direction
    direction = "R"
    
    # list of sprites we can bump against
    level = None
    
    # methods
    def __init__(self):
        # constuctor function
        
        
        # calling parent constructor
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheet("_Run.png")
        sprite_jump = SpriteSheet("_Jump.png")
        
        run = sprite_sheet.get_image(0, 120, 80, 2)
        self.running_r.append(run)
        run = sprite_sheet.get_image(1, 120, 80, 2)
        self.running_r.append(run)
        run = sprite_sheet.get_image(2, 120, 80, 2)
        self.running_r.append(run)
        run = sprite_sheet.get_image(3, 120, 80, 2)
        self.running_r.append(run)
        run = sprite_sheet.get_image(4, 120, 80, 2)
        self.running_r.append(run)
        run = sprite_sheet.get_image(5, 120, 80, 2)
        self.running_r.append(run)
        run = sprite_sheet.get_image(6, 120, 80, 2)
        self.running_r.append(run)
        run = sprite_sheet.get_image(7, 120, 80, 2)
        self.running_r.append(run)
        run = sprite_sheet.get_image(8, 120, 80, 2)
        self.running_r.append(run)
        run = sprite_sheet.get_image(9, 120, 80, 2)
        self.running_r.append(run)
        run = sprite_sheet.get_image(10, 120, 80, 2)
        self.running_r.append(run)
        
        # load all images and flip them
        
        self.walking_l = self.running_r
        self.walking_l = pygame.transform.flip(run, True, False)
        
        # setting the image the player starts with
        self.image = self.running_r[0]
        
        # jumping
        jump = sprite_jump.get_image(1, 120, 80, 2)
        self.jumping.append(jump)
        
        # set a image rect
        self.rect = self.image.get_rect()
        
    def update(self):
        # moving the player 
        # gravity
        self.calc_grav()
        
        # moving left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world.shift

        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_r)
            self.image = self.walking_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_l)
            self.image = self.walking_l[frame]
        
        # move up and down
        self.rect.y = self.change_y
            
        # checking to see if your on the ground
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right        
    def calc_grav(self):
        # calcalate gravity
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
            

                  
        if self.rect.y >= main.WIN_H == self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = main.WIN_H - self.rect.height
        
    def jump(self):
        # called when the user jumps 
        
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platfrom_list, False)
        
    def left(self):
        self.change_x = -6
    
    def right(self):
        self.change_x = 6
    
    def stop(self):
        self.change_x = 0            
        
        