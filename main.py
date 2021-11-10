import pygame, os, random, sys
from pygame import draw
from pygame import font
from player import Player, player
import platforms
pygame.init()
pygame.font.init()

# TODO learn hwo to use spreadsheets and making multiple files in to pygame

# screen variables
pygame.display.set_caption("final project")

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

def main():
    pygame.init()
    WIN_W = 1100
    WIN_H = 600
    win = pygame.display.set_mode((WIN_W, WIN_H))
    
    pygame.display.set_caption('Final Project')
    
    # creating player
    knight = Player()
    
    # creating levels
    level_list = []
    current_level = level_list[current_level_no]
    
    # setting current level
    current_level_no = 0
    
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    
    player.rect.x = 340
    player.rect.y = WIN_H - player.rect.height
    active_sprite_list.add(player)
    
    run = False
    
    clock = pygame.time.Clock()
    
    while not run:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                run = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                    
        # Update the player.
        active_sprite_list.update()
        
        # Update items in the level
        current_level.update()
        
        # shifting the world screen
        
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)
            
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
        
        current_level.draw(win)
        active_sprite_list(win)
        
        
        clock.tick(60)
        
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()
        