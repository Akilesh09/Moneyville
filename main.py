import pygame
import os
import random


WIDTH, HEIGHT = 640, 512
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moneyville")

CashOnHand = 10000
UnrealizedGains = 0
Target = 20000

Year = 0

BACKGROUND_COLOR = (255, 255, 255)
FPS = 60

CHAR_HEIGHT = 75
CHAR_WIDTH = 150
MAIN_CHARACTER = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'main_character.jpg')), (CHAR_WIDTH, CHAR_HEIGHT))
BACKGROUND_MAP = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'map1.jpg')), (WIDTH, HEIGHT))
PICK_SOMETHING_SCREEN = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'questionscreen.jpg')), (WIDTH, HEIGHT))
CHARACTER_X, CHARACTER_Y = 0, 0
counter = 0

loadingscreenset = True  # Starts as false
onmap = True  # Starts as false

START_BUTTON_RECT = pygame.Rect(240, 200, 160, 50)
EXIT_BUTTON_RECT = pygame.Rect(240, 300, 160, 50)

def draw_home_screen():
    WIN.fill(BACKGROUND_COLOR)

    # Draw the "Start" button
    pygame.draw.rect(WIN, (0, 255, 0), START_BUTTON_RECT)
    start_font = pygame.font.Font(None, 36)
    start_text = start_font.render("Start", True, (0, 0, 0))
    start_text_rect = start_text.get_rect(center=START_BUTTON_RECT.center)
    WIN.blit(start_text, start_text_rect)

    # Draw the "Exit" button
    pygame.draw.rect(WIN, (255, 0, 0), EXIT_BUTTON_RECT)
    exit_font = pygame.font.Font(None, 36)
    exit_text = exit_font.render("Exit", True, (0, 0, 0))
    exit_text_rect = exit_text.get_rect(center=EXIT_BUTTON_RECT.center)
    WIN.blit(exit_text, exit_text_rect)
    pygame.display.update()


def draw_stats():
    # Stat names and numerical values
    pygame.draw.rect(WIN, (255, 255, 255), (0, 0, 200, 150))

    
    font = pygame.font.Font("font.ttf", 12)
    
    cash_text = font.render(f"{'Cash on Hand'}: {CashOnHand}", True, (0, 0, 0))
    investment_text = font.render(f"{'Unrealized Gains'}: {UnrealizedGains}", True, (0, 0, 0))
    target_text = font.render(f"{'Target'}: {Target}", True, (0, 0, 0))
    year_text = font.render(f"{'Year'}: {Year}", True, (0, 0, 0))


    WIN.blit(cash_text, (20, 20))
    WIN.blit(investment_text, (20, 50))
    WIN.blit(target_text, (20, 80))
    WIN.blit(year_text, (20, 110))

    
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
    in_home_screen = True
    Coordinates = pygame.Rect(300,300,CHAR_WIDTH,CHAR_HEIGHT)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if in_home_screen:
            # Draw the home screen
            draw_home_screen()

            # Check for button clicks
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if START_BUTTON_RECT.collidepoint(mouse_pos):
                    # Start button clicked, transition to the game
                    in_home_screen = False
                    # Add your game initialization code here
                elif EXIT_BUTTON_RECT.collidepoint(mouse_pos):
                    # Exit button clicked, quit the game
                    pygame.quit()
        else:
            keys = pygame.key.get_pressed()
            # print(Coordinates.x, Coordinates.y)
            if keys[pygame.K_LEFT] and Coordinates.x>-49:
                Coordinates.x -= 3
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

def choicemenu(prompt,choices,consequence):
    f = True
    WIN.blit(BACKGROUND_MAP, (0, 0))
    pygame.display.update()
    #add line that displays the prompt on the screen
    #add line that dispslays the prompt on the 
    if len(choices) == 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return
        return 0
    while(f):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            consequence[1]
            return
        if keys[pygame.K_2]:
            consequence[2]
            return
        if keys[pygame.K_3] and len(choices) > 2:
            consequence[3]
            return
        if keys[pygame.K_4] and len(choices) == 4:
            consequence[4]
            return
        
#def gym():
    choicemenu("Choose a workout", ["30 minute run", "Weightlifting (1 hour)", "Return Back"], )
def bank():
    choicemenu("What type of fund would you like to invest in?", ["Stocks - Medium risk with average ROI of 10% (1 hour)", "Bonds - Low risk with average ROI of 4%(1 hour)", "Certified Deposit(CD) - Very low risk with average ROI of 2%(1 hour)","EXIT"])


#consequences

#def thirty_minute_run():
#    if .5 > remaininghours:
#        choicemenu("Sorry, not enough time left", [],)
#    else:
#        reduceTime(30)
#        changeHealth(1)

#def weightlift():
#    if 1 > remaininghours:
#        choicemenu("Sorry, not enough time left", [],)
#    else:
#        reduceTime(.5)
#        changeHealth(1)

#def reduceTime(value): #value in hours
#    remaininghours = remaininghours - value

#def newDay(): #sets time back to normal 
#    time = dailytime
#    changeHealth(-1)
#    social = social -1 

#def changeMoney(value):
#    money = money + value
    
#def multInvestment(factor): #mult factor 
#    investmentMoney = investmentMoney * factor

#def changeHealth(value): #adds/decreases to fitness
#    health += value
#    if health > 100:
#        health = 99
    
#def gamble(value):
#    if money < 500:
#        choicemenu("Way too less money, sorry!",[],)
#    else:
#        random_number = random.random()
#        if random.random() > random_number * 1.07:
#            choicemenu("Congrats, your picks won!")

            