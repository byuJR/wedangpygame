import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Tradisional cafe")

BG = pygame.image.load("assets/Background.png")
BG2 = pygame.image.load("assets/Background.png")
BG3 = pygame.image.load("assets/Background3.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():

    global user_input
    global python_input

    user_input = 0
    python_input = 0

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG2, (0, 0))

        PLAY_TEXT = get_font(45).render("PER-WEDANGAN", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(920, 650), 
                            text_input="RA SIDO", font=get_font(40), base_color="Green", hovering_color="White")
        
        WJ = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(320, 150), 
                            text_input="WEDANG JAHE 20k", font=get_font(35), base_color="Green", hovering_color="White")
        
        WU = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(320, 230), 
                            text_input="WEDANG UWUH 24K", font=get_font(35), base_color="Green", hovering_color="White")
        
        WR = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(320, 310), 
                            text_input="WEDANG RONDE 20K", font=get_font(35), base_color="Green", hovering_color="White")
        
        BG = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(320, 390), 
                            text_input="BAJIGUR 9K", font=get_font(35), base_color="Green", hovering_color="White")
        
        ST = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(320, 470), 
                            text_input="SEKOTENG 15K", font=get_font(35), base_color="Green", hovering_color="White")
        
        BD = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(960, 390), 
                            text_input="BANDREK 7K", font=get_font(35), base_color="Green", hovering_color="White")
        
        STHJ = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(960, 150), 
                            text_input="STMJ 20K", font=get_font(35), base_color="Green", hovering_color="White")
        
        ET = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(960, 230), 
                            text_input="ES TELER 23K", font=get_font(35), base_color="Green", hovering_color="White")
        
        ED = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(960, 310), 
                            text_input="ES DAWET 12K", font=get_font(35), base_color="Green", hovering_color="White")
        
        CLEAR = Button(image=None, pos=(600, 600), 
                            text_input="CLEAR", font=get_font(35), base_color="Green", hovering_color="White")
        
        PAY = Button(image=None, pos=(920, 550), 
                            text_input="BAYAR", font=get_font(40), base_color="Green", hovering_color="White")
        
        
        WEDANG = [PLAY_BACK, WJ, WU, WR, BG, ST, BD, STHJ, ET, ED, CLEAR, PAY]
        
        for button in WEDANG:

            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
            

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WJ.checkForInput(PLAY_MOUSE_POS):
                    print("20")
                    user_input += 20
                    python_input += 20
                if WU.checkForInput(PLAY_MOUSE_POS):
                    print("24")
                    user_input += 24
                    python_input += 24
                if WR.checkForInput(PLAY_MOUSE_POS):
                    print("20")
                    user_input += 20
                    python_input += 20
                if BG.checkForInput(PLAY_MOUSE_POS):
                    print("9")
                    user_input += 9
                    python_input += 9
                if ST.checkForInput(PLAY_MOUSE_POS):
                    print("20")
                    user_input += 15
                    python_input += 15
                if BD.checkForInput(PLAY_MOUSE_POS):
                    print("7")
                    user_input += 7
                    python_input += 7
                if STHJ.checkForInput(PLAY_MOUSE_POS):
                    print("20")
                    user_input += 20
                    python_input += 20
                if ET.checkForInput(PLAY_MOUSE_POS):
                    print("23")
                    user_input += 23
                    python_input += 23
                if ED.checkForInput(PLAY_MOUSE_POS):
                    print("12")
                    user_input += 12
                    python_input += 12
                if CLEAR.checkForInput(PLAY_MOUSE_POS):
                    user_input = 0 
                    python_input = 0
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PAY.checkForInput(PLAY_MOUSE_POS):
                    PAYMENT()

        PLAY_TEXT = get_font(45).render(f"Total {user_input} k", True, "Green")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(320, 600))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
    
        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("Masih pagi makanan belum ada bro and sis.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def PAYMENT():
    global user_input
    global python_input
    global pay
    global kembalian

    pay = "0"
    kembalian = 0


    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG3, (0, 0))

        OPTIONS_TEXT = get_font(45).render("--Payment--", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        PLAY_TEXT = get_font(45).render(f"Total {user_input} k", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_TEXT = get_font(45).render(f"Uang Anda = {pay} k", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(380, 250))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_TEXT = get_font(45).render(f"Kembalian = {kembalian} k", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(900, 250))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        OPTIONS_BACK = Button(image=None, pos=(960, 600), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")
        CLEAR = Button(image=None, pos=(540, 550), 
                            text_input="CLEAR", font=get_font(30), base_color="Black", hovering_color="Green")
        BAYAR = Button(image=None, pos=(740, 550), 
                            text_input="BAYAR", font=get_font(30), base_color="Black", hovering_color="Green")
        NUMBER0 = Button(image=None, pos=(540, 300), 
                            text_input="0", font=get_font(30), base_color="Black", hovering_color="Green")
        NUMBER1 = Button(image=None, pos=(540, 350), 
                            text_input="1", font=get_font(30), base_color="Black", hovering_color="Green")
        NUMBER2 = Button(image=None, pos=(540, 400), 
                            text_input="2", font=get_font(30), base_color="Black", hovering_color="Green")
        NUMBER3 = Button(image=None, pos=(540, 450), 
                            text_input="3", font=get_font(30), base_color="Black", hovering_color="Green")
        NUMBER4 = Button(image=None, pos=(540, 500), 
                            text_input="4", font=get_font(30), base_color="Black", hovering_color="Green")
        NUMBER5 = Button(image=None, pos=(740, 300), 
                            text_input="5", font=get_font(30), base_color="Black", hovering_color="Green")
        NUMBER6 = Button(image=None, pos=(740, 350), 
                            text_input="6", font=get_font(30), base_color="Black", hovering_color="Green")
        NUMBER7 = Button(image=None, pos=(740, 400), 
                            text_input="7", font=get_font(30), base_color="Black", hovering_color="Green")
        NUMBER8 = Button(image=None, pos=(740, 450), 
                            text_input="8", font=get_font(30), base_color="Black", hovering_color="Green")
        NUMBER9 = Button(image=None, pos=(740, 500), 
                            text_input="9", font=get_font(30), base_color="Black", hovering_color="Green")
        
        CALCULATOR = [OPTIONS_BACK, CLEAR, BAYAR, NUMBER0, NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5, NUMBER6, NUMBER7, NUMBER8, NUMBER9]

        for number in CALCULATOR:
            number.changeColor(OPTIONS_MOUSE_POS)
            number.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if BAYAR.checkForInput(OPTIONS_MOUSE_POS):
                    pay_kem = int(pay) - user_input
                    kembalian += pay_kem
                if CLEAR.checkForInput(OPTIONS_MOUSE_POS):
                    pay = ""
                    kembalian = 0
                if NUMBER0.checkForInput(OPTIONS_MOUSE_POS):
                    pay += "0"
                if NUMBER1.checkForInput(OPTIONS_MOUSE_POS):
                    pay += "1"
                if NUMBER2.checkForInput(OPTIONS_MOUSE_POS):
                    pay += "2"
                if NUMBER3.checkForInput(OPTIONS_MOUSE_POS):
                    pay += "3"
                if NUMBER4.checkForInput(OPTIONS_MOUSE_POS):
                    pay += "4"
                if NUMBER5.checkForInput(OPTIONS_MOUSE_POS):
                    pay += "5"
                if NUMBER6.checkForInput(OPTIONS_MOUSE_POS):
                    pay += "6"
                if NUMBER7.checkForInput(OPTIONS_MOUSE_POS):
                    pay += "7"
                if NUMBER8.checkForInput(OPTIONS_MOUSE_POS):
                    pay += "8"
                if NUMBER9.checkForInput(OPTIONS_MOUSE_POS):
                    pay += "9"


        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TRADISIONAL CAFE", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 250), 
                            text_input="WEDANG", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="FOOD", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()