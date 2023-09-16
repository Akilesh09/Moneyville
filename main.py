import pygame
import os

WIDTH,HEIGHT = 640,512
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Moneyville")

BACKGROUND_COLOR = (255,255,255)
FPS = 60

CHAR_HEIGHT = 100
CHAR_WIDTH = 70
MAIN_CHARACTER = pygame.transform.scale(pygame.image.load(os.path.join('Assets','main_character.jpg')),(CHAR_HEIGHT,CHAR_WIDTH))
BACKGROUND_MAP = pygame.transform.scale(pygame.image.load(os.path.join('Assets','map1.jpg')),(WIDTH,HEIGHT))
CHARACTER_X, CHARACTER_Y = 0,0


loadingscreenset = True#Stars as false
onmap = True # Starts as false

def draw():
    draw_background()
    if onmap:
        draw_character()
    else: #draw options into four box screen

def draw_character(x,y):
    WIN.fill(BACKGROUND_COLOR)
    WIN.blit(MAIN_CHARACTER,(x,y))
    pygame.display.update()

def draw_background(): #draws the background, if we're on the map it draws the map otherwise it draws the boxes for the selection screen
    if onmap:
        WIN.fill(BACKGROUND_COLOR)
        WIN.blit(BACKGROUND_MAP,(0,0))
    else: #draw a box with four descriptions of options

    pygame.display.update()

def islegalarea(): 



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #draw_window()
        draw()
    pygame.quit()

if __name__ == "__main__":
    main()

