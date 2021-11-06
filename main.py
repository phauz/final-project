import pygame, os, random, sys

pygame.init()
pygame.font.init()

# screen variables

SCREEN_W = 1400
SCREEN_H = 800
SCREEN = pygame.display.set_mode(SCREEN_W, SCREEN_H)

RUNNING = [pygame.image.load(os.path.join("images/outline", "_Run.png"))]


class knight:
    
    def __init__(self):
        
        self.running = RUNNING