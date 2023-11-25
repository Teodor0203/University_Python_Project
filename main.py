import os  # Pentru A Sterge Consola
import random
import winsound # Pentru Audio
from Cuvinte import set_cuvinte

# \n spune programului sa lase spatiu (endl in c++ sau <br> in html)

# Arata o litera din cuvant
def indiciu():
  indiciu = ""
  numar_litere = len(cuvant)
  indexul_unei_litere = random.randint(0, numar_litere - 1)

  print(f"Indiciul este: {cuvant[indexul_unei_litere]}")

#Alege o cheie random si o valoare random din dictionar

def alegeCuvantRandom():
  global lista
  global cuvant
  lista = random.choice(list(set_cuvinte.keys()))
  cuvant = random.choice(set_cuvinte[lista])

# Meniul Principal, Turorial
def mainGameIntroduction():
  from ASCII__art import logo
  print(logo)
  print("\n")
  print("Bine ati venit la jocul de spanzuratoare!")
  print("Daca te blochezi la un cuvant, scrie indiciu in terminal!")
  print("Ai doua indicii pe runda! \n")
  input("Apasa enter pentru a incepe jocul!").lower()
  os.system('cls')
  mainGame()


# Jocul Principal
def mainGame():
  os.system('cls')
  
  # Numarul 1 este pentru a se auzi in background, de mentionat: functia nu suporta decat format .wav
  winsound.PlaySound('Audio/Game Win Sound.wav', 1)

  # Pregatirea jocului

  alegeCuvantRandom()
  print(f"Domeniul : {lista} \n")

  global numar_indicii
  numar_indicii = 2
  
  numar_litere = len(cuvant)

  sfarsit_joc = False
  vieti = 6
  linii = []

  for _ in range(numar_litere):
    linii += "_"

  print(' \n')
  print(' '.join(linii))
  print(' \n')

  # Principala functie a jocului
  while not sfarsit_joc:

    # Citim litera de la utilizator
    litera_introdusa = input("Ghiciti o litera: ").lower()
    os.system('cls')

    # Desenele ce reprezinta "spanzuratoarea" pe fiecare stadiu

    from ASCII__art import stages
    print(stages[vieti])  # De fixat, sare peste anumite stagii finale

    # Inlocuieste fiecare linie cu litera corespunzatoare sau de fapt..

    for pozitie in range(numar_litere):
      litera = cuvant[pozitie]

      if litera == litera_introdusa:
        linii[pozitie] = litera

    # Da un indiciu 
    # elif este similar cu else if in C++
    if ((litera_introdusa == "indiciu") and (numar_indicii > 0)):
      print(f"{''.join(linii)} \n")

      numar_indicii = numar_indicii - 1
      if (numar_indicii == 0):
        print("Nu mai ai indicii ramase! \n")
      else:
        winsound.PlaySound('Audio/Game Hint Sound.wav', 1)
        print(f"Mai ai {numar_indicii} indiciu ramas! \n")
      
      indiciu()
    elif ((litera_introdusa == "indiciu") and (numar_indicii <= 0)):
        print(f"{''.join(linii)} \n")
        print("Ai epuizat deja numarul de indicii! \n")
    else:
      # Caz 1: Litera introdusa nu se gaseste in cuvant

      if litera_introdusa not in cuvant:
        vieti -= 1
        print(f"Litera {litera_introdusa} nu face parte din cuvant.")

        if vieti > 0:
          winsound.PlaySound('Audio/Game Error Sound.wav', 1)

        # Nu mai sunt vieti, runda s-a terminat
        if vieti == 0:
          winsound.PlaySound('Audio/Game Lose Sound.wav', 1)
          os.system('cls')
          sfarsit_joc = True
          print(stages[0])
          print("Ai pierdut.")
          print(f"Cuvantul era {cuvant}. \n")

      # Caz 2:  Nu au mai ramas spatii necompletate. Runda s-a terminat

      if "_" not in linii:
        winsound.PlaySound('Audio/Game Win Sound.wav', 1)
        os.system('cls')
        sfarsit_joc = True
        print("Ai ghicit cuvantul! \n")

      # Caz 3:  Litera deja in cuvant

      if litera_introdusa in cuvant:
        print(f"Litera {litera_introdusa} este corecta (sau este deja ghicita).")

        if not sfarsit_joc:
          winsound.PlaySound('Audio/Generic Game Notification Sound.wav', 1)

      # Unesc toate elementele listei "linii" pentru a le transforma intr-un string

      print(f"{''.join(linii)} \n")

  # Daca s-a terminat runda, intreba jucatorul daca mai vrea sa continuie

  if sfarsit_joc:
    vreaSaContinuie = input(
        "Vrei sa continui? Daca scrii da, jocul va continua! \n").lower()

    # Daca da, continua
    if (vreaSaContinuie == "da"):
      sfarsit_joc = False
      mainGame()


# Ruleaza Programul
mainGameIntroduction()
