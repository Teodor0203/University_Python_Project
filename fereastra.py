import pygame, sys
from pygame import mixer
from buton import Button

mixer.init()
mixer.music.load("Audio/birds-19624.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()


pygame.init()

ecran = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Spanzuratoarea")

BG = pygame.image.load("interfata/bg.png")

def font(size):
    return pygame.font.Font("interfata/font.ttf", size)

def joaca():
    while True:
        pozitie_mouse_joca = pygame.mouse.get_pos()

        ecran.blit(BG, (0,0))

        joaca_text = font(45).render("Aici va fi jocul", True, "blueviolet")
        joaca_rect = joaca_text.get_rect(center=(960, 300))
        ecran.blit(joaca_text, joaca_rect)

        joaca_inapoi = Button(image=None, pos=(960, 500), text_input="INAPOI", font=font(75), base_color="blueviolet", hovering_color="blue")
        joaca_indiciu = Button(image=None, pos=(1900,100), text_input="?", font=font(75),base_color="black", hovering_color="white")

        joaca_indiciu.changeColor(pozitie_mouse_joca)
        joaca_indiciu.update(ecran)

        joaca_inapoi.changeColor(pozitie_mouse_joca)
        joaca_inapoi.update(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if joaca_inapoi.checkForInput(pozitie_mouse_joca):
                    meniu_principal()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if joaca_indiciu.checkForInput(pozitie_mouse_joca):
                    indiciu()
        pygame.display.update()

def indiciu():
    while True:
        pozite_mouse_indiciu = pygame.mouse.get_pos()

        ecran.blit(BG, (0, 0))

        indiciu_text = font(45).render("Indiciul este...", True, "black")
        indiciu_rect = indiciu_text.get_rect(center=(960, 300))
        ecran.blit(indiciu_text, indiciu_rect)

        indiciu_inapoi = Button(image=None, pos=(960, 500), text_input="INAPOI", font=font(86), base_color="blueviolet",
                                hovering_color="blue")

        indiciu_inapoi.changeColor(pozite_mouse_indiciu)
        indiciu_inapoi.update(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if indiciu_inapoi.checkForInput(pozite_mouse_indiciu):
                    joaca()
        pygame.display.update()
def optiuni():
    while True:
        pozite_mouse_optiuni = pygame.mouse.get_pos()

        ecran.blit(BG, (0, 0))

        optiuni_text = font(45).render("Aici vor fi instructiunile", True, "black")
        optiuni_rect = optiuni_text.get_rect(center=(960, 300))
        ecran.blit(optiuni_text, optiuni_rect)

        optiuni_inapoi = Button(image=None, pos=(960, 500), text_input="INAPOI", font=font(86), base_color="blueviolet", hovering_color="blue")

        optiuni_inapoi.changeColor(pozite_mouse_optiuni)
        optiuni_inapoi.update(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if optiuni_inapoi.checkForInput(pozite_mouse_optiuni):
                    meniu_principal()
        pygame.display.update()
def meniu_principal():

    while True:

        ecran.blit(BG,(0, 0))

        pozitie_mouse_meniu = pygame.mouse.get_pos()
        meniu_text = font(100).render("MENIUL PRINCIPAL", True, "blueviolet")
        meniu_rect = meniu_text.get_rect(center=(960,100))

        buton_start = Button(image=None, pos=(960, 250), text_input="START", font=font(75), base_color="blueviolet", hovering_color="blue")

        buton_optiuni = Button(image=None, pos=(960, 350), text_input="INSTRUCTIUNI", font=font(76), base_color="blueviolet", hovering_color="blue")

        buton_iesire = Button(image=None, pos=(960, 450), text_input="IESI", font=font(75), base_color="blueviolet", hovering_color="blue")

        ecran.blit(meniu_text, meniu_rect)

        for button in [buton_start, buton_optiuni, buton_iesire]:
            button.changeColor(pozitie_mouse_meniu)
            button.update(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buton_start.checkForInput(pozitie_mouse_meniu):
                    joaca()
                if buton_optiuni.checkForInput(pozitie_mouse_meniu):
                    optiuni()
                if buton_iesire.checkForInput(pozitie_mouse_meniu):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

meniu_principal()