import pygame
import os

WIDTH, HEIGHT = 640, 512
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moneyville")

health = 100
money = 1000
social = 50

# Define stat names
health_name = "Health"
money_name = "Money"
social_name = "Social"

BACKGROUND_COLOR = (255, 255, 255)
FPS = 60

CHAR_HEIGHT = 75
CHAR_WIDTH = 150
MAIN_CHARACTER = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'main_character.jpg')), (CHAR_WIDTH, CHAR_HEIGHT))
BACKGROUND_MAP = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'map1.jpg')), (WIDTH, HEIGHT))
CHARACTER_X, CHARACTER_Y = 0, 0


loadingscreenset = True  # Starts as false
onmap = True  # Starts as false

def draw_stats():
    # Stat names and numerical values
    pygame.draw.rect(WIN, (255, 255, 255), (0, 0, 150, 150))

    
    font = pygame.font.Font("font.ttf", 15)
    
    health_text = font.render(f"{health_name}: {health}", True, (0, 0, 0))
    money_text = font.render(f"{money_name}: {money}", True, (0, 0, 0))
    social_text = font.render(f"{social_name}: {social}", True, (0, 0, 0))


    WIN.blit(health_text, (20, 20))
    WIN.blit(money_text, (20, 60))
    WIN.blit(social_text, (20, 100))

    # Stat bars
    pygame.draw.rect(WIN, (255, 0, 0), (20, 50, health, 10))
    pygame.draw.rect(WIN, (0, 255, 0), (20, 90, money/1000, 10))
    pygame.draw.rect(WIN, (0, 0, 255), (20, 130, social, 10))

    # Stat bar outlines
    pygame.draw.rect(WIN, (0, 0, 0), (20, 50, 100, 10), 2)
    pygame.draw.rect(WIN, (0, 0, 0), (20, 90, 100, 10), 2)
    pygame.draw.rect(WIN, (0, 0, 0), (20, 130, 100, 10), 2)

    
def draw(x,y):
    draw_background()
    if onmap:
        draw_character(x,y)
    draw_stats()
    pygame.display.update()

    #if onmap:
        #draw_character()
    #else: #draw options into four box screen


def draw_character(x, y):
    WIN.blit(MAIN_CHARACTER, (x, y))


def draw_background():  # draws the background, if we're on the map it draws the map otherwise it draws the boxes for the selection screen
    if onmap:
        WIN.fill(BACKGROUND_COLOR)
        WIN.blit(BACKGROUND_MAP, (0, 0))
    # else: #draw a box with four descriptions of options


# def islegalarea(x,y):
   
#    if 40 < x < 500 and 200 + CHAR_HEIGHT < y < 220 + CHAR_HEIGHT :
#         return True
#    if 70 < x < 330 and 460+ CHAR_HEIGHT < y < 470+ CHAR_HEIGHT :
#         return True
#    if 40 < x < 590 and 310+ CHAR_HEIGHT  < y < 325+ CHAR_HEIGHT :
#         return True
#    if 465 < x < 485 and 325+ CHAR_HEIGHT  < y < 435+ CHAR_HEIGHT :
#         return True
#    if 420 < x < 535 and 135 + CHAR_HEIGHT < y < 150+ CHAR_HEIGHT :
#         return True
#    if 420 < x < 437 and 135+ CHAR_HEIGHT  < y < 320+ CHAR_HEIGHT :
#         return True
#    if 340 < x < 420 and 80+ CHAR_HEIGHT  < y < 95+ CHAR_HEIGHT :
#         return True
#    if 340 < x < 367 and 80 + CHAR_HEIGHT < y < 325+ CHAR_HEIGHT :
#         return True
#    if 295 < x < 308 and 200+ CHAR_HEIGHT  < y < 470+ CHAR_HEIGHT :
#         return True
#    if 227 < x < 242 and 200+ CHAR_HEIGHT  < y < 325+ CHAR_HEIGHT :
#         return True
#    if 138 < x < 151 and 200+ CHAR_HEIGHT  < y < 325+ CHAR_HEIGHT :
#         return True
#    if 40 < x < 55 and 200+ CHAR_HEIGHT  < y < 325+ CHAR_HEIGHT :
#         return True


def main():
    pygame.init()  # Initialize Pygame
    pygame.font.init()  # Initialize the font module
    clock = pygame.time.Clock()
    run = True
    Coordinates = pygame.Rect(300,300,CHAR_WIDTH,CHAR_HEIGHT)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        # print(Coordinates.x, Coordinates.y)
        if keys[pygame.K_LEFT] and Coordinates.x>-49:
            Coordinates.x -= 2
        if keys[pygame.K_RIGHT] and Coordinates.x < 538:
            Coordinates.x += 3
        if keys[pygame.K_UP] and Coordinates.y > -3:
            Coordinates.y -= 3
        if keys[pygame.K_DOWN] and Coordinates.y < 423:
            Coordinates.y += 3
        draw(Coordinates.x,Coordinates.y)
    pygame.quit()


if __name__ == "__main__":
    main()
