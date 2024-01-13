import random
import pygame, sys
from pygame import mixer
from buton import Buton
from spanzuratoare import HangmanGame
from cursor import Cursor

mixer.init()
#sunet_click.load("Audio/birds-19624.mp3")
# sunet_click.set_volume(0.5)

sunet_click_1 = pygame.mixer.Sound("Audio/mixkit-handgun-release-1664.wav")
sunet_click_1.set_volume(.2)

sunet_pierdut = pygame.mixer.Sound("Audio/gun-shots-from-a-distance-7-96391.mp3")
sunet_pierdut.set_volume(.2)

sunet_click = pygame.mixer.Sound("Audio/mixkit-handgun-click-1660.mp3")
sunet_click.set_volume(0.2)

pygame.init()

resolutia_ecranului = pygame.display.Info()

# ecran = pygame.display.set_mode((1700, 1000))
ecran = pygame.display.set_mode((resolutia_ecranului.current_w, resolutia_ecranului.current_h))
pygame.display.set_caption("Spanzuratoarea")

cursor = Cursor(cale_imagine="interfata/cursor.png", ecran=ecran, latime=50, inaltime=50)

BG = pygame.image.load("interfata/meniu_principal.png")
screenUpdate_meniu = pygame.transform.scale(BG, (resolutia_ecranului.current_w, resolutia_ecranului.current_h))

BG_2 = pygame.image.load("interfata/joc_principal.png")
screenUpdate_joc = pygame.transform.scale(BG_2, (resolutia_ecranului.current_w, resolutia_ecranului.current_h))

BG_3 = pygame.image.load("interfata/fundal_0.png")
screenUpdate_dificultati = pygame.transform.scale(BG_3, (resolutia_ecranului.current_w, resolutia_ecranului.current_h))
def font(size):
    return pygame.font.Font("interfata/font2.otf", size)

def meniu_dificultate():
    joc = HangmanGame()
    joc.alege_cuvant_random()
    joc.indiciu()

    while True:
        
        ecran.blit(screenUpdate_dificultati, (0, 0))

        cautat = pygame.transform.scale(pygame.image.load("interfata/Mircea.png"), (550, 550))
        cautat_rect = cautat.get_rect()
        cautat_rect.center = (resolutia_ecranului.current_w * .13, resolutia_ecranului.current_h * .35)

        ecran.blit(cautat, cautat_rect)
        pozitie_mouse_joca = pygame.mouse.get_pos()

        joaca_text_1 = font(41).render("El e Mircea și urmează să fie judecat.", True, "black")
        joaca_rect_1 = joaca_text_1.get_rect(center=(resolutia_ecranului.current_w * .63,  (resolutia_ecranului.current_h * .2)))
        
        joaca_text_2 = font(42).render("Ghicește cuvântul pentru a-l salva.", True, "black")
        joaca_rect_2 = joaca_text_2.get_rect(center=(resolutia_ecranului.current_w * .63,  (resolutia_ecranului.current_h * .3)))

        joaca_text_indicatii = font(55).render("Primești doar două indicii!", True, "darkred")
        joaca_rect_indicatii = joaca_text_indicatii.get_rect(center=(resolutia_ecranului.current_w * .63, (resolutia_ecranului.current_h * .4)))

        joaca_text_dificultate = font(50).render("Alege dificultatea... cu grijă:", True, "black")
        joaca_rect_dificultate = joaca_text_dificultate.get_rect(center=(resolutia_ecranului.current_w * .63, (resolutia_ecranului.current_h * .5)))

        dificultate_GREU = Buton(imagine=None, pos=(resolutia_ecranului.current_w * 0.47, resolutia_ecranului.current_h * 0.74), text_input="GREU", font=font(75), culoare_baza="black", culoare_activare=("white"))
        dificultate_GREU.schimbaCuloare(pozitie_mouse_joca)
        dificultate_GREU.update(ecran)

        dificultate_USOR = Buton(imagine=None, pos=(resolutia_ecranului.current_w * 0.81, resolutia_ecranului.current_h * 0.74), text_input="UȘOR", font=font(75), culoare_baza="black", culoare_activare=("white"))
        dificultate_USOR.schimbaCuloare(pozitie_mouse_joca)
        dificultate_USOR.update(ecran)

        ecran.blit(joaca_text_1, joaca_rect_1)
        ecran.blit(joaca_text_2, joaca_rect_2)
        ecran.blit(joaca_text_indicatii, joaca_rect_indicatii)
        ecran.blit(joaca_text_dificultate, joaca_rect_dificultate)

        # joaca_inainte = Buton(imagine=None, pos=(resolutia_ecranului.current_w * .3, resolutia_ecranului.current_h * .6), text_input="INAINTE", font=font(75), culoare_baza="black", culoare_activare="white")
        joaca_inapoi = Buton(imagine=None, pos=(resolutia_ecranului.current_w * .63, resolutia_ecranului.current_h * .93), text_input="ÎNAPOI", font=font(75), culoare_baza="black", culoare_activare="white")

        # joaca_inainte.schimbaCuloare(pozitie_mouse_joca)
        # joaca_inainte.update(ecran)

        joaca_inapoi.schimbaCuloare(pozitie_mouse_joca)
        joaca_inapoi.update(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if joaca_inapoi.verificaInput(pozitie_mouse_joca):
                    sunet_click_1.play()
                    meniu_principal()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dificultate_GREU.verificaInput(pozitie_mouse_joca):
                    sunet_click.play()
                    joc.nivel_Dificultate = 1
                    joc.alegeNouCuvant()
                    joc_principal(joc)
                if dificultate_USOR.verificaInput(pozitie_mouse_joca):
                    sunet_click.play()
                    joc.nivel_Dificultate = 0
                    joc.alegeNouCuvant()
                    joc_principal(joc)
        
        cursor.update()
        pygame.display.update()

def arata_stadile(joc):
    imp = pygame.image.load("interfata/stages/stage_00.png")

    if joc.aCastigat:
            imp = pygame.image.load("interfata/stages/stage_08.png")
    else:
        if joc.vieti >= 6:
            imp = pygame.image.load("interfata/stages/stage_00.png")

        if joc.vieti == 5:
            imp = pygame.image.load("interfata/stages/stage_01.png")

        if joc.vieti == 4:
            imp = pygame.image.load("interfata/stages/stage_02.png")

        if joc.vieti == 3:
             imp = pygame.image.load("interfata/stages/stage_03.png")

        if joc.vieti == 2:
            imp = pygame.image.load("interfata/stages/stage_04.png")

        if joc.vieti == 1:
            imp = pygame.image.load("interfata/stages/stage_05.png")

        if joc.vieti <= 0:
            imp = pygame.image.load("interfata/stages/stage_06.png")

    ecran.blit(imp, (0, resolutia_ecranului.current_h - 512))  

def main_game_gui(joc):
    if joc.runda_finalizata:
        text_litera = font(85).render(joc.cuvant, True, "black")
        ecran.blit(text_litera,(500, resolutia_ecranului.current_h - 140))
    else:
        for litera in range(len(joc.linii)):
            text_litera = font(85).render(joc.linii[litera], True, "black")
            ecran.blit(text_litera,(500 + litera * 100, resolutia_ecranului.current_h - 140))
    
    semn_1 =pygame.transform.scale (pygame.image.load("interfata/semn_2.png"),(350,350) )
    semn_1_rect = semn_1.get_rect()
    semn_1_rect.center = (resolutia_ecranului.current_w * .12, resolutia_ecranului.current_h * .2)
    
    semn_2 =pygame.transform.scale (pygame.image.load("interfata/semn_2.png"),(350,350) )
    semn_2_rect = semn_2.get_rect()
    semn_2_rect.center = (resolutia_ecranului.current_w * .44, resolutia_ecranului.current_h * .2)
    
    semn_3 =pygame.transform.scale (pygame.image.load("interfata/semn_2.png"),(350,350) )
    semn_3_rect = semn_3.get_rect()
    semn_3_rect.center = (resolutia_ecranului.current_w * .66, resolutia_ecranului.current_h * .2)
    
    semn_4 =pygame.transform.scale (pygame.image.load("interfata/semn_2.png"),(350,350) )
    semn_4_rect = semn_4.get_rect()
    semn_4_rect.center = (resolutia_ecranului.current_w * .88, resolutia_ecranului.current_h * .2)
    
    scor_text = font(35).render(f"Scor: {joc.scor}", True, "black")
    # scor_rect = scor_text.get_rect(center=(resolutia_ecranului.current_w - 300, 100))
    
    ecran.blit(semn_1,semn_1_rect)
    ecran.blit(semn_1,semn_2_rect)
    ecran.blit(semn_1,semn_3_rect)
    ecran.blit(semn_1,semn_4_rect)
    ecran.blit(scor_text, (resolutia_ecranului.current_w * .78, 100))

    scor_maxim_text = font(35).render(f"Scor maxim: {joc.scor_maxim}", True, "black")
    # scor_maxim_rect = scor_maxim_text.get_rect(center=(resolutia_ecranului.current_w - 300, 200))
    ecran.blit(scor_maxim_text, (resolutia_ecranului.current_w * .66, 200))

    domeniu_text = font(35).render(f"Domeniul: {joc.lista}", True, "black")
    ecran.blit(domeniu_text, (resolutia_ecranului.current_w * .63, 300))
    
def joc_principal(joc):
    joc.aCastigat = False
    joc.runda_finalizata = False


    while True:
        ecran.blit(screenUpdate_joc, (0, 0))

        if joc.vieti <= 0:
            joc.runda_finalizata = True
            ecran.blit(screenUpdate_meniu, (0, 0))
            # castigat(joc)
            sunet_pierdut.play()
            pierdut(joc)

        if "_" not in joc.linii:
            joc.aCastigat = True
            joc.runda_finalizata = True
            ecran.blit(screenUpdate_meniu, (0, 0))
            castigat(joc)
        
        pozitie_mouse_continua = pygame.mouse.get_pos()
        
        main_game_gui(joc)
        
        continua_inapoi = Buton(imagine=None, pos=(180, resolutia_ecranului.current_h * .15), text_input="MENIU", font=font(50), culoare_baza="black", culoare_activare="white")
        continua_indiciu = Buton(imagine=None, pos=(190,resolutia_ecranului.current_h * .2), text_input="?", font=font(55), culoare_baza="black", culoare_activare="white")
    
        continua_indiciu.schimbaCuloare(pozitie_mouse_continua)
        continua_indiciu.update(ecran)

        continua_inapoi.schimbaCuloare(pozitie_mouse_continua)
        continua_inapoi.update(ecran)

        
        arata_stadile(joc)
        cursor.update()
        pygame.display.flip()   

        esteOLiteraValida = True
        char = ""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continua_inapoi.verificaInput(pozitie_mouse_continua):
                    sunet_click_1.play()
                    meniu_principal()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continua_indiciu.verificaInput(pozitie_mouse_continua):
                    indiciu(joc)

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (event.type == pygame.KEYDOWN and event.key == pygame.K_PRINTSCREEN):
                esteOLiteraValida = False
            elif event.type == pygame.KEYDOWN:
                char = event.unicode if event.unicode else chr(event.key)
                ghiceste_litera(char, joc)

def ghiceste_litera(litera_introdusa, joc):
    for pozitie, litera in enumerate(joc.cuvant):
        if litera == litera_introdusa:
            joc.linii[pozitie] = litera
    
    if litera_introdusa not in joc.cuvant:
        joc.vieti -= 1
                     
        if joc.vieti == 0:
            joc.jocTerminat = False

    elif "_" not in joc.linii:
        joc.tine_scor()
        joc.jocTerminat = True

def indiciu(joc):
    joc.indexul_unei_litere = random.randint(0, len(joc.cuvant) - 1)
    joc.numar_indicii -= 1

    while True:
        ecran.blit(screenUpdate_joc, (0, 0))
        arata_stadile(joc)
        main_game_gui(joc)
        pozite_mouse_indiciu = pygame.mouse.get_pos()

        if joc.numar_indicii > 0:
            indiciu_text = font(35).render(f"Indiciul este: {joc.cuvant[joc.indexul_unei_litere]}", True, "black")
            indiciu_rect = indiciu_text.get_rect(center=(300, 300))
            ecran.blit(indiciu_text, indiciu_rect)
        elif joc.numar_indicii <= 0:
            indiciu_0 = font(35).render(f"Nu mai ai indicii", True, "black")
            indiciu_0_rect = indiciu_0.get_rect(center=(300, 300))
            ecran.blit(indiciu_0, indiciu_0_rect)
        
        # indiciu_inapoi = Buton(imagine=None, pos=(30, 300), text_input="x", font=font(35), culoare_baza="black",
        #                         culoare_activare="white")

        # indiciu_inapoi.schimbaCuloare(pozite_mouse_indiciu)
        # indiciu_inapoi.update(ecran)

        cursor.update()
        pygame.display.flip()  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    joc_principal(joc)

        # cursor.update()
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
#        optiuni_inapoi = Buton(imagine=None, pos=(960, 500), text_input="INAPOI", font=font(86), culoare_baza="black", culoare_activare="white")
#
#        optiuni_inapoi.schimbaCuloare(pozite_mouse_optiuni)
#        optiuni_inapoi.update(ecran)
#
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                sys.exit()
#            if event.type == pygame.MOUSEBUTTONDOWN:
#                if optiuni_inapoi.verificaInput(pozite_mouse_optiuni):
#                    meniu_principal()
#        pygame.display.update()

def meniu_principal():
    menu_offset = 0
    moveDown = False

    while True:
        ecran.blit(screenUpdate_meniu, (0, 0))

        if menu_offset > 15:
            moveDown = True
        elif menu_offset < 0:
            moveDown = False

        if moveDown:
            menu_offset -= .05
        else:
            menu_offset += .05

        pozitie_mouse_meniu = pygame.mouse.get_pos()
        meniu_text = font(100).render("SPÂNZURĂTOAREA", True, "black")
        meniu_rect = meniu_text.get_rect(center=(resolutia_ecranului.current_w * .5, 0 + (resolutia_ecranului.current_w * .1)))

        meniu_rect = meniu_text.get_rect(center=(resolutia_ecranului.current_w * .5, menu_offset + (resolutia_ecranului.current_w * .1)))

        buton_start = Buton(imagine=None, pos=(resolutia_ecranului.current_w * .3, resolutia_ecranului.current_h * .6), text_input="START", font=font(100), culoare_baza="black", culoare_activare="white")

        #buton_optiuni = Buton(imagine=None, pos=(960, 650), text_input="INSTRUCTIUNI", font=font(76), culoare_baza="black", culoare_activare="white")

        buton_iesire = Buton(imagine=None, pos=(resolutia_ecranului.current_w * .7, resolutia_ecranului.current_h * .6), text_input="IEȘI", font=font(100), culoare_baza="black", culoare_activare="white")

        ecran.blit(meniu_text, meniu_rect)

        for button in [buton_start, buton_iesire]:
            button.schimbaCuloare(pozitie_mouse_meniu)
            button.update(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buton_start.verificaInput(pozitie_mouse_meniu):
                    sunet_click.play()
                    meniu_dificultate()
                #if buton_optiuni.verificaInput(pozitie_mouse_meniu):
                #    optiuni()
                if buton_iesire.verificaInput(pozitie_mouse_meniu):
                    sunet_click_1.play()
                    pygame.quit()
                    sys.exit()
        
        cursor.update()
        pygame.display.update()

#CAND PIERZI/CASTIGI APARE O IMAGINE CU O PANCARDA PE CARE SCRIE "AI PIERDUT/CASTIGAT!" SI BUTON PENTRU A CONITNUA SAU A IESI
def pierdut(joc):

    while True:        
        ecran.blit(screenUpdate_joc, (0, 0))
        main_game_gui(joc)
        arata_stadile(joc)
        #PANCARDA1 ESTE PENTRU AFISAJUL "AI PIERDUT/CASTIGAT!", IAR PANCARDA2 AR PUTEA FI FOLOSIT PENTRU TASTATURA

        pancarda = pygame.image.load("interfata/semn_3.png")
        pancarda_2 = pygame.transform.scale(pancarda, (600, 600))
        rect_pancarda = pancarda_2.get_rect()
        rect_pancarda.center = (resolutia_ecranului.current_w * .5, resolutia_ecranului.current_h * .5 + 80)

        ecran.blit(pancarda_2, rect_pancarda)

        joaca_text = font(40).render("Nu l-ai salvat!", True, "black")
        joaca_rect = joaca_text.get_rect()
        joaca_rect.center = (resolutia_ecranului.current_w * .5, resolutia_ecranului.current_h * .5)
        ecran.blit(joaca_text, joaca_rect)

        pierdut_inainte = Buton(imagine=None, pos=(resolutia_ecranului.current_w * .5 - 80, resolutia_ecranului.current_h * .5 + 130), text_input="CONTINUĂ",
                                 font=font(30), culoare_baza="black", culoare_activare="white")
        pierdut_inapoi = Buton(imagine=None, pos=(resolutia_ecranului.current_w * .5 + 110, resolutia_ecranului.current_h * .5 + 130), text_input="MENIU", font=font(30), culoare_baza="black",
                                culoare_activare="white")

        pozitie_mouse = pygame.mouse.get_pos()

        pierdut_inapoi.schimbaCuloare(pozitie_mouse)
        pierdut_inapoi.update(ecran)

        pierdut_inainte.schimbaCuloare(pozitie_mouse)
        pierdut_inainte.update(ecran)
        
        cursor.update()
        pygame.display.flip()  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pierdut_inapoi.verificaInput(pozitie_mouse):
                    sunet_click_1.play()
                    meniu_principal()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pierdut_inainte.verificaInput(pozitie_mouse):
                    sunet_click.play()
                    joc.reset_game_state()
                    joc.alegeNouCuvant()
                    joc_principal(joc)
        pygame.display.update()

def castigat(joc):
    viteza_animatiei = 0
    animeaza_alt_frame = False

    while True:
        ecran.blit(screenUpdate_joc, (0, 0))
        imp = pygame.image.load("interfata/stages/stage_00.png")

        if viteza_animatiei > .5:
            animeaza_alt_frame = True
        elif viteza_animatiei < 0:
            animeaza_alt_frame = False

        if animeaza_alt_frame:
            viteza_animatiei -= .05
            imp = pygame.image.load("interfata/stages/stage_07.png")
        else:
            viteza_animatiei += .05
            imp = pygame.image.load("interfata/stages/stage_08.png")

        ecran.blit(imp, (0, resolutia_ecranului.current_h - 512))
        joc.aCastigat = True
        main_game_gui(joc)

        pancarda = pygame.image.load("interfata/semn_3.png")
        #pancarda_2 = pygame.transform.scale(pancarda, (500, 250))
        rect_pancarda = pancarda.get_rect()
        rect_pancarda.center = (resolutia_ecranului.current_w * .5, resolutia_ecranului.current_h * .5 + 80)

        ecran.blit(pancarda, rect_pancarda)

        joaca_text = font(40).render("L-ai salvat!", True, "black")
        joaca_rect = joaca_text.get_rect()
        joaca_rect.center = (resolutia_ecranului.current_w * .5, resolutia_ecranului.current_h * .5)
        ecran.blit(joaca_text, joaca_rect)

        castigat_inainte = Buton(imagine=None, pos=(resolutia_ecranului.current_w * .5 - 80, resolutia_ecranului.current_h * .5 + 130), text_input="CONTINUĂ",
                                 font=font(30), culoare_baza="black", culoare_activare="white")
        castigat_inapoi = Buton(imagine=None, pos=(resolutia_ecranului.current_w * .5 + 110, resolutia_ecranului.current_h * .5 + 130), text_input="MENIU", font=font(30), culoare_baza="black",
                                culoare_activare="white")

        pozitie_mouse = pygame.mouse.get_pos()

        castigat_inainte.schimbaCuloare(pozitie_mouse)
        castigat_inainte.update(ecran)

        castigat_inapoi.schimbaCuloare(pozitie_mouse)
        castigat_inapoi.update(ecran)

        cursor.update()
        pygame.display.flip()  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if castigat_inapoi.verificaInput(pozitie_mouse):
                    sunet_click_1.play()
                    meniu_principal()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if castigat_inainte.verificaInput(pozitie_mouse):
                    sunet_click.play()
                    joc.reset_game_state()
                    joc.alegeNouCuvant()
                    joc_principal(joc)

        pygame.display.update()


meniu_principal()
