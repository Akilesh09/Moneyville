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
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets','map1.jpg')),(HEIGHT,WIDTH))


# def draw_window():
#     WIN.fill(BACKGROUND_COLOR)
#     WIN.blit(MAIN_CHARACTER,(500,300))
#     pygame.display.update()

def draw_background():
    WIN.fill(BACKGROUND_COLOR)
    WIN.blit(MAIN_CHARACTER,(500,300))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = Truef
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()

