import pygame
import os

WIDTH, HEIGHT = 640, 512
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moneyville")

BACKGROUND_COLOR = (255, 255, 255)
FPS = 60

CHAR_HEIGHT = 100
CHAR_WIDTH = 70
MAIN_CHARACTER = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'main_character.jpg')), (CHAR_WIDTH, CHAR_HEIGHT))
BACKGROUND_MAP = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'map1.jpg')), (WIDTH, HEIGHT))
CHARACTER_X, CHARACTER_Y = 0, 0


loadingscreenset = True  # Stars as false
onmap = True  # Starts as false


def draw(x,y):
    draw_background()
    draw_character(x,y)
    #if onmap:
        #draw_character()
    #else: #draw options into four box screen


def draw_character(x, y):
    WIN.blit(MAIN_CHARACTER, (x, y))
    pygame.display.update()


def draw_background():  # draws the background, if we're on the map it draws the map otherwise it draws the boxes for the selection screen
    if onmap:
        WIN.fill(BACKGROUND_COLOR)
        WIN.blit(BACKGROUND_MAP, (0, 0))
    # else: #draw a box with four descriptions of options


def islegalarea(x,y):
   
   if 40 < x < 500 and 200 < y < 220:
        return True
   if 70 < x < 330 and 460 < y < 470:
        return True
   if 40 < x < 590 and 310 < y < 325:
        return True
   if 465 < x < 485 and 325 < y < 435:
        return True
   if 420 < x < 535 and 135 < y < 150:
        return True
   if 420 < x < 437 and 135 < y < 320:
        return True
   if 340 < x < 420 and 80 < y < 95:
        return True
   if 340 < x < 367 and 80 < y < 325:
        return True
   if 295 < x < 308 and 200 < y < 470:
        return True
   if 227 < x < 242 and 200 < y < 325:
        return True
   if 138 < x < 151 and 200 < y < 325:
        return True
   if 40 < x < 55 and 200 < y < 325:
        return True


def main():
    clock = pygame.time.Clock()
    run = True
    Coordinates = pygame.Rect(300,300,CHAR_WIDTH,CHAR_HEIGHT)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            Coordinates.x -= 5
        if keys[pygame.K_RIGHT]:
            Coordinates.x += 5
        if keys[pygame.K_UP]:
            Coordinates.y -= 5
        if keys[pygame.K_DOWN]:
            Coordinates.y += 5
        draw(Coordinates.x,Coordinates.y)
    pygame.quit()


if __name__ == "__main__":
    main()
