import pygame, sys
from pygame import mixer
from buton import Button
from main import HangmanGame

mixer.init()
mixer.music.load("Audio/birds-19624.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

pygame.init()


ecran = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Spanzuratoarea")

BG = pygame.image.load("interfata/bg2.jpg")
screenUpdate = pygame.transform.scale(BG, (1920, 1080))
def font(size):
    return pygame.font.Font("interfata/font2.otf", size)

def joaca():
    joc = HangmanGame()
    joc.alege_cuvant_random()
    joc.indiciu()
    while True:
        pozitie_mouse_joca = pygame.mouse.get_pos()

        ecran.blit(screenUpdate, (0, 0))

        joaca_text = font(45).render("Bine ati venit la jocul de spanzuratoare!!", True, "black")
        joaca_rect = joaca_text.get_rect(center=(960, 300))
        ecran.blit(joaca_text, joaca_rect)

        joaca_inainte = Button(image=None, pos=(960, 500), text_input="INAINTE", font=font(55), base_color="black", hovering_color="white")
        joaca_inapoi = Button(image=None, pos=(960, 650), text_input="INAPOI", font=font(55), base_color="black", hovering_color="white")


        joaca_inainte.changeColor(pozitie_mouse_joca)
        joaca_inainte.update(ecran)



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
                if joaca_inainte.checkForInput(pozitie_mouse_joca):
                    continua_1(joc)
        pygame.display.update()

def continua_1(joc):

    while True:
        pozitie_mouse_continua = pygame.mouse.get_pos()

        ecran.blit(screenUpdate, (0, 0))

        for litera in range(len(joc.cuvant)):
            text_litera = font(85).render("_", True, "black")
            ecran.blit(text_litera,(900 + litera * 100, 950))

        scor_text = font(35).render(f"Scor: {joc.scor}", True, "black")
        scor_rect = scor_text.get_rect(center=(1600, 100))

        scor_maxim_text = font(35).render(f"Scor maxim: {joc.scor_maxim}", True, "black")
        scor_maxim_rect = scor_maxim_text.get_rect(center=(1600, 200))
        ecran.blit(scor_maxim_text, scor_maxim_rect)

        ecran.blit(scor_text, scor_rect)

        continua_inapoi = Button(image=None, pos=(150, 1020), text_input="MENIU", font=font(50), base_color="black", hovering_color="white")
        continua_indiciu = Button(image=None, pos=(100, 100), text_input="?", font=font(55), base_color="black", hovering_color="white")

        continua_indiciu.changeColor(pozitie_mouse_continua)
        continua_indiciu.update(ecran)

        continua_inapoi.changeColor(pozitie_mouse_continua)
        continua_inapoi.update(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continua_inapoi.checkForInput(pozitie_mouse_continua):
                    meniu_principal()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continua_indiciu.checkForInput(pozitie_mouse_continua):
                    indiciu(joc)
        pygame.display.update()


def indiciu(joc):

    while True:
        pozite_mouse_indiciu = pygame.mouse.get_pos()

        indiciu_text = font(35).render(f"Indiciul este: {joc.cuvant[joc.indexul_unei_litere]}", True, "black")
        indiciu_rect = indiciu_text.get_rect(center=(300, 300))
        ecran.blit(indiciu_text, indiciu_rect)

        indiciu_inapoi = Button(image=None, pos=(30, 300), text_input="x", font=font(35), base_color="black",
                                hovering_color="white")

        indiciu_inapoi.changeColor(pozite_mouse_indiciu)
        indiciu_inapoi.update(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if indiciu_inapoi.checkForInput(pozite_mouse_indiciu):
                    continua_1(joc)
        pygame.display.update()
#def optiuni():
#    while True:
#        pozite_mouse_optiuni = pygame.mouse.get_pos()
#
#        ecran.blit(screenUpdate, (0, 0))
#
#        optiuni_text = font(45).render("indiciu - ", True, "black")
#        optiuni_rect = optiuni_text.get_rect(center=(960, 300))
#        ecran.blit(optiuni_text, optiuni_rect)
#
#        optiuni_inapoi = Button(image=None, pos=(960, 500), text_input="INAPOI", font=font(86), base_color="black", hovering_color="white")
#
#        optiuni_inapoi.changeColor(pozite_mouse_optiuni)
#        optiuni_inapoi.update(ecran)
#
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                sys.exit()
#            if event.type == pygame.MOUSEBUTTONDOWN:
#                if optiuni_inapoi.checkForInput(pozite_mouse_optiuni):
#                    meniu_principal()
#        pygame.display.update()
def meniu_principal():

    while True:

        ecran.blit(screenUpdate, (0, 0))

        pozitie_mouse_meniu = pygame.mouse.get_pos()
        meniu_text = font(100).render("SPANZURATOAREA", True, "black")
        meniu_rect = meniu_text.get_rect(center=(960,100))

        buton_start = Button(image=None, pos=(700, 600), text_input="START", font=font(100), base_color="black", hovering_color="white")

        #buton_optiuni = Button(image=None, pos=(960, 650), text_input="INSTRUCTIUNI", font=font(76), base_color="black", hovering_color="white")

        buton_iesire = Button(image=None, pos=(1200, 600), text_input="IESI", font=font(100), base_color="black", hovering_color="white")

        ecran.blit(meniu_text, meniu_rect)

        for button in [buton_start, buton_iesire]:
            button.changeColor(pozitie_mouse_meniu)
            button.update(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buton_start.checkForInput(pozitie_mouse_meniu):
                    joaca()
                #if buton_optiuni.checkForInput(pozitie_mouse_meniu):
                #    optiuni()
                if buton_iesire.checkForInput(pozitie_mouse_meniu):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

meniu_principal()
