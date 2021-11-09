import pygame, os
import main


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

class player(pygame.sprite.Sprite):
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
        
        sprite_sheet = SpriteSheet()
        self.running_l = running
        self.running_l = pygame.transform.flip(running, True, False)
        self.running_r = running
        
        self.image = self.running_r[0]
        
        self.rect = self.image.get_rect()
        
        def update(self):
            # moving the player 
            # gravity
            self.calc_grav()
            
            # moving left/right
            self.rect.x += self.change_x
            pos = self.rect.x
            
        def calc_grav(self):
            # calcalate gravity
            if self.change_y == 0:
                self.change_y = 1
            else:
                self.change_y += 0.35
                
            # checking to see if your on the ground
            
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
        
        