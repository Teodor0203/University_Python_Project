import os  # Pentru A Sterge Consola
import random

# \n spune programului sa lase spatiu (endl in c++ sau <br> in html)


# Arata o litera din cuvant
def indiciu():
  indiciu = ""
  numar_litere = len(cuvant)
  indexul_unei_litere = random.randint(0, numar_litere - 1)

  print(f"Indiciul este: {cuvant[indexul_unei_litere]}")


# Meniul Principal
def mainGameIntroduction():
  from ASCII__art import logo
  print(logo)
  print("\n")
  print("Bine ati venit la jocul de spanzuratoare!")
  print("Cuvintele sunt nume de animale! \n")
  print("Daca te blochezi la un cuvant, scrie indiciu in terminal!")
  print("Ai 2 indicii pe runda! \n")
  input("Apasa enter pentru a incepe jocul!").lower()
  os.system('cls')
  mainGame()


# Jocul Principal
def mainGame():
  os.system('cls')

  # Pregatirea jocului
  from Cuvinte import animale

  global numar_indicii
  numar_indicii = 2

  global cuvant
  cuvant = random.choice(animale)
  numar_litere = len(cuvant)

  sfarsit_joc = False
  vieti = 6
  linii = []

  for _ in range(numar_litere):
    linii += "_"

  print(' ')
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
      print(f"{numar_indicii} indiciu ramas! \n")
      
      indiciu()
    elif ((litera_introdusa == "indiciu") and (numar_indicii <= 0)):
      print(f"{''.join(linii)} \n")
      print(f"Ai epuizat numarul de indicii! \n")
    else:
      # Litera introdusa nu se gaseste in cuvant

      if litera_introdusa not in cuvant:
        vieti -= 1
        print(f"Litera {litera_introdusa} nu face parte din cuvant.")

        # Nu mai sunt vieti, runda s-a terminat

        if vieti == 0:
          os.system('cls')
          sfarsit_joc = True
          print(stages[0])
          print("Ai pierdut.")
          print(f"Cuvantul era {cuvant}. \n")

      # Nu au mai ramas spatii necompletate. Runda s-a terminat

      if "_" not in linii:
        os.system('cls')
        sfarsit_joc = True
        print("Ai ghicit cuvantul! \n")

      # Litera deja in cuvant

      if litera_introdusa in cuvant:
        print(f"Litera {litera_introdusa} este corecta (sau este deja ghicita).")

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
