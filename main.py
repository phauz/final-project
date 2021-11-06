import pygame, os, random, sys

pygame.init()
pygame.font.init()

# screen variables

SCREEN_W = 1400
SCREEN_H = 800
SCREEN = pygame.display.set_mode(SCREEN_W, SCREEN_H)
clock = pygame.time.Clock()

RUNNING = [pygame.image.load(os.path.join("images/outline", "_Run.png"))]


class knight:
    
    def __init__(self):
        
        self.running = RUNNING
        
    def update(self. userInput):
        if self.running:
            self.run()
            
            
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self))



run = True
def main():
    
    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = false
                
                
    SCREEN.fill(255,255,255)
    userInput = pygame.key.get_pressed()
    