
#Joc de spanzuratoare, realizat la 8.11.2023. Trebuie imbunatatit.. mult :)))
#De adaugat mai multe librarii si dictionare
#Daca ghicesti cuvantul sau ramai fara vieti, se imchide automat
#Daca ai de exemplu, 3 litere puse si sa spunem ca iti dai seama care este cuvantul complet, atunci cand il scrii
# nu completeaza toate spatiile si spune ca ai castigat
#Poate reusesc sa tin evidenta scorului


import os #librarie care imi permite sa adaug in program comanda os.system('cls') care da clear la consola

from ASCII_art import logo #am adus si am afisat logoul
print(logo)
print(" ") #Nu stiu cum altfel sa creez spatiu intre logo si primul mesaj
print("Bine ati venit la jocul de spanzuratoare!")
print("     Cuvintele sunt nume de animale.     ") #Nu stiu cum altfel sa centrez text -- sper sa mai aduc modificari

"""Acum voi face programul sa aleaga un cuvant random"""

import random #librarie pentru random
from Cuvinte import animale #din fisierul cuvinte aduc lista animale

cuvant = random.choice(animale) #alege un cuvant random din lista
numar_litere = len(cuvant) #numarul de litere pe care le are cuvantul adus din lista

'''Creez o variabila care ne spune daca jocul s-a terminat sau nu'''

sfarsit_joc = False #Asta ma va ajuta mai tarziu in program sa opresc loop-ul while

'''Creez o variabila pentru numarul de vieti, vom avea 6 incercari'''

vieti = 6

'''Creez lista si vom afisa atatea linii cate litere are cuvantul'''

linii = [] #creez o lista goala

for _ in range(numar_litere): #verifica numarul de litere din cuvantul random si adauga atatea linii cate litere are cuvantul
    linii += "_"

print(' ') #aceeasi problema ca si la inceput, nu stiu cum sa fac altfel
print(' '.join(linii)) #Unesc toate elementele listei "linii" pentru a le transforma intr-un string  
print(' ')


#Am incercat sa fac in asa fel incat programul sa afiseze prima litera a cuvantului in caz de jucatorul scire "indiciu"
#dar nu am reusit sa scad vietile -- de revazut

#indiciu = input("Pentru indiciu, scrieti <indiciu>. Veti pierde o viata.\n").lower()
#if indiciu == "indiciu":
#
#        lit = cuvant[0]
#        linii[0] = lit  #am incercat eu ceva logica, functioneaza partial, imi arata prima litera din cuvant, dar nu scade viata
#        vieti -= 1
#        print(' '.join(linii)) #Unesc toate elementele listei "linii" pentru a le transforma intr-un string

'''Voi crea un loop astfel incat jucatorul sa poata ghici cate o litera pana cand
    gaseste cuvantul sau ramane fara vieti'''

while not sfarsit_joc:

    ghiceste = input("Ghiciti o litera: ").lower() #Variabila care cere jucatorului sa introduca o valoare
    os.system('cls') #curata ecranul (consola)

    from ASCII_art import stages #Aduc desenele care reprezinta "spanzuratoarea" pe fiecare stadiu
    print(stages[vieti]) #Nu imi afiseaza desenul complet atunci cand raman fara vieti -- de revazut

    for pozitie in range(numar_litere): #inlocuieste fiecare linie cu litera corespunzatoare sau de fapt..
        litera = cuvant[pozitie]

        if litera == ghiceste:
            linii[pozitie] = litera

#Verific daca jucatorul a ales corect

    if ghiceste not in cuvant: #Daca litera nu e in cuvant, se scade o viata si se spune jucatorului ca litera nu face parte din cuvant
        vieti -= 1
        print(f"Litera {ghiceste} nu face parte din cuvant.")
        if vieti == 0:                                          #cand vietile ajung la 0, sfarsit_jos se schimba in True
                                                                # , astfel se incheie loop-ul si se termina jocul.
            sfarsit_joc = True
            print(stages[0])
            print("Ai pierdut.")
            print(f"Cuvantul era {cuvant}.")

#Verific daca jucatorul a ghicit cuvantul

    if "_" not in linii:    #verifica daca taote liniile _ au fost inlocuite de litere. Daca da, atunci se termina jocul.
        sfarsit_joc = True
        print("Ai ghicit cuvantul.")

    if ghiceste in cuvant:                                                 
        print(f"Litera {ghiceste} este corecta (sau este deja ghicita).") #Aici chiar daca ghicesti litera pentru prima data, tot apare acest text, nu stiu cum sa fac sa apara
                                                                          #doar atunci cand alegi din nou aceeasi litera

#Unesc toate elementele listei "linii" pentru a le transforma intr-un string

    print(f"{''.join(linii)}")