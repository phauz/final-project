import pygame, os, random, sys
from pygame import draw
from pygame import font

pygame.init()
pygame.font.init()

# screen variables
pygame.display.set_caption("final project")
WIN_W = 1100
WIN_H = 600
win = pygame.display.set_mode((WIN_W, WIN_H))

vel = 5

# TODO add backdrop and and other images/sounds and other game variables

width = 64
height = 64

#fonts 
fontMenu = pygame.font.Font("fonts/Precise-M Bold.ttf", 16)

# TODO add fonts

#buttons
start_img = pygame.image.load(os.path.join("images/buttons", "start_button.png")).convert_alpha()

idle = pygame.image.load(os.path.join("images/idle", "idle.png"))

runningRight = [pygame.image.load(os.path.join("images/running", "run1.png")),
           pygame.image.load(os.path.join("images/running", "run2.png")),
           pygame.image.load(os.path.join("images/running", "run3.png")),
           pygame.image.load(os.path.join("images/running", "run4.png")),
           pygame.image.load(os.path.join("images/running", "run5.png")),
           pygame.image.load(os.path.join("images/running", "run6.png")),
           pygame.image.load(os.path.join("images/running", "run7.png")),
           pygame.image.load(os.path.join("images/running", "run8.png")),
           pygame.image.load(os.path.join("images/running", "run9.png")),
           pygame.image.load(os.path.join("images/running", "run10.png"))]

runningLeft = runningRight
runningLeft = pygame.transform.flip(win, True, False)

tileset = pygame.image.load(os.path.join("images/tileset/platforms", "mossy-floating.png"))
tileset = pygame.transform.scale(tileset, (500, 200))
cave_sounds = pygame.mixer.Sound("sounds/cavesounds.mp3.wav")

class knight:
    x = 80
    y = 500
    
    def __init__(self):
        
        self.running_left = runningLeft
        self.running_right = runningRight
        self.runCount = 0
        
        self.idle = idle
        
        self.left = False
        self.right = False
        
        self.userInput = pygame.key.get_pressed()
        
        self.knight_rect = self.running.get_rect()
        self.knight_rect.x = self.x
        self.knight_rect.y = self.y
        
    def running(self, userInput):

        
        if userInput[pygame.K_RIGHT] and [pygame.K_LSHIFT] and x < WIN_W - width - vel:
            x += vel
            self.running_right = True
            self.running_left = False
        if userInput[pygame.K_LEFT] and [pygame.K_LSHIFT] and x > vel:
            x -= vel
            self.running_left = True
            self.running_right = False      
        else:
            self.running_right = False
            self.running_right = False
            self.runCount = 0
            
    def draw(self, win):
        
        win.blit(self.image, (self.knight_rect.x, self.knight_rect.y))
        
        if self.runCount + 1 >= 30:
            runCount = 0
        if runningLeft:
            win.blit(self.running_left[runCount//3, (x, y)])
            runCount += 1
        elif right:
            win.blit(runningRight[runCount//3], (x ,y))
            runCount += 1
        else:
            win.blit(idle, (x,y))

    pygame.display.update()

class Button():
    def __init__(self, x ,y ,image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x , y)
        self.clicked = False
        
    def draw(self):   
        action = False
        #getting mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and collect conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True    
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        win.blit(self.image, (self.rect.x, self.rect.y))
        return action
        
start_button = Button(100, 200, start_img, 0.5)
run = True
welcomeMessage = fontMenu.render("Welcome to my game", True, (0,0,0))
while run:
    
    win.blit(tileset, (WIN_H,100))
    # welcomeMessageRect = welcomeMessage.get_rect()
    # welcomeMessage.center = ((SCREEN_W // 2, SCREEN_H // 2))
    # win.blit(welcomeMessage, welcomeMessageRect)
    if start_button.draw() == True:
        print('start') 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
            
    pygame.display.update()    

pygame.quit()

# def main():
#     knight = knight()
#     clock = pygame.time.Clock()
#     run = True
        
#     while run: 
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = false
#                 sys.exit()
   
#         win.fill(255,255,255)
#         win.blit(tileset, (0, 0))
#         userInput = pygame.key.get_pressed()
#         knight.draw(win)
#         knight.update(userInput)
       
#         clock.tick(30)
#         pygame.display.update()
    
 
    
#         pygame.quit()