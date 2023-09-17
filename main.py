import pygame
import os
import random
import textwrap
import time



WIDTH, HEIGHT = 640, 512
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moneyville")

CashOnHand = 10000
UnrealizedGains = 0
Target = 20000

Year = 0

BACKGROUND_COLOR = (255, 255, 255)
BACKGROUND_COLOR2 = (255, 253, 140)

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
global onmap
onmap = False

START_BUTTON_RECT = pygame.Rect(240, 200, 160, 50)
EXIT_BUTTON_RECT = pygame.Rect(240, 300, 160, 50)

def draw_home_screen():
    WIN.fill(BACKGROUND_COLOR2)

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
    target_text = font.render(f"{'Target'}: {int(Target*(1.03)**Year)}", True, (0, 0, 0))
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

def end_of_year():
    global Year
    global CashOnHand
    global UnrealizedGains

    # Add unrealized gains to cash on hand
    CashOnHand += UnrealizedGains

    # Reset unrealized gains for the next year
    UnrealizedGains = 0

    # Increment the year
    Year += 1
   


def draw_character(x, y):
    WIN.blit(MAIN_CHARACTER, (x, y))

def spaceBar(x,y):
    # (78,264) (192,390)
    if 78 < x < 192 and 264 < y < 390:
        bank()
    # (186,60) 258,159
    if 186 < x < 258 and 60 < y < 159:
        bank_quiz()
    # (69,87) (156,150
    if 69 < x < 156 and 87 < y < 150:
        pass
    # 297,45 324,157
    if 297 < x < 324 and 45 < y < 157:
        pass
    # 450,-3 504,66
    if 450 < x < 504 and -3 < y < 66:
        pass
    pass


def draw_background():  # draws the background, if we're on the map it draws the map otherwise it draws the boxes for the selection screen
    if onmap:
        WIN.fill(BACKGROUND_COLOR)
        WIN.blit(BACKGROUND_MAP, (0, 0))
    # else: #draw a box with four descriptions of options

def choicemenu(prompt, choices):
    f = True
    choice_font = pygame.font.Font(None, int(36 * 0.7))  # Reduced font size by a factor of 0.7

    # Display the choices before entering the while loop
    WIN.fill((0, 0, 0))  # Black background
    prompt_font = pygame.font.Font(None, int(24 * 0.7))  # Reduced font size by a factor of 0.7
    prompt_text = prompt_font.render(prompt, True, (255, 255, 255))  # White text
    prompt_text_rect = prompt_text.get_rect(center=(WIDTH // 2, 50))
    WIN.blit(prompt_text, prompt_text_rect)

    for i, choice in enumerate(choices):
        choice_rect = pygame.Rect(20 if i % 2 == 0 else 320,  # Left or right side
                                   180 if i < 2 else 330,    # Top or bottom row
                                   300, 150)
        pygame.draw.rect(WIN, (255, 255, 255), choice_rect, 3)  # White border with 3-pixel width

        # Wrap long paragraphs to fit within the choice box, leaving a 10-pixel margin
        max_width = 280  # Maximum width for the text inside the box
        wrapped_text = textwrap.fill(choice, width=30)  # Adjust the width as needed
        wrapped_lines = wrapped_text.split('\n')

        # Calculate the total height required for the wrapped text
        total_height = 0
        for line in wrapped_lines:
            line_text = choice_font.render(line, True, (255, 255, 255))  # White text
            total_height += line_text.get_height()

        # Calculate the y-coordinate to center the wrapped text vertically
        y_offset = (choice_rect.height - total_height) // 2

        # Render and display wrapped text line by line
        for line in wrapped_lines:
            text = choice_font.render(line, True, (255, 255, 255))  # White text
            text_rect = text.get_rect(left=choice_rect.left + 10, top=choice_rect.top + y_offset + 10)
            WIN.blit(text, text_rect)
            y_offset += text.get_height()

    pygame.display.update()

    if len(choices) == 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return
        return 0
    mouse_x, mouse_y = -5, -5
    
    while(f):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # print(mouse_x,mouse_y)
        if 20 < mouse_x < 320 and 180 < mouse_y <330:
            f = False
            return 0
        if 320 < mouse_x < 620 and 180 < mouse_y <330:
            f = False
            return 1
        if 20 < mouse_x < 320 and 330 < mouse_y <480 and len(choices) >= 3:
            return 2
        if 320 < mouse_x < 620 and 330 < mouse_y <480 and len(choices) == 4:
            f = False
            return 3
        # keys = pygame.key.get_pressed()
        # print(keys)
        # if keys[pygame.K_1]:
        #     consequence[1]
        #     return
        # elif keys[pygame.K_2]:
        #     consequence[2]
        #     return
        # elif keys[pygame.K_3] and len(choices) > 2:
        #     consequence[3]
        #     return
        # elif keys[pygame.K_4] and len(choices) == 4:
        #     consequence[4]
        #     return


def split_string_into_sets_of_12_words(input_string):
    words = input_string.split()
    return [" ".join(words[i:i+12]) for i in range(0, len(words), 12)]

def display_text(text):
    arr = split_string_into_sets_of_12_words(text)
    for x in arr:
        choicemenu(x,["","","",""])

def bank_quiz():
    onmap = False #necessary
    display_text("Index Funds: An index fund is a type of mutual fund or exchange-traded fund (ETF) that aims to replicate the performance of a specific market index, such as the S&P 500 (Top 500 publicly traded companies). It is a passive investment strategy designed to match the returns of the index it tracks. It is typically a long term investment placed in retirement accounts, and offers moderately risky diversification options. Typical returns range from 3%-9% per year. ")
    display_text("IPOs: An IPO is the process by which a privately held company becomes publicly traded by issuing shares of stock to the general public for the first time. It's often seen as a way for companies to raise capital to fuel growth. IPOs can be extremely risky, and require a detailed analysis of the companies performance pre-IPO to help determine future performance. Returns may range from -30%-100% per year. ")
    display_text("Company Stock: Stocks, also known as equities or shares, represent ownership in a company. When you buy a stock, you become a shareholder and have a claim on the company's assets and earnings. You will need to pay close attention to market conditions, investor sentiment towards the company, and pay close attention to quarterly reports! Average returns are about -10-30% per year.")
    display_text("U.S Treasury Bonds: These are issued by the U.S. Department of the Treasury and are considered one of the safest investments in the world. The rate of return is 1%")
    display_text("Corporate Bonds:  These are issued by corporations to raise capital for various purposes, such as expansion or debt refinancing. Corporate bonds can vary in terms of credit quality, with investment-grade bonds being less risky than high-yield or junk bonds. The rate of return is 3%")
    display_text("Certificate of Deposit: A Certificate of Deposit (CD) is a financial instrument offered by banks and credit unions that allows individuals to deposit a fixed amount of money for a specified period of time, typically ranging from a few months to several years. The rate of return is 1.5%")
    display_text("Quiz Time!")
    while not(choicemenu("1. What is the primary goal of an index fund?", ["a. To outperform the market", "b. To replicate the performance of a specific market index", "c. To invest in IPOs", "d. To generate consistent interest from bonds"]) == 1):
        None
    while not(choicemenu("2. What is the typical range of returns for index funds per year?", ["a. -30% to 100%", "b. 1% to 3%", "c. 3% to 9%", "d. -10% to 30%"]) == 2):
        None
    while not(choicemenu("3. What does IPO stand for, and what does it involve?", ["a. IPO stands for Index Performance Offering, and it involves tracking market indices.", "b. IPO stands for Individual Passive Ownership, and it involves investing in index funds.", "c. IPO stands for Initial Public Offering, and it involves a privately held company going public by issuing shares to the general public.", "d. IPO stands for Income Potential Opportunity, and it involves investing in corporate bonds."]) == 2):
        None
    while not(choicemenu("4. What should investors pay attention to when buying company stock?", ["a. The rate of return on U.S. Treasury Bonds", "b. Market conditions and investor sentiment towards the company", "c. The average returns of index funds", "d. The price of gold"]) == 1):
        None
    while not(choicemenu("5. Which type of bond is considered one of the safest investments in the world?", ["a. Corporate Bonds", "b. Certificate of Deposit", "c. U.S. Treasury Bonds", "d. Municipal Bonds"]) == 2):
        None
    while not(choicemenu("6. What is the primary purpose of issuing Corporate Bonds?", ["a. To raise capital for expansion", "b. To provide long-term returns", "c. To match the performance of market indices", "d. To invest in IPOs"]) == 0):
        None
    while not(choicemenu("7. What is the rate of return typically associated with Corporate Bonds?", ["a. 1%", "b. 3%", "c. 1.5%", "d. Varies widely"]) == 1):
        None
    while not(choicemenu("8. What is the rate of return typically associated with Certificate of Deposit (CD)?", ["a. 1%", "b. 3%", "c. 1.5%", "d. Varies widely"]) == 2):
        None
    



def bank():
    onmap = False
    global UnrealizedGains
    global CashOnHand
    choice = choicemenu("What type of fund would you like to invest in?", ["Stocks(-10-30% ROI)", "IPO(-20-100% ROI)", "Index Fund(4-8% ROI)","EXIT"])
    if not choice == 3:
        multiplier = [.1,.25,.5,1]
        percentchoice = choicemenu("What percent of your earnings would you like to invest",["10%", "25%", "50%", "100%"])
        if choice == 0:
            UnrealizedGains = UnrealizedGains + investStock(multiplier[percentchoice] * CashOnHand)
            CashOnHand = CashOnHand - multiplier[percentchoice] * CashOnHand
        if choice == 1:
            UnrealizedGains = UnrealizedGains + investIPO(multiplier[percentchoice] * CashOnHand)
            CashOnHand = CashOnHand - multiplier[percentchoice] * CashOnHand
        if choice == 2:
            UnrealizedGains = UnrealizedGains + investIndexFunds(multiplier[percentchoice] * CashOnHand)
            CashOnHand = CashOnHand - multiplier[percentchoice] * CashOnHand
    onmap = True

def investIndexFunds(amount):
    rate = (1+0.01*random.randint(4,8))
    result = amount*rate
    return result

def investIPO(amount):
    rate = (1+0.01*float(random.randint(-20,100)))
    result = amount*rate
    return result

def investStock(amount):
    rate = (1+0.01*random.float(randint(-10,30)))
    result = amount*rate
    return result

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
def draw_end_screen(years):
    WIN.fill(BACKGROUND_COLOR)
    
    # Display the congratulation message and the number of years
    font = pygame.font.Font(None, 36)
    text = font.render(f"Congratulations, you won in {years} years!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WIN.blit(text, text_rect)

    pygame.display.update()
            
def main():
    pygame.init()  # Initialize Pygame
    pygame.font.init()  # Initialize the font module
    clock = pygame.time.Clock()
    run = True
    in_home_screen = True
    end_screen = False
    Coordinates = pygame.Rect(300,300,CHAR_WIDTH,CHAR_HEIGHT)
    global onmap
    onmap = True
    global UnrealizedGains  # Declare UnrealizedGains as a global variable
    onmap = True
    UnrealizedGains = 0  # Initialize UnrealizedGains here
    
    while run:
        if CashOnHand > Target:
            end_screen = True
            run = False
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
        elif end_screen:
            draw_end_screen(Year)
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
            if keys[pygame.K_SPACE] and Coordinates.y < 423:
                spaceBar(Coordinates.x,Coordinates.y)
            if keys[pygame.K_n]:
                end_of_year()
                time.sleep(1)
            draw(Coordinates.x,Coordinates.y)
    pygame.quit()


if __name__ == "__main__":
    main()