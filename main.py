import os  # Pentru A Sterge Consola
import os.path
import random
import winsound # Pentru Audio
from Cuvinte import set_cuvinte

# \n spune programului sa lase spatiu (endl in c++ sau <br> in html)

def puneDesenul():
  # Desenele ce reprezinta "spanzuratoarea" pe fiecare stadiu
  from ASCII__art import stages
  print(stages[vieti])  # De fixat, sare peste anumite stagii finale

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

# Initializeaza Scorul
scor = 0

# Create a new folder
if not os.path.exists('Salvari/'):
  os.makedirs('Salvari/')

  # Create a new file inside the folder
  with open('Salvari/Scor.txt', 'w') as f:
    f.write(f"{scor}")
    scorMaxim = 0
    f.close()

else:
  # Create a new file inside the folder
  f = open("Salvari/Scor.txt", "r")
  scorSalvat = f.read()
  scorMaxim = int(scorSalvat)
  f.close()

def tineScor():
  global scor
  global scorMaxim
  if (numar_indicii == 1):
    scor += 100
  elif (numar_indicii == 0):
    scor += 50
  else:
    scor += 200

  # Create a new file inside the folder
  print(f"Scorul tau este {scor}")

  if (scorMaxim >= scor):
    print(f"Scorul tau maxim este {scorMaxim}")
  else:
    print(f"Scorul tau maxim este {scor}")

# Meniul Principal, Turorial
def mainGameIntroduction():
  from ASCII__art import logo
  print(logo)
  print("\n")
  print("Bine ati venit la jocul de spanzuratoare!")
  print("Daca te blochezi la un cuvant, scrie indiciu in terminal!")
  print("Ai doua indicii pe runda! \n")
  print("Daca ti-ai dat seama cuvantul, scrie-l! \n")
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
  
  global numar_indicii
  numar_indicii = 2
  
  numar_litere = len(cuvant)

  sfarsit_joc = False
  global vieti
  vieti = 6
  linii = []
  puneDesenul()

  for _ in range(numar_litere):
    linii += "_"

  print(f"Domeniul : {lista} \n")
  print(' '.join(linii) + ' \n')

  # Principala functie a jocului
  while not sfarsit_joc:
    
    # Citim litera de la utilizator
    litera_introdusa = input("Ghiciti o litera: ").lower()
    os.system('cls')

    # Inlocuieste fiecare linie cu litera corespunzatoare sau de fapt..

    for pozitie in range(numar_litere):
      litera = cuvant[pozitie]

      if litera == litera_introdusa:
        linii[pozitie] = litera

    # Da un indiciu 
    # elif este similar cu else if in C++
    if ((litera_introdusa == "indiciu") and (numar_indicii > 0)):
      puneDesenul()

      winsound.PlaySound('Audio/Game Hint Sound.wav', 1)
      numar_indicii = numar_indicii - 1
      
      indiciu()

      if (numar_indicii == 0):
        print("Nu mai ai indicii ramase! \n")
      else:
        print(f"Mai ai {numar_indicii} indiciu ramas! \n")

      print(f"{''.join(linii)} \n")
      
    elif ((litera_introdusa == "indiciu") and (numar_indicii <= 0)):
        puneDesenul()
        print("Ai epuizat deja numarul de indicii! \n")
        print(f"{''.join(linii)} \n")

    elif (litera_introdusa == "skip"):
        litera_introdusa = cuvant
        puneDesenul()
        tineScor()
        print("Ai ghicit cuvantul! \n")
        print(f"{cuvant} \n")
        sfarsit_joc = True

    elif (litera_introdusa == cuvant):
        puneDesenul()
        tineScor()
        print("Ai ghicit cuvantul! \n")
        print(f"{cuvant} \n")
        sfarsit_joc = True
    else:
      # Caz 1: Litera introdusa nu se gaseste in cuvant

      if litera_introdusa not in cuvant:
        vieti -= 1

        if vieti > 0:
          puneDesenul()
          winsound.PlaySound('Audio/Game Error Sound.wav', 1)

        print(f"Litera {litera_introdusa} nu face parte din cuvant.")

        # Nu mai sunt vieti, runda s-a terminat
        if vieti == 0:
          winsound.PlaySound('Audio/Game Lose Sound.wav', 1)
          os.system('cls')
          sfarsit_joc = True
          from ASCII__art import stages
          print(stages[0])
          print(f"Scorul tau este {scor} \n")
          print("Ai pierdut.")
          print(f"Cuvantul era {cuvant}. \n")

      # Caz 2:  Nu au mai ramas spatii necompletate. Runda s-a terminat

      elif "_" not in linii:
        winsound.PlaySound('Audio/Game Win Sound.wav', 1)
        sfarsit_joc = True
        os.system('cls')
        tineScor()
        print("Ai ghicit cuvantul! \n")
      # Caz 3:  Litera deja in cuvant

      elif litera_introdusa in cuvant:
        puneDesenul()
        print(f"Litera {litera_introdusa} este corecta (sau este deja ghicita).")

        if not sfarsit_joc:
          winsound.PlaySound('Audio/Generic Game Notification Sound.wav', 1)

      # Unesc toate elementele listei "linii" pentru a le transforma intr-un string
      print(f"{''.join(linii)} \n")

  # Daca s-a terminat runda, intreba jucatorul daca mai vrea sa continuie

  if sfarsit_joc:
    vreaSaContinuie = input("Vrei sa continui? Daca scrii da, jocul va continua! \n").lower()

    # Daca da, continua
    if (vreaSaContinuie == "da"):
      sfarsit_joc = False
      mainGame()
    else:
      with open('Salvari/Scor.txt', 'w') as f:
        if (scorMaxim < scor):
          f.write(f"{scor}")
          f.close()
        else:
          f.write(f"{scorMaxim}")
          f.close()


# Ruleaza Programul
mainGameIntroduction()
