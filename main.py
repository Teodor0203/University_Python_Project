import random
import pygame, sys
from pygame import mixer
from buton import Button
from spanzuratoare import HangmanGame


mixer.init()
mixer.music.load("Audio/birds-19624.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()

pygame.init()
resolutiaEcranului = pygame.display.Info()
# pygame.display.set_mode((infoObject.current_w, infoObject.current_h))


ecran = pygame.display.set_mode((resolutiaEcranului.current_w, resolutiaEcranului.current_h))
# ecran = pygame.display.set_mode((1700, 1000))
pygame.display.set_caption("Spanzuratoarea")

BG = pygame.image.load("interfata/bg2.jpg")
screenUpdate = pygame.transform.scale(BG, (resolutiaEcranului.current_w, resolutiaEcranului.current_h))
def font(size):
    return pygame.font.Font("interfata/font2.otf", size)

def joaca():
    joc = HangmanGame()
    joc.alege_cuvant_random()
    joc.indiciu()

    while True:
        pozitie_mouse_joca = pygame.mouse.get_pos()

        ecran.blit(screenUpdate, (0, 0))

        joaca_text = font(42).render("Bine ati venit la jocul de spanzuratoare!!", True, "black")
        joaca_rect = joaca_text.get_rect(center=(resolutiaEcranului.current_w / 2, 0 + (resolutiaEcranului.current_w * .1)))

       #SA AFISEZE DOMENIUL PE ECRAN, DAR TREBUIE PUS LA INCEPUTUL FIECAREI RUNDE, NU IN MENIUL "JOACA"

       #domeniu_text = font(42).render(f"Domeniul este: {joc.lista}", True, "black")
       #domeniu_rect = domeniu_text.get_rect(center=(resolutiaEcranului.current_w / 2, 0 +(resolutiaEcranului.current_w * 0.15)))

       #ecran.blit(domeniu_text, domeniu_rect)
        ecran.blit(joaca_text, joaca_rect)

        joaca_inainte = Button(image=None, pos=(resolutiaEcranului.current_w / 3, resolutiaEcranului.current_h / 1.7), text_input="INAINTE", font=font(55), base_color="black", hovering_color="white")
        joaca_inapoi = Button(image=None, pos=(resolutiaEcranului.current_w / 1.5, resolutiaEcranului.current_h / 1.7), text_input="INAPOI", font=font(55), base_color="black", hovering_color="white")


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
                    joc.alegeNouCuvant()
                    continua_1(joc)
        pygame.display.update()

def arataStadile(joc):
    imp = pygame.image.load("interfata/stages/stage_0.png")

    if joc.aCastigat:
            imp = pygame.image.load("interfata/stages/stage_8.png")
    else:
        if joc.vieti >= 6:
            imp = pygame.image.load("interfata/stages/stage_0.png")

        if joc.vieti == 5:
            imp = pygame.image.load("interfata/stages/stage_1.png")

        if joc.vieti == 4:
            imp = pygame.image.load("interfata/stages/stage_2.png")

        if joc.vieti == 3:
             imp = pygame.image.load("interfata/stages/stage_3.png")

        if joc.vieti == 2:
            imp = pygame.image.load("interfata/stages/stage_4.png")

        if joc.vieti == 1:
            imp = pygame.image.load("interfata/stages/stage_5.png")

        if joc.vieti <= 0:
            imp = pygame.image.load("interfata/stages/stage_6.png")

    ecran.blit(imp, (0, resolutiaEcranului.current_h - 512))
    pygame.display.flip()

def main_game_gui(joc):
    if joc.rundaFinalizata:
        text_litera = font(85).render(joc.cuvant, True, "black")
        ecran.blit(text_litera,(500, resolutiaEcranului.current_h - 140))
    else:
        for litera in range(len(joc.linii)):
            text_litera = font(85).render(joc.linii[litera], True, "black")
            ecran.blit(text_litera,(500 + litera * 100, resolutiaEcranului.current_h - 140))
    
    scor_text = font(35).render(f"Scor: {joc.scor}", True, "black")
    # scor_rect = scor_text.get_rect(center=(resolutiaEcranului.current_w - 300, 100))
    ecran.blit(scor_text, (resolutiaEcranului.current_w * .78, 100))

    scor_maxim_text = font(35).render(f"Scor maxim: {joc.scor_maxim}", True, "black")
    # scor_maxim_rect = scor_maxim_text.get_rect(center=(resolutiaEcranului.current_w - 300, 200))
    ecran.blit(scor_maxim_text, (resolutiaEcranului.current_w * .66, 200))
    
def continua_1(joc):
    joc.aCastigat = False
    joc.rundaFinalizata = False

    while True:
        ecran.blit(screenUpdate, (0, 0))

        if joc.vieti <= 0:
            joc.rundaFinalizata = True
            ecran.blit(screenUpdate, (0, 0))
            # castigat(joc)
            pierdut(joc)

        if "_" not in joc.linii:
            joc.aCastigat = True
            joc.rundaFinalizata = True
            ecran.blit(screenUpdate, (0, 0))
            castigat(joc)
        
        pozitie_mouse_continua = pygame.mouse.get_pos()

        # for litera in range(len(joc.cuvant)):
        #     text_litera = font(85).render("_", True, "black")
        #     ecran.blit(text_litera,(300 + litera * 100, resolutiaEcranului.current_h - 85 * 2))

        continua_inapoi = Button(image=None, pos=(150, resolutiaEcranului.current_h * .2), text_input="MENIU", font=font(50), base_color="black", hovering_color="white")
        continua_indiciu = Button(image=None, pos=(100, 100), text_input="?", font=font(55), base_color="black", hovering_color="white")

        continua_indiciu.changeColor(pozitie_mouse_continua)
        continua_indiciu.update(ecran)

        continua_inapoi.changeColor(pozitie_mouse_continua)
        continua_inapoi.update(ecran)

        main_game_gui(joc)
        arataStadile(joc)

        # Main loop        
        # Define a variable to store the character
        esteOLiteraValida = True
        char = ""

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

    while True:
        pozite_mouse_indiciu = pygame.mouse.get_pos()

        #Verifica daca mai ai indicii si afiseaza indiciul.
        if joc.numar_indicii > 0:
            indiciu_text = font(35).render(f"Indiciul este: {joc.cuvant[joc.indexul_unei_litere]}", True, "black")
            indiciu_rect = indiciu_text.get_rect(center=(300, 300))
            ecran.blit(indiciu_text, indiciu_rect)
        
        #Atunci cand ramai fara indicii iti spune ca nu mai ai indicii.
        elif joc.numar_indicii <= 0:
            indiciu_0 = font(35).render(f"Nu mai ai indicii", True, "black")
            indiciu_0_rect = indiciu_0.get_rect(center=(300, 300))
            ecran.blit(indiciu_0, indiciu_0_rect)
        
        
        indiciu_inapoi = Button(image=None, pos=(30, 300), text_input="x", font=font(35), base_color="black",
                                hovering_color="white")

        indiciu_inapoi.changeColor(pozite_mouse_indiciu)
        indiciu_inapoi.update(ecran)

        #ATUNCI CAND APASAM PE "?" CA SA APARA INDICIUL, IMAGINEA CU SPANZURATOAREA DISPAREA. ASA NU MAI DISPARE
        arataStadile(joc)

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
    testI = 0
    moveDown = False

    while True:

        ecran.blit(screenUpdate, (0, 0))

        if testI > 15:
            moveDown = True
        elif testI < 0:
            moveDown = False

        if moveDown:
            testI -= .05
        else:
            testI += .05

        pozitie_mouse_meniu = pygame.mouse.get_pos()
        meniu_text = font(100).render("SPANZURATOAREA", True, "black")
        meniu_rect = meniu_text.get_rect(center=(resolutiaEcranului.current_w / 2, 0 + (resolutiaEcranului.current_w * .1)))

        meniu_rect = meniu_text.get_rect(center=(resolutiaEcranului.current_w / 2, testI + (resolutiaEcranului.current_w * .1)))

        buton_start = Button(image=None, pos=(resolutiaEcranului.current_w / 3, resolutiaEcranului.current_h / 1.7), text_input="START", font=font(100), base_color="black", hovering_color="white")

        #buton_optiuni = Button(image=None, pos=(960, 650), text_input="INSTRUCTIUNI", font=font(76), base_color="black", hovering_color="white")

        buton_iesire = Button(image=None, pos=(resolutiaEcranului.current_w / 1.5, resolutiaEcranului.current_h / 1.7), text_input="IESI", font=font(100), base_color="black", hovering_color="white")

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

#CAND PIERZI/CASTIGI APARE O IMAGINE CU O PANCARDA PE CARE SCRIE "AI PIERDUT/CASTIGAT!" SI BUTON PENTRU A CONITNUA SAU A IESI
def pierdut(joc):

    while True:
        main_game_gui(joc)
        arataStadile(joc)
        #PANCARDA1 ESTE PENTRU AFISAJUL "AI PIERDUT/CASTIGAT!", IAR PANCARDA2 AR PUTEA FI FOLOSIT PENTRU TASTATURA

        pancarda = pygame.image.load("interfata/pancarda1.png")
        pancarda_2 = pygame.transform.scale(pancarda, (500, 250))
        rect_pancarda = pancarda_2.get_rect()
        rect_pancarda.center = (resolutiaEcranului.current_w * .5, resolutiaEcranului.current_h * .5 + 80)

        ecran.blit(pancarda_2, rect_pancarda)

        joaca_text = font(40).render("Ai pierdut!", True, "black")
        joaca_rect = joaca_text.get_rect()
        joaca_rect.center = (resolutiaEcranului.current_w * .5, resolutiaEcranului.current_h * .5)
        ecran.blit(joaca_text, joaca_rect)

        pierdut_inainte = Button(image=None, pos=(resolutiaEcranului.current_w * .5 - 80, resolutiaEcranului.current_h * .5 + 150), text_input="CONTINUA",
                                 font=font(30), base_color="black", hovering_color="white")
        pierdut_inapoi = Button(image=None, pos=(resolutiaEcranului.current_w * .5 + 110, resolutiaEcranului.current_h * .5 + 150), text_input="MENIU", font=font(30), base_color="black",
                                hovering_color="white")

        pozitie_mouse = pygame.mouse.get_pos()

        pierdut_inapoi.changeColor(pozitie_mouse)
        pierdut_inapoi.update(ecran)

        pierdut_inainte.changeColor(pozitie_mouse)
        pierdut_inainte.update(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pierdut_inapoi.checkForInput(pozitie_mouse):
                    meniu_principal()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pierdut_inainte.checkForInput(pozitie_mouse):
                    joc.reset_game_state()
                    joc.alegeNouCuvant()
                    continua_1(joc)
        pygame.display.update()

def castigat(joc):
    while True:
        joc.aCastigat = True
        main_game_gui(joc)
        arataStadile(joc)

        pancarda = pygame.image.load("interfata/pancarda1.png")
        pancarda_2 = pygame.transform.scale(pancarda, (500, 250))
        rect_pancarda = pancarda_2.get_rect()
        rect_pancarda.center = (resolutiaEcranului.current_w * .5, resolutiaEcranului.current_h * .5 + 80)

        ecran.blit(pancarda_2, rect_pancarda)

        joaca_text = font(40).render("Ai ghicit!", True, "black")
        joaca_rect = joaca_text.get_rect()
        joaca_rect.center = (resolutiaEcranului.current_w * .5, resolutiaEcranului.current_h * .5)
        ecran.blit(joaca_text, joaca_rect)

        castigat_inainte = Button(image=None, pos=(resolutiaEcranului.current_w * .5 - 80, resolutiaEcranului.current_h * .5 + 150), text_input="CONTINUA",
                                 font=font(30), base_color="black", hovering_color="white")
        castigat_inapoi = Button(image=None, pos=(resolutiaEcranului.current_w * .5 + 110, resolutiaEcranului.current_h * .5 + 150), text_input="MENIU", font=font(30), base_color="black",
                                hovering_color="white")

        pozitie_mouse = pygame.mouse.get_pos()

        castigat_inainte.changeColor(pozitie_mouse)
        castigat_inainte.update(ecran)

        castigat_inapoi.changeColor(pozitie_mouse)
        castigat_inapoi.update(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if castigat_inapoi.checkForInput(pozitie_mouse):
                    meniu_principal()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if castigat_inainte.checkForInput(pozitie_mouse):
                    joc.reset_game_state()
                    joc.alegeNouCuvant()
                    continua_1(joc)

        pygame.display.update()


meniu_principal()
