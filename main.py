import pygame, os, random, sys

pygame.init()
pygame.font.init()

# screen variables

SCREEN_W = 1400
SCREEN_H = 800
win = pygame.display.set_mode(SCREEN_W, SCREEN_H)
clock = pygame.time.Clock()
steps = 10

RUNNING = [pygame.image.load(os.path.join(("images/outline", "_Run.png"))]

cave_sounds = pygame.mixer.Sound("sounds/cavesounds.mp3.wav")


class knight:
    X_POS = 80
    Y_POS = 500
    def __init__(self):
        
        self.running = RUNNING
        self.userInput = pygame.key.get_pressed()
        
        self.knight_rect = self.running.get_rect()
        self.knight_rect.x = self.X_POS
        self.knight_rect.y = self.X_POS
        
    pygame.sprite.Sprite.__init__(self):
        self.movex = 0
        self.movey = 0
        self.frame = 0
        
    def running(self, userInput):
    
        if userInput[pygame.K_w] and [pygame.K_LSHIFT]:
            
            
    
            
            
    def draw(self, win):
        win.blit(self.image, (self.knight_rect.x, self.knight_rect.y))



run = True

def main():
    
    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = false
                
    key_pressed = pygame.key.get_pressed()
                
                
    win.fill(255,255,255)
    userInput = pygame.key.get_pressed()
    knight.draw(win)
    
    clock.tick(30)
    pygame.display.update()
    
    