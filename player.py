import pygame, os

from pygame import sprite
import main
from spritesheets import SpriteSheet
# calling file name 

running = [pygame.image.load(os.path.join("images/animations/running", "run1.png")),
           pygame.image.load(os.path.join("images/animations/running", "run2.png")),
           pygame.image.load(os.path.join("images/animations/running", "run3.png")),
           pygame.image.load(os.path.join("images/animations/running", "run4.png")),
           pygame.image.load(os.path.join("images/animations/running", "run5.png")),
           pygame.image.load(os.path.join("images/animations/running", "run6.png")),
           pygame.image.load(os.path.join("images/animations/running", "run7.png")),
           pygame.image.load(os.path.join("images/animations/running", "run8.png")),
           pygame.image.load(os.path.join("images/animations/running", "run9.png")),
           pygame.image.load(os.path.join("images/animations/running", "run10.png"))]

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
        self.rect.y += self.change_y
            
            
    def calc_grav(self):
        # calcalate gravity
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
            
        # checking to see if your on the ground
        if self.rect.y >= main.WIN_H == self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = main.WIN_H - self.rect.height
        
    def jump(self):
        # called when the user jumps 
        
        self.rect.y += 2
        
        if self.rect.bottom >= WIN_H:
            self.change_y = -10
        
    def left(self):
        self.change_x = -6
    
    def right(self):
        self.change_x = 6
    
    def stop(self):
        self.change_x = 0            
        
        