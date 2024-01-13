import os
import random
import winsound
from cuvinte import cuvinte_usoare, cuvinte_grele
from ASCII__art import stages, logo
import pygame

class HangmanGame:
    def __init__(self):
        self.scor = 0
        self.scor_maxim = self.incarca_scor_maxim()
        self.lista = ""
        self.cuvant = ""
        self.numar_indicii = 3
        self.vieti = 6
        self.linii = []
        self.jocTerminat = False
        self.aCastigat = False
        self.rundaFinalizata = False
        self.nivel_Dificultate = 0
        self.muzica = True
        self.sfx = True

    def reset_game_state(self):
        self.vieti = 6
        self.jocTerminat = False

    def ghiceste_litera(self, litera_introdusa):
      for pozitie, litera in enumerate(self.cuvant):
        if litera == litera_introdusa:
          self.linii[pozitie] = litera

    def tine_scor(self):
        if self.numar_indicii == 3:
            self.scor += 250
        elif self.numar_indicii == 2:
            self.scor += 100
        else:
            self.scor += 50

        if self.scor_maxim < self.scor:
            self.scor_maxim = self.scor

            with open('Salvari/Scor.txt', 'w') as f:
                f.write(f"{self.scor_maxim}")


    def incarca_scor_maxim(self):
        if not os.path.exists('Salvari/'):
            os.makedirs('Salvari/')

            with open('Salvari/Scor.txt', 'w') as f:
                f.write(f"{self.scor}")
                scor_maxim = 0
                f.close()
        else:
            f = open("Salvari/Scor.txt", "r")
            scor_salvat = f.read()
            scor_maxim = int(scor_salvat)
            f.close()

        return scor_maxim

    def pune_desenul(self):
        print(stages[self.vieti])

    def alege_cuvant_random(self):
        if self.nivel_Dificultate == 1:
            self.lista = random.choice(list(cuvinte_grele.keys()))
            self.cuvant = random.choice(cuvinte_grele[self.lista])

        elif self.nivel_Dificultate == 0:
            self.lista = random.choice(list(cuvinte_usoare.keys()))
            self.cuvant = random.choice(cuvinte_usoare[self.lista])

    def indiciu(self):
        self.indexul_unei_litere = random.randint(0, len(self.cuvant) - 1)
        print(f"Indiciul este: {self.cuvant[self.indexul_unei_litere]}")

    def alegeNouCuvant(self):
        self.scor_maxim = self.incarca_scor_maxim()
        # self.tine_scor()
        self.jocTerminat = False
        self.numar_indicii = 3
        self.alege_cuvant_random()
        self.linii = ["_" for _ in range(len(self.cuvant))]


    def main_game(self):
        self.pune_desenul()
        self.alege_cuvant_random()
        self.linii = ["_" for _ in range(len(self.cuvant))]
        print(f"Domeniul : {self.lista} \n")
        print(' '.join(self.linii) + ' \n')

        while True:
            litera_introdusa = input("Ghiciti o litera: ").lower()
            os.system('cls')

            if litera_introdusa == "indiciu" and self.numar_indicii > 0:
                self.pune_desenul()
                winsound.PlaySound('Audio/Game Hint Sound.wav', 1)
                self.numar_indicii -= 1
                self.indiciu()
                print(f"Mai ai {self.numar_indicii} indiciu ramas! \n")
                print(f"{''.join(self.linii)} \n")

            elif litera_introdusa == "indiciu" and self.numar_indicii <= 0:
                self.pune_desenul()
                print("Ai epuizat deja numarul de indicii! \n")
                print(f"{''.join(self.linii)} \n")

            elif litera_introdusa == "skip":
                litera_introdusa = self.cuvant
                self.pune_desenul()
                self.tine_scor()
                print(f"Ai ghicit cuvantul! \n{self.cuvant} \n")
                break

            elif litera_introdusa == self.cuvant:
                self.pune_desenul()
                self.tine_scor()
                print(f"Ai ghicit cuvantul! \n{self.cuvant} \n")
                break

            else:
                self.ghiceste_litera(litera_introdusa)
                if litera_introdusa not in self.cuvant:
                    self.vieti -= 1
                    if self.vieti > 0:
                        self.pune_desenul()
                        winsound.PlaySound('Audio/Game Error Sound.wav', 1)
                    print(f"Litera {litera_introdusa} nu face parte din cuvant.")

                    if self.vieti == 0:
                        winsound.PlaySound('Audio/Game Lose Sound.wav', 1)
                        os.system('cls')
                        self.pune_desenul()
                        print(f"Scorul tau este {self.scor} \n")
                        print("Ai pierdut.")
                        print(f"Cuvantul era {self.cuvant}. \n")
                        break

                elif "_" not in self.linii:
                    winsound.PlaySound('Audio/Game Win Sound.wav', 1)
                    os.system('cls')
                    self.tine_scor()
                    print(f"Ai ghicit cuvantul! \n")
                    break

                elif litera_introdusa in self.cuvant:
                    self.pune_desenul()
                    print(f"Litera {litera_introdusa} este corecta (sau este deja ghicita).")
                    winsound.PlaySound('Audio/Generic Game Notification Sound.wav', 1)

                print(f"{''.join(self.linii)} \n")

        vrea_sa_continue = input("Vrei sa continui? Daca scrii da, jocul va continua! \n").lower()

        if vrea_sa_continue != "da":
            with open('Salvari/Scor.txt', 'w') as f:
                if self.scor_maxim < self.scor:
                    f.write(f"{self.scor}")
                else:
                    f.write(f"{self.scor_maxim}")

# Ruleaza Programul
if __name__ == "__main__":
    joc = HangmanGame()
    joc.main_game()
