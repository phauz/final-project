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
ani = 4
vel = 5

# TODO add backdrop and and other images/sounds and other game variables

width = 64
height = 64

#fonts 
fontMenu = pygame.font.Font("fonts/Precise-M Bold.ttf", 32)

# TODO add fonts

#buttons
start_img = pygame.image.load(os.path.join("images/buttons", "start_button.png")).convert_alpha()

idle = pygame.image.load(os.path.join("images/animations/idle", "idle.png"))
idle = pygame.transform.scale(idle, (64 * 3, 64  * 3))
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

jumping = [pygame.image.load(os.path.join("images/animations/jumping", "jump.png")),
           pygame.image.load(os.path.join("images/animations/jumping", "jump2.png")),
           pygame.image.load(os.path.join("images/animations/jumping", "jump3.png"))]

cave_sounds = pygame.mixer.Sound("sounds/cavesounds.mp3.wav")


class Knight():
    x = 50
    y = (WIN_H / 2) - 100    
    vel = 9
    def __init__(self):
        self.movey = 0
        self.movex = 0
        self.frame = 0
        self.vel = vel
        self.knight_jumping = False
        self.knight_running = False
        self.knight_idle = True
        self.idle_img = idle



    def run(self):
        self.run_img = running
        self.knight_run = self.run_img[0]
        self.rect = self.knight_run.get_rect()
          
        self.rect.x = self.rect.x + self.movex 
   
        if self.movex < 0:
            self.frame += 1
        if self.frame > 3*ani:
            self.frame = 0
        self.knight_run = pygame.transform.flip(self.run_img[self.frame // ani], True, False)
    # running right
        if self.movex > 0:
            self.frame += 1
        if self.frame > 3*ani:
            self.frame = 0
        self.knight_run = self.run_img[self.frame//ani]
    
    def jump(self):
        self.jump_img = jumping
        self.knight_jump = self.jump_img[0]
        
        self.rect.y = self.rect.y + self.movey
        if self.knight_jumping:
            self.rect.y -= self.vel * 4
            self.vel =- 0.8
        if self.vel < - vel:
            self.jumping = False
            self.vel = vel

        
        if self.movey > 0:
            self.frame += 1
        if self.frame > 3:
            self.frame = 0
        self.knight_jump = self.jump_img[self.frame//3]

    def control(self ,x, y):
        self.movex += x
        self.movey += y
        
    def update(self, userInput):
        if self.knight_running:
            self.run()
        if self.knight_jumping:
            self.jump()
            
        if self.frame >= 10:
            self.frame = 0
        
        if userInput[pygame.K_LEFT] and [pygame.K_RIGHT]:
            self.knight_running = True
        elif userInput[pygame.K_SPACE]:
            self.knight_jumping = True
        elif not self.knight_jumping and self.knight_running:
            knight_idle = True
            self.idle_img
 
            
            

            
    def draw(self, win):
        win.blit(self.knightPos, (self.rect.x, self.rect.y))
        
    # def running(self, userInput):
    #     if userInput[pygame.K_RIGHT] and [pygame.K_LSHIFT] and x < WIN_W - width - vel:
    #         self.x += vel
    #         self.right = True
    #         self.left = False
    #         win.blit(runningRight[runningRight//3], (self.x, self.y))
    #         self.runCount += 1
    #     if userInput[pygame.K_LEFT] and [pygame.K_LSHIFT] and x > vel:
    #         self.x -= vel
    #         self.left = True
    #         self.right = False   
    #         win.blit(runningLeft[running//3], (self.x, self.y))   
    #         self.runCount += 1
    #     else:
    #         self.right = False
    #         self.left = False
    #         self.runCount = 0
    #         self.idle
 
    
    # def idle(self, win):
    #     win.blit(self.idle, (self.x, self.y))



# class Button():
#     def __init__(self, x ,y ,image, scale):
#         width = image.get_width()
#         height = image.get_height()
#         self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x , y)
#         self.clicked = False
        
#     def draw(self):   
#         action = False
#         #getting mouse position
#         pos = pygame.mouse.get_pos()

#         #check mouseover and collect conditions
#         if self.rect.collidepoint(pos):
#             if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
#                 action = True
#                 self.clicked = True    
#         if pygame.mouse.get_pressed()[0] == 0:
#             self.clicked = False
        
#         win.blit(self.image, (self.rect.x, self.rect.y))
#         return action
        
# start_button = Button(100, 200, start_img, 0.5)




# def startingMenu():
#     win.blit(startingMenuScreen, (0, 0))
#     win.blit(idle, (50, 250))
#     welcomeMessage = fontMenu.render("Welcome to my game", True, (0,0,0))
#     welcomeMessage_center = (WIN_W // 2 - 300, WIN_H // 2 - 100)
#     win.blit(welcomeMessage, welcomeMessage_center)

# setup
startingMenuScreen = pygame.image.load(os.path.join("images/backgrounds", "startingMenu.png"))
startingMenuScreen = pygame.transform.scale(startingMenuScreen, (WIN_W, WIN_H))
clock = pygame.time.Clock()
pygame.init()
fps = 30
knight = Knight()
userInput = pygame.key.get_pressed()
steps = 5
run = True
while run:
    
    # startingMenu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                knight.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                knight.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                knight.control(0 , steps)
        
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                knight.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                knight.control(-steps,0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                run = False
        
    
    win.blit(startingMenuScreen, (0,0))
    knight.update(userInput)
    knight.draw(win)
    pygame.display.flip()
    clock.tick(fps)    

pygame.quit()


# TODO once player moves to the right the game starts
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